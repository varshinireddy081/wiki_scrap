import requests
from bs4 import BeautifulSoup
import sys

COUNT= 0
SCRAPPED_URL=[]

def scrapeWikiArticle(url):
    global COUNT
    global SCRAPPED_URL
    if url in SCRAPPED_URL:
        print("WE ALREADY SCRAPPED ",url)
    else:
        SCRAPPED_URL.append(url)
    if COUNT <= 0:
        print("Number of cycles achieved")
        exit()
    COUNT=COUNT-1

    response = requests.get(
        url=url,
    )
    print("Scrapping ",url)
    soup = BeautifulSoup(response.content, 'html.parser')


    all_links_in_page = soup.find(id="bodyContent").find_all("a")
    print("We found ", len(all_links_in_page)," from ", url)
    for link in all_links_in_page:
    # We are only interested in other wiki articles
        print("Processing",link['href'])

        if link['href'].find("/wiki/") !=-1:
            scrapeWikiArticle("https://en.wikipedia.org" + link['href'])
        else:
            print("NOT A WIKI LINK!!")



param_1= sys.argv[1]
param_2= sys.argv[2]

COUNT=int(param_2)
is_int = isinstance(COUNT, int)
if param_1.find("wikipedia.org") ==-1  :
    print("Sorry This is not a wikipedia link")
elif is_int==False :
    print("Please enter valid iterations")
else :
    print("Scraping ",param_1," Iterations ",COUNT)
    scrapeWikiArticle(param_1)