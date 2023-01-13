#Imports a module used for accessing API data and GUI library
import requests
import tkinter as tk

#This program gives the user weather info
#User enters location
#Weather data is printed 

#This function will get and verify a location entered by the user
def verifyLocation(root):

    #Gets the location from the user
    location = textfield.get()

    #Created connection with API
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+"2c8c9d4d3f1a476186105cc3d560ec87"
    api_link = requests.get(complete_api_link)
    #Stores API data into a var
    api_data = api_link.json()

                
    #if api_data['cod'] != '404':
    #    labelOne.config(text = "Not valid")

    weatherData(api_data)


#Function that prints weather data    
def weatherData(api_data):
    
   

    #gets values from api_data and converts them to C from Kelvins
    temp = int(((api_data['main']['temp']) - 273.15))
    cond = api_data['weather'][0]['main']
    feelsLike = int(((api_data['main']['feels_like']) - 273.150))
    weatherDesc = api_data['weather'][0]['description']
    windSpd = api_data['wind']['speed']
    pressure = api_data['main']['pressure']
    humidity = api_data['main']['humidity']

    labelOneData= cond+ "\n" + str(temp) + "°C" 
    labelTwoData = "\n" + "Feels like : " + str(feelsLike) + "°C" + "\n" + weatherDesc.capitalize() + "\n" + "Wind speed: " + str(windSpd) + " KM/H"+ "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " +  str(humidity) + "%" +"\n"


    labelOne.config(text = labelOneData)
    labelTwo.config(text = labelTwoData)



root = tk.Tk()
root.geometry("600x500")
root.title("Weather App")
root.configure(background='SlateGray1')

fontOne = ("poppins", 35, "bold")
fontTwo = ("poppins", 35, "bold")

textfield = tk.Entry(root,font = fontTwo)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', verifyLocation)

labelOne = tk.Label(root, font = fontTwo, bg = "SteelBlue3")
labelOne.pack(pady = 20)
labelTwo = tk.Label(root, font =  fontOne, bg = "SteelBlue3")
labelTwo.pack(pady = 20)
root.mainloop()





