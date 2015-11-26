search = search.replace(" ","%20")
  site= "http://www.google.co.in/search?q="+search+"&tbm=isch&tbs=isz:l"
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}
  QtGui.qApp.processEvents()
  req = urllib2.Request(site, headers=hdr)

  try:
      QtGui.qApp.processEvents()
      page = urllib2.urlopen(req)
  except urllib2.HTTPError, e:
      print e.fp.read()  
  QtGui.qApp.processEvents()
  content = page.read()
  #print content
  soup = BeautifulSoup(content)
  results = soup.findAll("a")
  linkarray = soup.find_all(attrs={"class": "rg_meta"})
  #print linkarray
  refer_rl=[]
  total=len(linkarray)
  i=0
  for divs in linkarray:
    i=i+1
    stri=str(divs)
    refer_url=stri.split('%3B')
    try:
        QtGui.qApp.processEvents()
        url=urllib.unquote(refer_url[2]).decode('utf8') 
        url=urllib.unquote(url).decode('utf8') 
        #os.system('wget '+url)
        #f = open('links.txt', 'a')
        #f.write(url+'\n')
        form.textBrowser.append(url)
        form.progressBar.setProperty("value", i*100/total)
        time.sleep(0.05)

    except:
        continue
  #os.system('aria2c -i links.txt -x 16')
  #os.system('rm links.txt')
  print "All good, you can download now"
