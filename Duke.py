import tkinter as tk 
from PIL import Image, ImageTk
import Duke2 as Duke


def yeet():
   #determining user input
   listen_text.set("listening...")
   h = Duke.speech_recognition()
   listen_text.set("Recognizing....")
   
   #displaying the user input 
   display = " "
   display = display.join(h)
   display = 'You: ' + display
   text_box = tk.Text(root, height= 10, width = 50, padx = 15, pady = 15)
   text_box.insert(1.0, display)
   text_box.grid(column = 1, row = 3)
   
   #calculating 
   sums = Duke.main(h)
   weather_sum = sums[0]
   date_sum = sums[1]
   time_sum = sums[2]
   print(weather_sum)
   print(date_sum)
   print(time_sum)
   results = []
   x = ''
   
   if(weather_sum > date_sum and weather_sum > time_sum and weather_sum > 0.5):
            {   
                results.append('Duke: the weather is ' + str(Duke.weather()) + 'F')
            }
   else:
        if(date_sum > weather_sum and date_sum > time_sum and date_sum > 0.5):
                { 
                results.append('Duke: the date is ' + Duke.date())
                }
        else:
            if(time_sum > weather_sum and time_sum > date_sum and time_sum > 0.5):
                {
                
                    results.append('Duke: the current time is ' + Duke.time())
                }
            else:
                {
                    results.append("Duke: I didn't understand that")
                }
                
   x = x.join(results)
   display = display + '\n' + x
   text_box = tk.Text(root, height= 10, width = 50, padx = 15, pady = 15)
   text_box.insert(1.0, display)
   text_box.grid(column = 1, row = 3)
   listen_text.set("Click Me")
    
root = tk.Tk()
root.title("Duke")

canvas = tk.Canvas(root, width = 800, height = 400)
canvas.grid(columnspan = 3, rowspan = 3)

#logo
logo = Image.open('C:/Users/19787/Desktop/Duke/Duke_Logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column = 1, row = 0)

#instructions 
instructions = tk.Label(root, text="Press the button below for Duke to start listening", font = 'Raleway')
instructions.grid(columnspan = 3, column = 0, row =1)

#button
listen_text = tk.StringVar()
listen_btn = tk.Button(root, textvariable = listen_text, command=lambda:yeet(), font = 'Raleway', bg = '#20bebe', fg = 'black', height = 2, width = 15)
listen_text.set("Click Me")
listen_btn.grid(column = 1, row = 2)

canvas = tk.Canvas(root, width = 800, height = 250)
canvas.grid(columnspan = 3,)

#text_box
text_box = tk.Text(root, height= 10, width = 50, padx = 15, pady = 15)
text_box.insert(1.0, 'Duke: Hello There!')
text_box.grid(column = 1, row = 3)


root.mainloop()