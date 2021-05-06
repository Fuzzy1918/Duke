import numpy as np
from gensim.models import Word2Vec
import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk
import os
import random as rd

def time():
    from datetime import datetime

    now = datetime.now()
    hours = now.strftime("%H")
    hours = int(hours)
    minutes = now.strftime("%M")

    if (hours - 12 > 0): 
        real_h = hours - 12
        real_h = str(real_h)
        time = "PM" 
    else:
            time = "AM"
            real_h = str(hours)

    current_time = (real_h + ":" + minutes + ' ' + time)
    print("Current Time =", current_time)
    return current_time

def date():
    from datetime import date

    today = date.today()

    d2 = today.strftime("%B %d %Y")
    print(d2)
    return d2
    
def temperature():    
    # importing requests and json
    import requests
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "01970"
    API_KEY = "349c8c17598c5154250288cdf4d57c88"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       # getting the main dict block
       main = data['main']
       # getting temperature
       temperature = main['temp']
       # getting the humidity
       humidity = main['humidity']
       # getting the pressure
       pressure = main['pressure']
       # weather report
       report = data['weather']
       print(f"{CITY:-^30}")
       print(f"Temperature: {temperature}")
       print(f"Humidity: {humidity}")
       print(f"Pressure: {pressure}")
       print(f"Weather Report: {report[0]['description']}")
       temperature = (temperature - 273)*9/5 + 32
       temperature = "{:.1f}".format(temperature)
       return temperature
    else:
        # showing the error message
        print("Error in the HTTP request")
        
def climate():
    # importing requests and json
    import requests
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "01970"
    API_KEY = "349c8c17598c5154250288cdf4d57c88"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       # getting the main dict block
       main = data['main']
       # getting temperature
       temperature = main['temp']
       # getting the humidity
       humidity = main['humidity']
       # getting the pressure
       pressure = main['pressure']
       # weather report
       report = data['weather']
       print(f"{CITY:-^30}")
       print(f"Temperature: {temperature}")
       print(f"Humidity: {humidity}")
       print(f"Pressure: {pressure}")
       print(f"Weather Report: {report[0]['description']}")
       cool = report[0]['description']
       return str(cool)
    else:
        # showing the error message
        print("Error in the HTTP request")  
        
class NeuralNetwork():
    
    def __init__(self):
        # Seed the random number generator
        np.random.seed(69)
        #definding input for NN as well as range of outputs
        self.synaptic_weights = 2 * np.random.random((4, 1)) - 1

    def sigmoid(self, x):
       #custome sigmoid function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        #deravitive of sigmoid function for weight adjustments 
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
     
        for i in range(training_iterations):
            # Pass training set through the neural network
            output = self.predict(training_inputs)

            # Calculate the error rate
            error = training_outputs - output

            # Multiply error by input and gradient of the sigmoid function
            # Less confident weights are adjusted more through the nature of the function
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            # Adjust synaptic weights
            self.synaptic_weights += adjustments

    def predict(self, inputs):

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

def convert(lst): 
    return (lst.split()) 
    import speech_recognition as sr
    #take microphone input and prints recognized output
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
#recognized words is saved as sentence 
            sentence = recognizer.recognize_google(audio)
            h =  convert(sentence)
            print(h) 
            return h
        except sr.UnknownValueError:
                print("Could not understand audio")
                print(sentence.lower())       

def speech_recognition():
    #prediction word used for the model
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        print("Stay Silent...")
        recognizer.adjust_for_ambient_noise(source)
        print("Say your command")
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
#recognized words is saved as sentence 
            sentence = recognizer.recognize_google(audio)
            sentence = sentence.lower()
            h =  convert(sentence)
            print(h) 
            return h
        except sr.UnknownValueError:
                print("Could not understand audio")
                return ['nothing']
    
def main(h, neural_network_weather, neural_network_date, neural_network_time):

    
    weather_sum = 0.0
    date_sum = 0.0
    time_sum = 0.0
    game_sum = 0.0
    joke_sum = 0.0
    idk_sum = 0.0
    game_whitelist = [0]
    joke_whitelist = [0]
    time_whitelist = [0]
    date_whitelist = [0]
    weather_whitelist = [0]
    idk_whitelist = [0]
    loops = 0           
    i = 0  
    
    while (i < len(h)):
        element = h[i]
        if (element == 'time'):
            {
                time_whitelist.append(1000)
            }
        if (element == 'game'):
            {
                game_whitelist.append(1000)
            }
        if (element == 'joke'):
            {
                joke_whitelist.append(1000)
            }
        if (element == 'weather'):
            {
                weather_whitelist.append(1000)
            }
        if (element == 'date'):
            {
                date_whitelist.append(1000)
            }
        if (element == 'nothing'):
            {
               idk_whitelist.append(1000)
            }
        i += 1
        Array = Word2Vec.load("C:\\Users\\19787\\Desktop\\Duke\\model1").wv.__getitem__(element)
        
    
        weather_pred = neural_network_weather.predict(np.array([Array])) 
        date_pred = neural_network_date.predict(np.array([Array]))
        time_pred = neural_network_time.predict(np.array([Array]))
        
    
        if(weather_pred > 0.5):
    
         weather_sum += weather_pred
        else:
             weather_sum = weather_sum - weather_pred
        if(date_pred > 0.5):
            
         date_sum += date_pred
        else: 
            date_sum = date_sum - date_pred
        if(time_pred > 0.5):
            
         time_sum += time_pred
        else:
             time_sum = time_sum - time_pred
             
        loops += 1  
            
    
    weather_sum += weather_whitelist[-1]
    date_sum += date_whitelist[-1]
    time_sum += time_whitelist[-1]
    game_sum += game_whitelist[-1]
    joke_sum += joke_whitelist[-1]
    idk_sum += idk_whitelist[-1]
    print(weather_sum)
    print(date_sum)
    print(time_sum)
    print(game_sum)
    print(joke_sum)
    sums = [weather_sum, date_sum, time_sum, game_sum, joke_sum, idk_sum]
    return sums

def set_button(root, Frame, bg, text):
    listen_text = tk.StringVar()
    listen_btn = tk.Button(root, textvariable = listen_text, command=lambda:print("nope"), font = 'Raleway', bg = bg, activebackground="red",  fg = 'black', height = 4, width = 30)
    listen_text.set(text)
    listen_btn.grid(columnspan = 2, rowspan = 2, column = 1, row = 3)
    
    root.update()
     
def set_image_bg(root, Frame, bg):
    image = Frame(root, height= 350, width = 400,  bg=bg)
    image.grid(columnspan = 2, rowspan = 3, column = 3, row = 0)
    root.update()
    
def image_open(url):
    
    img = Image.open(url)
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(image = img)
    img_label.image = img
    img_label.grid(columnspan = 2, rowspan = 3, column = 3, row = 0)  

def game(results):
    image_open('C:/Users/19787/Desktop/Duke/images/game1.png')
    os.startfile("C:/Program Files (x86)/Minecraft Launcher/MinecraftLauncher.exe")
    results.append('Duke: Launching game')
    results.append('Launching game' )

def joke(results):
    jokebank = ['Why do we tell actors to break a leg? Because every play has a cast.', 
                'Hear about the new restaurant called karma? There is no menu you get what you deserve',
                'I invented a new word! Plagiarism']
    image_open('C:/Users/19787/Desktop/Duke/images/joke1.png')
    rand = rd.randint(0,2)
    results.append('Duke: '+ jokebank[rand])
    results.append(jokebank[rand])
    
def weather(results, temperature, c):
    image_open('C:/Users/19787/Desktop/Duke/images/weather1.png')
    results.append('Duke: The Weather is ' + c + ' and '+ temperature + 'F')
    results.append('The Weather is' + c + 'and' + temperature + ' degrees fahrenheit' )
    
def date_give(date, results):
    image_open('C:/Users/19787/Desktop/Duke/images/date1.png')
    results.append('Duke: the date is ' + date)
    results.append('The date is ' + date)
    
def time_give(time, results):
    image_open('C:/Users/19787/Desktop/Duke/images/time1.png')
    results.append('Duke: the current time is ' + time)
    results.append('The current time is ' + time)
    
def rejected(results):
    results.append("Duke: I didn't understand that")
    results.append("I didn't understand that")
