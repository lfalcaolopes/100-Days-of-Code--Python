import datetime as dt
import smtplib
import pandas
from random import choice

my_email = "tpython212@gmail.com"
password = "ar***********s"

now = dt.datetime.now()
birthdays = pandas.read_csv("birthdays.csv")
birth_data = birthdays.to_dict()

with open("letter_templates/letter_1.txt") as file:
    letter_1 = file.read()

with open("letter_templates/letter_2.txt") as file:
    letter_2 = file.read()

with open("letter_templates/letter_3.txt") as file:
    letter_3 = file.read()

letters = [letter_1, letter_2, letter_3]


for index in range(len(birth_data["name"])):
    if now.month == birth_data["month"][index] and now.day == birth_data["day"][index]:
        name = birth_data["name"][index]
        person_email = birth_data["email"][index]
        custom_letter = choice(letters).replace("[NAME]", name)

        print(custom_letter)
        print(birth_data["email"][index])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=person_email,
                                msg=f"Subject:Happy Birthday!!\n\n{custom_letter}"
                                )
