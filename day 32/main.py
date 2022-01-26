import smtplib
import datetime
from random import choice

quotes = []
date = datetime.datetime.now()
today = date.weekday()

with open("quotes.txt", "r") as quotes_file:
    quotes = quotes_file.readlines()

quotes = [quote.strip("\n") for quote in quotes]
random_quote = choice(quotes)

email = "javiercrack351@gmail.com"
password = "asdadada3v423v"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="hello@gmail.com",
                        msg=f"Subject:Today's quote\n\n{random_quote}")
