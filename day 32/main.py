import smtplib

email = "javiercrack351@gmail.com"
password = "asdadada3v423v"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs="hello@gmail.com", msg="Hello XD")
