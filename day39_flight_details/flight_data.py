class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)