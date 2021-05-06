import numpy as np
import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk
import Duke2 as Duke
import pyttsx3    
    
def start(root,listen_text,Frame, neural_network_weather, neural_network_date, neural_network_time, Global_display):
   #determining user input
   h = Duke.speech_recognition()
   #h = ['what', 'is', 'the', 'date']
   
   #displaying the user input   
   display = " "
   display = display.join(h)
   display = 'You: ' + display
   Global_display.append(display)
   
   text_box = tk.Text(root, height= 20, width = 50, padx =10, pady = 10)
   text_box.insert(1.0, display)
   text_box.grid(columnspan = 2, rowspan = 3, column = 1, row = 0)
   
   #calculating 
   sums = Duke.main(h, neural_network_weather, neural_network_date, neural_network_time)
   weather_sum = sums[0]
   date_sum = sums[1]
   time_sum = sums[2]
   game_sum = sums[3]
   joke_sum = sums[4]
   idk_sum = sums[5]
   print(weather_sum)
   print(date_sum)
   print(time_sum)
   print(game_sum)
   print(joke_sum)
   results = []
   x = ''
   Duke.set_image_bg(root, Frame, bg = "#33B5FF")
   
   temperature = str(Duke.temperature())
   climate = Duke.climate()
   date = Duke.date()
   time = Duke.time()
   
   
   if(weather_sum > date_sum and weather_sum > time_sum and weather_sum > game_sum and weather_sum > joke_sum and weather_sum > idk_sum and weather_sum > 0.5):
    
       Duke.weather(results, temperature, climate)
 

   if(date_sum > weather_sum and date_sum > time_sum and date_sum > game_sum and date_sum > joke_sum and date_sum > idk_sum and date_sum > 0.5):

       Duke.date_give(date, results)



   if(time_sum > weather_sum and time_sum > date_sum and time_sum > game_sum and time_sum > joke_sum and time_sum > idk_sum and time_sum > 0.5):

       Duke.time_give(time, results)
  
  
   if(game_sum > weather_sum and game_sum > date_sum and game_sum > time_sum and game_sum > joke_sum and game_sum > idk_sum and game_sum > 0.5):

       Duke.game(results)
   

   if(joke_sum > weather_sum and joke_sum > date_sum and joke_sum > time_sum and joke_sum > game_sum and joke_sum > idk_sum and joke_sum > 0.5):
       
       Duke.joke(results)
       
   if(idk_sum > weather_sum and idk_sum > date_sum and idk_sum > time_sum and idk_sum > game_sum and idk_sum > joke_sum and idk_sum > 0.5):
       {
        Duke.rejected(results)
        }

   
   print(results)         
   x = x.join(results[0])
   display = display + '\n' + x
   
   Global_display.append(display)
   
   text_box = tk.Text(root, height= 20, width = 50, padx =10, pady = 10)
   text_box.insert(1.0,display)
   text_box.grid(columnspan = 2, rowspan = 3, column = 1, row = 0)
   
   listen_text = tk.StringVar()
   listen_btn = tk.Button(root, textvariable = listen_text, command=lambda:prep(root,listen_text,Frame,neural_network_weather, neural_network_date, neural_network_time, Global_display), font = 'Raleway', bg = '#33B5FF', activebackground="red",  fg = 'black', height = 4, width = 30)
   listen_text.set("Click Me")
   listen_btn.grid(columnspan = 2, rowspan = 2, column = 1, row = 3)
   
   root.update()
   engine = pyttsx3.init()
   engine.say(results[1])
   engine.runAndWait()

def prep(root,listen_text,Frame, neural_network_weather, neural_network_date, neural_network_time, Global_display):
    Duke.set_image_bg(root, Frame, bg = "#be2040")
    Duke.set_button(root, Frame, bg = "#be2040",text = "Please Wait")
    
    root.update()
    start(root,listen_text,Frame, neural_network_weather, neural_network_date, neural_network_time, Global_display)    

def GUI(neural_network_weather, neural_network_date, neural_network_time, neural_network_game, neural_network_joke):   
    root = tk.Tk()
    root.title("Duke")

    canvas = tk.Canvas(root, width = 220, height = 400)
    canvas.grid(columnspan = 4, rowspan = 3)
    #33B5FF
    #behind image backdrop
    image = Frame(root, height= 350, width = 400,  bg="#33B5FF")
    image.grid(columnspan = 2, rowspan = 3, column = 3, row = 0)

    #logo
    logo = Image.open('C:/Users/19787/Desktop/Duke/Duke.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image = logo)
    logo.image = logo
    logo_label.grid(columnspan = 3, rowspan = 1, column = 3, row = 3)
    
    #textbox 
    text_box = tk.Text(root, height= 20, width = 50, padx =10, pady = 10)
    text_box.insert(1.0, 'Duke: Hello There!')
    text_box.grid(columnspan = 2, rowspan = 3, column = 1, row = 0)
    Global_display = []
    
    #button
    listen_text = tk.StringVar()
    listen_btn = tk.Button(root, textvariable = listen_text, command=lambda:prep(root,listen_text,Frame, neural_network_weather, neural_network_date, neural_network_time, Global_display), font = 'Raleway', bg = '#33B5FF', activebackground="red",  fg = 'black', height = 4, width = 30)
    listen_text.set("Click Me")
    listen_btn.grid(columnspan = 2, rowspan = 2, column = 1, row = 3)
    

    root.mainloop()
    
#Starts here!!!
#Wooooooooooooooooo   
 
# Initialize the neural networks
neural_network_weather = Duke.NeuralNetwork()
neural_network_date = Duke.NeuralNetwork()
neural_network_time = Duke.NeuralNetwork()
neural_network_game =  Duke.NeuralNetwork()
neural_network_joke =  Duke.NeuralNetwork()

training_inputs = np.array([[-0.03627917,0.10471522,-0.10026854,0.02875868],
                       [0.09668428,0.0538136,0.03402844,0.04554762],
                       [0.01395842,-0.00782125,-0.08180993,0.00389336],
                       [0.01395842,-0.00782125,-0.08180993,0.00389336],
                      [-0.08209962,0.16797704,-0.1086292,-0.07613142],
                      [-0.11225612,0.01542065,-0.0529591,-0.00025066],
                      [-0.00880101,-0.08572748,-0.08237889,0.01552423],
                      [0.11972316,0.02438944,0.07279091,0.12142652],
                      [0.12085818,0.12155448,0.12040057,-0.11162022],
                      [0.07069848,-0.0070207,-0.03462103,-0.16239952],
                      [-0.06209321,0.00553475,0.00353729,0.12363361],
                      [-0.00554066,-0.05375038,-0.00671253,-0.05054714],
                      [0.04562913,-0.00251329,0.05240403,0.08733993],
                      [-0.01105306,-0.08799928,0.05996143,0.10991833],
                      [-0.06909497,-0.00376274,-0.00750561,-0.06259944],
                      [0.03833304,-0.03537022,0.10527875,-0.14467834],
                      [0.03892542,1.3263664,0.3591809,-1.0351576]])

weather_outputs = np.array([[1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0]]).T

date_outputs = np.array([[0,1,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0]]).T

time_outputs = np.array([[0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,1,0]]).T

game_outputs = np.array([[0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0]]).T

joke_outputs = np.array([[0,1,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0]]).T

# Train the neural networks
neural_network_weather.train(training_inputs, weather_outputs, 10000)
neural_network_date.train(training_inputs, date_outputs, 10000)
neural_network_time.train(training_inputs, time_outputs, 10000)
neural_network_game.train(training_inputs, game_outputs, 10000)
neural_network_joke.train(training_inputs, joke_outputs, 10000)

print("\nSynaptic weights after training: ")
print("\nsynaptic weights for weather after training: ")
print(neural_network_weather.synaptic_weights)
print("\nsynaptic weights for date after training: ")
print(neural_network_date.synaptic_weights)
print("\nsynaptic weights for time after training: ")
print(neural_network_time.synaptic_weights)   
print("\nsynaptic weights for time after training: ")
print(neural_network_game.synaptic_weights) 
print("\nsynaptic weights for time after training: ")
print(neural_network_joke.synaptic_weights) 
    
GUI(neural_network_weather, neural_network_date, neural_network_time, neural_network_game, joke_outputs)
    
    
    
    
    
    
