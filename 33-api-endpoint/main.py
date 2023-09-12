import requests
import datetime 
import time
import smtplib


MY_LAT = -6.221446
MY_LONG = 106.826248
FROM_EMAIL = ""
MY_EMAIL = ""
MY_PASSWORD = ""

# if night 
def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    sunrise_hour = response.json()['results']['sunrise'].split('T')[1].split(':')[0]
    sunset_hour = response.json()['results']['sunset'].split('T')[1].split(':')[0]
    print(sunrise_hour,sunset_hour)
    now = datetime.datetime.now()
    today_sunrise = now.replace(hour=sunrise_hour, minute=0, second=0, microsecond=0)
    today_sunset = now.replace(hour=sunset_hour, minute=0, second=0, microsecond=0)
    return now > today_sunset or now < today_sunrise

# in lat long radius
def is_iss_over():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_position = response.json()["iss_position"]
    print(iss_position)
    lat = iss_position["latitude"]
    long = iss_position["longitude"]

    return MY_LAT-5 <= lat <= MY_LAT+5 and MY_LONG-5 <= long <= MY_LONG+5 

isOn = True
while isOn:
    if is_night() and is_iss_over():
        #should use smtplib to sent the email
        with smtplib.SMTP("smtp.gmail.com") as connection: 
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Look Up!!!"
            )
        #debug
        print("Look Up!!!")
    time.Sleep(60)