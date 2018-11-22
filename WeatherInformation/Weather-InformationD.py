import requests
from time import sleep

ABSOLUTE_ZERO = 273
Choice = "Y"

api_Address = "http://api.openweathermap.org/data/2.5/weather?q="
api_ID = "&APPID=f9b5b60caa372024f1e419aa12803552"

def choiceCheck(Choice):
    if Choice!="Y" and Choice!="N":
        print("The choice entered is wrong.Try Again")
        print("---------------------------------------------------------------------")

while Choice != "N" :
    try:


            city_name = str(input("Enter the name of the city: "))
            url = api_Address + city_name +  api_ID
            jason_data = requests.get(url).json()
            weather_info = jason_data["weather"][0]["main"]
            humidity =  jason_data["main"]["humidity"]
            visibility = jason_data["visibility"]
            wind_speed = jason_data["wind"]["speed"]
            country_info =jason_data["sys"]["country"]
            temp_info = jason_data["main"]["temp"]
            temp_info = round(temp_info)

            sleep(1)
            print("-------------------------------------------------------------------------")
            print("Fetching data...")
            print("-------------------------------------------------------------------------")
            sleep(1)


            print("Country abbreviation: " + country_info)
            print("The current weather is: " + weather_info)
            print("The humidity is: " + str(humidity) + " %")
            print("The visibility is: " + str(visibility) + "m")
            print("The wind speed is: " + str(wind_speed) + " km/h")
            print("The temp is: " + str(temp_info - ABSOLUTE_ZERO) + " Degrees")

            print("-------------------------------------------------------------------------")
            Choice = input("Do you want to search for another city? Yes(Y)|No(N)")
            Choice = Choice.upper()
            print("-------------------------------------------------------------------------")
            choiceCheck(Choice)
    except:
             print("-------------------------------------------------------------------------")
             print("Either this city doesn´t exist or the program could not find the data.")
             print("-------------------------------------------------------------------------")
             Choice = input("Do you want to search for another city? Yes(Y)|No(N)")
             Choice = Choice.upper()
             print("-------------------------------------------------------------------------")
             choiceCheck(Choice)
else:
    print("-------------------------------------------------------------------------")
    print("I hope you liked the program :) Thanks")
    print("-------------------------------------------------------------------------")
