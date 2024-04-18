import requests
from twilio.rest import Client
import math
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_EMAIL = "t3266694@gmail.com"
# MY_PASSWORD = "rlfvtcalegsowwqd"

# stock_market_api = "FWFAH69X9RJP2KPF"
news_api = "8ac1d77f3f7147418142ca7b1ac9c233"
# account_sid = "AC6b2273276f74ddf6f99e1308f0bf1395"
# auth_token = "86a81e9c52b711055d13c6cc446c8df4"

# stock_parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "apikey": stock_market_api
# }

# stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
# stock_response.raise_for_status()
# data = stock_response.json()
# nov_1_close_price = data["Time Series (Daily)"]["2023-11-01"]["4. close"]
# nov_2_close_price = data["Time Series (Daily)"]["2023-11-02"]["4. close"]
# diff = abs(float(nov_1_close_price) - float(nov_2_close_price))
# percent = (diff / float(nov_2_close_price)) * 100

percent = 6

if percent > 5: 
    news_parameters = {
        "q": COMPANY_NAME,
        "from": "2023-11-01",
        "to": "2023-11-02",
        "sortBy": "popularity",
        "apiKey": news_api,
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything",params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"][:3]
    for article in articles:
        
        headline = article["title"]
        brief = article["description"]
    
        # msg = f"TSLA: 🔺{math.floor(percent)}%\nHeadline: {headline}\nBrief: {brief}"
        
        msg = f"TSLA: 🔺{math.floor(percent)}%\nHeadline: {headline}\nBrief: {brief}"
        print(msg)
                
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(MY_EMAIL, MY_PASSWORD)
        #     connection.sendmail(
        #         from_addr=MY_EMAIL,
        #         to_addrs=MY_EMAIL,
        #         msg=f"Subjecy:Stock Update\n\n{msg}"
        #     )
                
    
    # client = Client(account_sid, auth_token)

    # message = client.messages \
    #                 .create(
    #                     body="It's going to rain today. Remember to bring an ☔️",
    #                     from_='+12015523801',
    #                     to='+491636095447'
    #                 )
    
    




# print(nov_2_close_price)

# between 2023-11-01 and 2023-11-02 there is an increase of 12.85 (5.88 %)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

