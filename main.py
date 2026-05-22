import pandas as pd
import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

time = dt.datetime.now()
birthday_dict = {}
all_letters = ["letter_1", "letter_2", "letter_3"]
day, month = time.day, time.month

reader = pd.read_csv('birthdays.csv')
dict_data = reader.to_dict(orient='records')
# print(dict_data)
for d in dict_data:
    # print(d['month'],d['day'])
    # birthday_dict ={(data_row["month"], data_row["day"]) : data_row for data_row in dict_data.iterrows}
    birthday_dict[(d["month"],d["day"])] = d["name"],d["email"],d["year"]

if (month, day) in birthday_dict:
    random_letter = random.choice(all_letters)
    with open(f'letter_templates/{random_letter}.txt','r') as birthday_letter:
        text = birthday_letter.read()
        replace_letter = text.replace("[NAME]",birthday_dict[(month, day)][0])
        # print(replace_letter)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_dict[(month, day)][1],
                            msg=f"Subject:Birthday wishes!\n\n{replace_letter}")
# THIS PROJECT INCLUDES DICTIONARY COMPREHENSION, TUPLES, CSV, PANDAS,