import requests
from bs4 import BeautifulSoup
import pandas

base_url="http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"
r=requests.get(base_url)
c=r.content
soup=BeautifulSoup(c, "html.parser")
page_nr=soup.find_all("a",{"class":"Page"})
last_page=page_nr[-1].text


for page in range(0,int(last_page)*10,10):
    url=base_url+"t=0&s="+str(page)+".html"

    r=requests.get(url)
    c=r.content
    soup=BeautifulSoup(c, "html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})

    l=[]
    for a in all:
        d={}
        price=a.find_all("h4", {"class": "propPrice"})
        d["Price"]=price[0].text.replace('\n','').replace(' ','')

        address=a.find_all("span", {"class": "propAddressCollapse"})
        d["Address"]=address[0].text+' '+address[1].text

        beds=a.find("span", {"class": "infoBed"})
        try:
            d["Beds"]=beds.find("b").text
        except:
            d["Beds"]="None"

        sqft=a.find("span", {"class": "infoSqFt"})
        try:
            d["Area"]=sqft.find("b").text
        except:
            d["Area"]="None"

        full_bath=a.find("span", {"class": "infoValueFullBath"})
        try:
            d["FullBaths"]=full_bath.find("b").text
        except:
            d["FullBaths"]="None"

        half_bath=a.find("span", {"class": "infoValueHalfBath"})
        try:
            d["HalfBaths"]=half_bath.find("b").text
        except:
            d["HalfBaths"]="None"


        for column_group in a.find_all("div", {"class": "columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class", "featureGroup"}), column_group.find_all("span", {"class":"featureName"})):

                if "Lot Size" in feature_group.text:

                    d["LotSize"]=feature_name.text
                else:
                    d["LotSize"]="None"

        l.append(d)

        df=pandas.DataFrame(l)
        print(df)
