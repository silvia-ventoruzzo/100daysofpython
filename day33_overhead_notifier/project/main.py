import requests
from datetime import datetime
import tkinter
from tkinter import messagebox
from time import sleep

MY_LAT = 41.385063 # Your latitude
MY_LONG = 2.173404 # Your longitude

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def iss_overhead(lat, long):
    #Your position is within +5 or -5 degrees of the ISS position.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if lat-5 <= iss_latitude <= lat+5 and long-5 <= iss_longitude <= long+5:
        return True
    else:
        return False
    
def is_dark(lat, long):
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", 
                            params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = datetime.strptime(data['results']['sunrise'],'%Y-%m-%dT%H:%M:%S%z')
    sunset = datetime.strptime(data['results']['sunset'],'%Y-%m-%dT%H:%M:%S%z')

    time_now = datetime.now(tz=sunrise.tzinfo)
    
    if sunset <= time_now <= sunrise:
        return True
    else:
        return False
    
window = tkinter.Tk()

while True:
    sleep(60)
    if iss_overhead(MY_LAT, MY_LONG) and is_dark(MY_LAT, MY_LONG):
        # Showing messagebox instead of email because emails isn't working
        messagebox.showinfo(title="ISS close by", message="Look up to see the ISS.")

window.mainloop()