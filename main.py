from bs4 import BeautifulSoup
import requests
search=input("enter item to be serached")
params={"q":search}
r=requests.get("https://www.google.com/search",params=params)
soup=BeautifulSoup(r.text,"html.parser")
#print(soup.prettify())
result=soup.find("ol",{"id":"b_results"})
link=result.findAll("li",{"class":"b_algo"})

for item in link:
    item_text=item.find("a").text
    item_href=item.find("a").attrs["href"]
    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("summary",item.find("a").parent.parent.find("p").text)