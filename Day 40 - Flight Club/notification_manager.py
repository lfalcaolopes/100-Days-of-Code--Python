from twilio.rest import Client
import smtplib


class NotificationManager:
    def __init__(self):
        # self.twilio_SID = "https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1"
        # self.twilio_token = "https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1"
        self.phone = +17853673661
        self.final_message = ""

        # self.my_email = "tpy*******2@gmail.com"
        # self.password = "ar***********hos"

    def send_message(self, entry):
        client = Client(self.twilio_SID, self.twilio_token)

        self.text = f"Low price alert! Only R${entry['price']} to fly from {entry['cityFrom']}-{entry['airportFrom']}" \
                    f" to {entry['cityTo']}-{entry['airportTo']}, on {entry['date'].replace('-','/')}\n\n{entry['link']}"

        client.messages.create(
            body=self.text,
            from_='whatsapp:+14155238886',
            to='whatsapp:+557********6'
        )

    def send_email(self, tickets, users_data):
        for entry in tickets:
            text = f"Only R${entry['price']} to fly from {entry['cityFrom']}-{entry['airportFrom']} to " \
                   f"{entry['cityTo']}-{entry['airportTo']}, on {entry['date'].replace('-', '/')}\n\n{entry['link']}\n\n\n"

            self.final_message += text

        for user in range(len(users_data["firstName"])):
            with smtplib.SMTP("smtp.gmail.com") as connect:
                connect.starttls()
                connect.login(user=self.my_email, password=self.password)
                connect.sendmail(from_addr=self.my_email,
                                 to_addrs=users_data["email"][user],
                                 msg=f"Subject:Low price alert!\n\nLook what I got for you {users_data['firstName'][user]}"
                                     f" {users_data['lastName'][user]}!\n{self.final_message}".encode('utf-8')
                                 )
