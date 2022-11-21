import requests
from bs4 import BeautifulSoup
from urllib.request import unquote
import os

# Creating pdf Folder if don't exists
if not os.path.isdir("./pdf/"):
    os.makedirs("./pdf/")

# url = 'https://dyysg.org.uk/docs.php' # --> target URL
url = 'https://bmcbiol.biomedcentral.com/counter/pdf/10.1186/s12915-017-0385-3.pdf' # --> target URL

# make HTTP GET request to the target URL
response = requests.get(url)

content = BeautifulSoup(response.text, 'html.parser') # --> Parse content

anchor = content.find_all('a') # --> Achor tags

for link in anchor:
    try:
        if '.pdf' in link['href']: # pick up only those URLs containing 'pdf' within 'href' attribute
            pdf_url = ''
            if 'https' not in link['href']: # append base URL if no 'https' available in URL
                pdf_url = url + link['href']

            else: # otherwise use bare URL
                pdf_url = link['href']
            
            # make HTTP GET request to fetch PDF bytes
            print('Dowloading...: %s', pdf_url)          
            pdf_response = requests.get(pdf_url)
            
            # extract  PDF file name
            filename = unquote(pdf_response.url).split('/')[-1].replace(' ', '_')
            
            
            # write PDF to local file
            with open('./pdf/' + filename, 'wb') as f:
                f.write(pdf_response.content) # write PDF to local file
    
    except: # if error occurs in url
        pass
