import urllib
import mechanize
from bs4 import BeautifulSoup
from urlparse import urlparse
from url_fetcher import fetch
from metamind.api import ClassificationData, ClassificationModel, set_api_key

k="tbYAbBvgQRgi9QfWRvs6NXAqcIFrp7p8ycYDctzT2duT8vlKkV"
set_api_key(k)

def getImageUrl(name):
        browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent', 'Mozilla')]
	#htmltext = browser.open("https://www.google.com/search?q=r&source=lnms&tbm=isch&sa=X&ved=0ahUKEwil0uyH8qLJAhXKcT4KHX6JCjYQ_AUIBygB&biw=1167&bih=593#tbm=isch&q=car")
	#htmltext = browser.open("https://www.google.com/search?q=fish&biw=1920&bih=916&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiN6OXs_KLJAhUJdD4KHbZ1CLAQ_AUIBigB")
	#htmltext = browser.open("https://www.google.com/search?tbm=isch&q=cat")
	#htmltext = browser.open("https://www.google.com/search?q=fish&tbm=isch")
	htmltext = browser.open("https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=1414&bih=709&q=cars&oq=cars")
	img_urls = []
	formatted_images = []
	print htmltext
	soup = BeautifulSoup(htmltext)
	results = soup.findAll("a")
	print results

	for r in results:
	    try:
	        print r
		print " "
	        if "imgres?imgurl" in r['href']:
		     img_urls.append(r['href'])
            except:
	        a=0

        print "img_urls ", len(img_urls)
        for im in img_urls:
	    refer_url = urlparse(str(im))
	    image_f = refer_url.query.split("&")[0].replace("imageurl","")
	    formatted_images.append(image_f)
	    print im


def train(names):
    training_data = ClassificationData(private=True, data_type='image', name='fish')

    inputs = []
    for name in names:
        urls = fetch(name)
        for url in urls:
            inputs.append((url, name))

    training_data.add_samples(inputs, input_type='urls')
    classifier = ClassificationModel(private=True, name='fish')
    classifier.fit(training_data)



if __name__ == "__main__":
    train(["striper", "bluefish", "weakfish", "bluefin"])
