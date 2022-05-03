#Imports a module used for accessing API data
import requests

#This program gives the user weather info
#User enters location
#User enters temp scale they want to use 
#Weather data is printed 
#User is asked if they want to try again with a different location


#This function will get and verify a location entered by the user
def verifyLocation(question):

    #Loop that will continue until valid location entered
    while True:

        #Gets the location from the user
        location = input(question)

    
        #Created connection with API
        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+"2c8c9d4d3f1a476186105cc3d560ec87"
        api_link = requests.get(complete_api_link)
        #Stores API data into a var
        api_data = api_link.json()

        #If location is valid break from infinite loop
        if api_data['cod'] != '404':
            break
        print("")
        print("Not a valid location")

    #returns API Data          
    return api_data

#Function that gets whether user wants to use C or F    
def getTempScale(question):

    #initializes x to blank str
    x = ""

    #While loop that continues unless user input  = C or = F
    while x!= "C" or "F":

        #Gets input from user
        x = input(question)
   
        #If statements stating what to return 
        if x == ("C"):
            return True

        elif x == ("F") :
            return False 

#Function that prints weather data    
def weatherData(api_data, inCelsius):
    
    #If temp scale is in C 
    if inCelsius == True:

        #gets values from api_data and converts them to C from Kelvins
        temp = ((api_data['main']['temp']) - 273.15)
        feelsLike = ((api_data['main']['feels_like']) - 273.150)
        #prints values
        print  ("Current temperature is: ",temp," deg C")
        print  ("Feels Like: ",feelsLike," deg C")
        
    # If temp scale is in F
    else:

        #gets values from api_data and converts them to F from Kelvins
        temp = ((api_data['main']['temp']) - 273.15) * 9/5 + 32
        feelsLike = ((api_data['main']['feels_like']) - 273.150)* 9/5 + 32
        #prints values
        print ("Current temperature is: ",temp," deg F")
        print  ("Feels Like: ",feelsLike," deg F")

    #gets values from api_data
    weatherDesc = api_data['weather'][0]['description']
    windSpd = api_data['wind']['speed']

    #prints values
    print ("Weather description  :",weatherDesc)
    print ("Wind speed    :",windSpd ,'kmph') 
    print ("")     

#Function that asks the user if they want to try again
def askUserToTryAgain(question):
    
    #initializes x to blank str
    x= ""

    #Loops until input = no or = yes
    while x!= "no" or "yes":   

        #Gets input from user
        x = input(question)

        #If statements that specify what to return
        if x == "no":
            return False 
        elif x == "yes":
            return True

#Prints title of program
print("*** WEATHER APP ***")
print("")

#Loop that runs program until user stops
while True: 
    #Storig API data with return value from function
    api_data= verifyLocation("What is the location you want to know the weather of? ")
    print("")

    #Storig temp scale with return value from function
    inCelsius = getTempScale("Do you want the temp to be in Celsius or Fahrenheit? (Enter C or F) ")
    print("")

    #Prints weather data 
    weatherData(api_data,inCelsius )

    #Stores whether user wants to try again with return value from function
    tryAgain = askUserToTryAgain("Would you like to get the weather info of another location? (Enter yes or no) ")

    #If the user doesn't want to try again then if statement breaks 
    if tryAgain == False:
        break 

#End screen messaage
print("")
print("Thanks for using the weather app")