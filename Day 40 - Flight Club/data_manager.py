import requests


class DataManager:
    def __init__(self):
        self.get_url = "https://api.sheety.co/9d5acd285f7610595936ae718741743d/flightDeals/prices"
        self.get_users_url = "https://api.sheety.co/9d5acd285f7610595936ae718741743d/flightDeals/users"
        self.post_url = "https://api.sheety.co/9d5acd285f7610595936ae718741743d/flightDeals/users"

        self.header = {
            # "Authorization": "Bearer https://dashboard.sheety.co/#"
        }

        response = requests.get(self.get_url, headers=self.header)

        self.data = response.json()["prices"]

    def airports(self):
        airport_list = [item["iataCode"] for item in self.data]

        starting_point = self.data[0]["flyFrom"]

        output = {
            "airports": airport_list,
            "fly from": starting_point
        }

        return output

    def max_price(self):
        price = {item["iataCode"]: item["lowestPrice"] for item in self.data}

        return price

    def is_missing(self):
        self.cities = {item["city"]: item["id"] for item in self.data if item["iataCode"] == ""}

        if len(self.cities) > 0:
            status = True
        else:
            status = False

        output = {
            "codes": self.cities,
            "status": status
        }

        return output

    def add_iata(self, codes):
        counter = 0
        for key, value in self.cities.items():

            put_url = f"https://api.sheety.co/9d5acd285f7610595936ae718741743d/flightDeals/prices/{value}"

            entry = {
                "price": {
                    "iataCode": codes[counter]
                }
            }

            counter += 1

            requests.put(put_url, json=entry, headers=self.header)

    def get_user(self):
        f_name = input("First name: ")
        l_name = input("Last name: ")

        not_confirmed = True

        while not_confirmed:
            user_email = input("What is your email? : ")
            confirmation_email = input("Type your email again: ")

            if user_email == confirmation_email:
                not_confirmed = False

                users_input = {
                    "user": {
                        "firstName": f_name,
                        "lastName": l_name,
                        "email": user_email,
                    }
                }

                requests.post(self.post_url, json=users_input, headers=self.header)
                print("User confirmed.")
            else:
                print("Confirmation email doesn't match. Try again.")

    def users_data(self):
        response = requests.get(self.get_users_url, headers=self.header)
        data = response.json()["users"]

        f_names = [item["firstName"] for item in data]
        l_names = [item["lastName"] for item in data]
        emails = [item["email"] for item in data]

        output = {
            "firstName": f_names,
            "lastName": l_names,
            "email": emails,
        }

        return output
