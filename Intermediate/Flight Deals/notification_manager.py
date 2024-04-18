import smtplib

class NotificationManager:
    def __init__(self):
        self.email = "t3266694@gmail.com"
        self.password = "rlfvtcalegsowwqd"

  
    def send_email(self, message, emails):
        
        for to_email in emails:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(self.email, self.password)
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=to_email,
                    msg=f"Subject:Flight Deal\n\n{message}"
                )
        