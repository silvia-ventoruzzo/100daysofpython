import datetime
from dateutil.relativedelta import relativedelta

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from day39_flight_details.data_manager import DataManager
from day39_flight_details.flight_search import FlightSearch
from day39_flight_details.notification_manager import NotificationManager

# Get data from Google Sheet
sheety_obj = DataManager()
search_obj = FlightSearch()
flight_data = sheety_obj.get_data()

# Get Iata Codes when missing
for i in flight_data.index[flight_data['iataCode'].isna()]:
    city_name = flight_data.loc[i, 'city']
    flight_data.loc[i, 'iataCode'] = search_obj.find_iata_code(city_name)

# Update Google Sheet with Iata Codes
sheety_obj.add_iata_code(flight_data['iataCode'])

# Create time period for round trip search
tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
in_six_months = (datetime.date.today() + relativedelta(months=6)).strftime('%d/%m/%Y')

# Search flights from Barcelona (result in Euro)
for index, row in flight_data.iterrows():
    flight_info = search_obj.get_cheap_flights(fly_from='BCN',
                                            fly_to=row['iataCode'],
                                            date_from=tomorrow,
                                            date_to=in_six_months,
                                            nights_in_dst_from=7,
                                            nights_in_dst_to=28,
                                            flight_type='round',
                                            one_for_city=1,
                                            curr='EUR',
                                            max_stopovers=0)
    
    try:
        if flight_info.price < row['lowestPrice']:
            NotificationManager().send_notification(fly_from_iata=flight_info.fly_from_iata, 
                                                fly_from_city=flight_info.fly_from_city,
                                                fly_to_iata=flight_info.fly_to_iata, 
                                                fly_to_city=flight_info.fly_to_city,
                                                price=flight_info.price, 
                                                out_date=flight_info.out_time.split("T")[0], 
                                                return_date=flight_info.return_time.split("T")[0])
    except AttributeError:
        pass
        


