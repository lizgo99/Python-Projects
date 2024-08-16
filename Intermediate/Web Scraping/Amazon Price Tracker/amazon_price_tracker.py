from bs4 import BeautifulSoup
import requests
import pprint
import smtplib
from dotenv import load_dotenv
import os

static_url = "https://appbrewery.github.io/instant_pot"
live_url = "https://www.amazon.de/-/en/Samsung-Android-Storage-Contract-Graphite/dp/B0CMDFBB8M/?_encoding=UTF8&pd_rd_w=s1NUN&content-id=amzn1.sym.8fe76663-8bd5-436a-a3f4-39fc4cefbe79&pf_rd_p=8fe76663-8bd5-436a-a3f4-39fc4cefbe79&pf_rd_r=9BW0ST2J76RZ41NTXPMK&pd_rd_wg=q8FAe&pd_rd_r=a34e2bd2-7112-41ef-b287-a64ca8282b18&ref_=pd_hp_d_btf_tb_bs_d"


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(live_url, headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")
all_prices = soup.find_all(class_="a-offscreen")
price = float(soup.find(class_="a-offscreen").getText()[1:])
product = soup.find(name="span", id="productTitle").getText()
product = " ".join(product.split())
print(price)

load_dotenv()
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            msg = f"Subject:Amazon Price Alert!\n\n {product} is now ${price}".encode('utf-8')
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=msg
            )
