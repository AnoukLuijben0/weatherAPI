def get_weather_for_city(city):

    if city =="Rotterdam":
        # Added own logic
        return{"temperature": 10.0, "city": "Rotterdam"}
    else:
        return{"temperature": 20.0, "city": city}