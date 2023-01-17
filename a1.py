#Weather App
import requests
import tkinter as tk

#This program gives the user current weather info
#User enters location through gui prompt
#Weather data is shown through the gui

#This function will get and verify a location entered by the user
def verifyLocation(root):

    #Boolean var set false if location not found in API
    locationFound = True 

    #Gets the location from the user
    location = textfield.get()

    #Created connection with API
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+"2c8c9d4d3f1a476186105cc3d560ec87"
    api_link = requests.get(complete_api_link)

    #Stores API data into a json var
    api_data = api_link.json()

    #Confirms what the user has entered is a valid location within the api database          
    if api_data['cod'] == '404':
        labelOne.config(text = "Not a valid location")
        locationFound = False
        labelTwo.config(text = "")
        
    #Calls weatherData function which formats and displays the weather data 
    if locationFound:
        weatherData(api_data)


#Function that displays weather data to the gui   
def weatherData(api_data):
    
    #gets values from api_data 
    temp = int(((api_data['main']['temp']) - 273.15))
    feelsLike = int(((api_data['main']['feels_like']) - 273.150))
    weatherDesc = api_data['weather'][0]['description']
    windSpd = api_data['wind']['speed']
    pressure = api_data['main']['pressure']
    humidity = api_data['main']['humidity']

    #formats api data into strings and changes label text
    labelOneData= weatherDesc.capitalize()+ "\n" + str(temp) + "°C" 
    labelTwoData = "\n" + "Feels like : " + str(feelsLike) + "°C" + "\n"  + "Wind speed: " + str(windSpd) + " KM/H"+ "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " +  str(humidity) + "%" +"\n"
    labelOne.config(text = labelOneData)
    labelTwo.config(text = labelTwoData)


#Creates root
root = tk.Tk()
root.geometry("600x700")
root.title("Current Weather App")
root.configure(background='SlateGray1')

#Font type
fontOne = ("poppins", 25, "bold")
fontTwo = ("poppins", 35, "bold")

#Formats a text field for the user
textfield = tk.Entry(root,font = fontTwo)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', verifyLocation)

#Formats labels
labelOne = tk.Label(root, font = fontTwo, bg = "SteelBlue3")
labelOne.pack(pady = 20)
labelTwo = tk.Label(root, font =  fontOne, bg = "SteelBlue3")
labelTwo.pack(pady = 20)


#loops root
root.mainloop()
