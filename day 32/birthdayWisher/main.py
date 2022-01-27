import pandas
import datetime
from random import randint
##################### Extra Hard Starting Project ######################
congratulations_list = []
data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
date = datetime.datetime.now()
month = date.month
day = date.day

for person in birthdays:
    if person["month"] == month and person["day"] == day:
        congratulations_list.append(person)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(congratulations_list) > 0:
    for person in congratulations_list:
        number = randint(1, 3)
        with open(f"letter_templates/letter_{number}.txt", "r") as letter_file:
            letter = letter_file.read()

# 4. Send the letter generated in step 3 to that person's email address.




