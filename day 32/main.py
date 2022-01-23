import smtplib

email = "javiercrack351@gmail.com"
password = "asdfsadfs"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email, password=password)
