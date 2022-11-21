import requests
from bs4 import BeautifulSoup

while True:
    url = input ("Enter the url of the website: ")
    # url = "https://github.com" -->  Example url of the website.
    try:
        r = requests.get(url)
        break
    except:
        print("Invalid url try again...")

htmlcontent = r.content # --> Get the content.


parsing = BeautifulSoup(htmlcontent, "html.parser") # --> Parse the Html(Beautify).

# Now finally scrape all the links available in the website.

anchors = parsing.find_all("a") # --> Return all anchor tags.
print("Collecting links...")

linksCollection = set()
for link in anchors:
    if link.get != "#":
        linksCollection.add(link.get("href"))

with open("links.txt",'w') as f:
    for items in linksCollection:
            if items.startswith("http"): # --> This block is only for external links not internal eg /contact
                f.write(f"{items}\n")
            else:
                f.write(f"{url}/{items}\n")

print("Succesful...")