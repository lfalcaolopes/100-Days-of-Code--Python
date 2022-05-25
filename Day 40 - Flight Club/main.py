from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_data import FlightData


data = DataManager()
alert_manager = NotificationManager()
flight_data = FlightData()
flight = FlightSearch()

if data.is_missing()["status"]:
    missing_cities = data.is_missing()["codes"]

    iata_codes = flight_data.get_iata(missing_cities)

    data.add_iata(iata_codes)

data.users_data()

if input("want to add an user? (Y/N): ").lower() == "y":
    data.get_user()

cities_list = data.airports()

start_date = input("A partir de quando você pode viajar? (dd/mm/aaaa)\n")
end_date = input("Até quando você pode viajar? (dd/mm/aaaa)\n")

tickets = flight.tickets(cities_list, start_date, end_date)
low_price_cities_info = []

for city, price in data.max_price().items():
    if price > tickets[city]["price"]:
        print(f"low price {city}")
        # alert_manager.send_message(tickets[city])

        low_price_cities_info.append(tickets[city])

alert_manager.send_email(low_price_cities_info, data.users_data())

