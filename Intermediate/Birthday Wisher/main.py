import smtplib
import datetime as dt
from datetime import datetime
import random
import pandas

gmail_email = "t3266694@gmail.com"
yahoo_email = "t3266694@yahoo.com"
password = "rlfvtcalegsowwqd"

def email_motivation_quote():
    weekday = dt.datetime.now().weekday()
        
    if weekday == 6:
        with open("Intermediate/Birthday Wisher/quotes.txt", "r") as quotes:
            list_of_quotes = quotes.readlines()
            random_quote = random.choice(list_of_quotes)
        
        with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
            gmail_connection.starttls()
            gmail_connection.login(user=gmail_email, password=password)
            gmail_connection.sendmail(
                from_addr=gmail_email, 
                to_addrs=gmail_email, 
                msg=f"Subject:Monday Motivation\n\n{random_quote}.")

def email_birthay_wishes_my_version():
    
    now = dt.datetime.now()
    current_month = now.month
    current_day = now.day

    birthdays_data = pandas.read_csv("Intermediate/Birthday Wisher/birthdays.csv")


    for i in birthdays_data.index:
        month = birthdays_data["month"][i]
        day = birthdays_data["day"][i]
        if current_day == day and current_month == month:
            
            email = birthdays_data["email"][i]
            name = birthdays_data["name"][i]
            
            random_num = random.randint(1,3)
            
            with open(f"Intermediate/Birthday Wisher/letter_templates/letter_{random_num}.txt") as letter_file:
                text = letter_file.read()
                new_text = text.replace("[NAME]" , name)
            
            with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
                gmail_connection.starttls()
                gmail_connection.login(user=gmail_email, password=password)
                gmail_connection.sendmail(
                    from_addr=gmail_email, 
                    to_addrs=email, 
                    msg=f"Subject:Happy Birthday!\n\n{new_text}.")
                
def email_birthay_wishes_class_version(): 
    
    MY_EMAIL = "t3266694@gmail.com"
    MY_PASSWORD = "rlfvtcalegsowwqd"

    today = datetime.now()
    today_tuple = (today.month, today.day)

    data = pandas.read_csv("birthdays.csv")
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
    if today_tuple in birthdays_dict:
        birthday_person = birthdays_dict[today_tuple]
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )


# email_birthay_wishes_my_version() 
email_birthay_wishes_class_version()
