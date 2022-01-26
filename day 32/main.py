import smtplib
import datetime

date = datetime.datetime.now()
today = date.weekday()


email = "javiercrack351@gmail.com"
password = "asdadada3v423v"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="hello@gmail.com", msg="Subject:Hello\n\nHello XD")
