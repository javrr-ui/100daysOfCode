import smtplib
import datetime
from random import choice

quotes = []
date = datetime.datetime.now()
today = date.weekday()

with open("quotes.txt", "r") as quotes_file:
    quotes = quotes_file.readlines()

quotes = [quote.strip("\n") for quote in quotes]

email = "javiercrack351@gmail.com"
password = "asdadada3v423v"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="hello@gmail.com", msg="Subject:Hello\n\nHello XD")
