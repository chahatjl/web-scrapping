from bs4 import BeautifulSoup
import requests
from io import BytesIO
from PIL import Image
import os
def search():
  search = input("enter item to be searched")
  params = {"q": search}
  dir_name=search.replace(" ","_",).lower()
  if not os.path.isdir(dir_name):
      os.mkdir(dir_name)
  r = requests.get("https://www.bing.com/images/search",params=params)
  soup = BeautifulSoup(r.text,"html.parser")
  link = soup.findAll("a",{"class":"thumb"})
  for item in link:
      try:
          img_obj = requests.get(item.attrs["href"])
          print("getting",item .attrs["href"])
          title = item.attrs["href"].split("/")[-1]
          try:

              img = Image.open(BytesIO(img_obj.content))
              img.save("./" +dir_name+ "/"+title,img.format)
          except:
              print("could not found")
      except:
          print("could not request image")


search()


search()