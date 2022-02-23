import datetime as dt
import smtplib
import random

with open("quotes.txt") as file:
    quotes = file.readlines()

now = dt.datetime.now()
random_quote = random.choice(quotes)

if now.weekday() == 1:
    my_email = "tpython212@gmail.com"
    password = "arribamuchachos"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="lfalcaolopes@gmail.com",
                            msg=f"Subject:Your motivational message\n\n{random_quote}"
                            )
