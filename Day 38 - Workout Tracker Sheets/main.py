from nutrition import Nutrition
from sheety import Sheety

nutri = Nutrition()
sheets = Sheety()

entry = input("What was your workout today?\n")

workout = nutri.info(entry)

for exercises in workout:
    sheets.update_sheet(exercise=exercises["name"], duration=exercises["duration_min"], calories=exercises["nf_calories"])

