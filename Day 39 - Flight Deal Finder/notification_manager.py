from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        # twilio_SID = "https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1"
        # twilio_token = "https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1"
        self.phone = +17853673661
        self.text = None

    def send_message(self, entry):
        client = Client(self.twilio_SID, self.twilio_token)

        self.text = f"Low price alert! Only R${entry['price']} to fly from {entry['cityFrom']}-{entry['airportFrom']}" \
                    f" to {entry['cityTo']}-{entry['airportTo']}, on {entry['date'].replace('-','/')}\n\n{entry['link']}"

        message = client.messages.create(
            body=self.text,
            from_='whatsapp:+14155238886',
            # to='whatsapp:+55********'
        )
