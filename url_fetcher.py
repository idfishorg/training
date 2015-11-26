
import urllib2
import simplejson
import cStringIO

def fetch(search):
    fetcher = urllib2.build_opener()
    search_url = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + search + "&start=0"
    f = fetcher.open(search_url)
    output = simplejson.load(f)
    results = output['responseData']['results']
    urls = []
    for result in results:
        urls.append(result['url'])
    return urls


if __name__ == "__main__":
    urls = fetch("car")
    print urls
