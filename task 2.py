from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/apple-iphone-14-blue-128-gb/p/itmdb77f40da6b6d?pid=MOBGHWFHSV7GUFWA&lid=LSTMOBGHWFHSV7GUFWA3AV8J8&marketplace=FLIPKART&q=apple+mobiles&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&fm=search-autosuggest&iid=fef359fd-df1c-4945-8a66-fe109edfa37a.MOBGHWFHSV7GUFWA.SEARCH&ppt=sp&ppn=sp&ssid=7ihea6644w0000001699848438959&qH=cb603b9543d774e1"

session = HTMLSession()
response = session.get(url)

response.html.render()

html = response.html.html

with open("flipkart_soup.html", "w", encoding="utf-8") as file:
    file.write(html)

soup = BeautifulSoup(html, 'html.parser')
title_device = soup.title.text
specifications_div = soup.find("div", class_="_5pFuey", string="Specifications")

if specifications_div:
    specifications_content = specifications_div.contents

    with open("specs.html", "w", encoding="utf-8") as file:
        for content in specifications_content:
            file.write(str(content))

    print("Specifications saved to specs.html")
else:
    print("Specifications not found.")