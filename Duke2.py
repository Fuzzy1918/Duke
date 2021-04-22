import numpy as np
from gensim.models import Word2Vec


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

    
def weather():    
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
        print("Stay Silent...")
        recognizer.adjust_for_ambient_noise(source)
        print("Say your command")
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
        
 
def main(h):
    # Initialize the neural networks
    neural_network_weather = NeuralNetwork()
    neural_network_date = NeuralNetwork()
    neural_network_time = NeuralNetwork()

    #generates our random starting weights 
    print("Random starting synaptic weights: ")
    print(neural_network_weather.synaptic_weights)

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

    # Train the neural networks
    neural_network_weather.train(training_inputs, weather_outputs, 10000)
    neural_network_date.train(training_inputs, date_outputs, 10000)
    neural_network_time.train(training_inputs, time_outputs, 10000)

    print("\nSynaptic weights after training: ")
    print("\nsynaptic weights for weather after training: ")
    print(neural_network_weather.synaptic_weights)
    print("\nsynaptic weights for date after training: ")
    print(neural_network_date.synaptic_weights)
    print("\nsynaptic weights for time after training: ")
    print(neural_network_time.synaptic_weights)
    
    weather_sum = 0.0
    date_sum = 0.0
    time_sum = 0.0
    loops = 0           
    i = 0  
    
    while (i < len(h)):
        element = h[i]
        print(element)
        i += 1
        Array = Word2Vec.load("C:\\Users\\19787\\Desktop\\Duke\\model1").wv.__getitem__(element)
        print(Array)

    
       
        weather_pred = neural_network_weather.predict(np.array([Array])) 
        date_pred = neural_network_date.predict(np.array([Array]))
        time_pred = neural_network_time.predict(np.array([Array]))
         
        print("Word: ", h)
        print("Word array:", Array)
        print("\n Output data: ")
        print("\n Weather thinks?: ")
        print(weather_pred)
        print("\n Date thinks?: ")
        print(date_pred)
        print("\n Time thinks?: ")
        print(time_pred)
        print("\n")
    
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
        
       
       
        
    sums = [weather_sum, date_sum, time_sum]
    return sums   
    print(weather_sum)
    print(date_sum)
    print(time_sum)
 
    
    if(weather_sum > date_sum and weather_sum > time_sum and weather_sum > 0.5):
            {   
            weather():
            print("\n weather wins!\n")
            }
    else:
        if(date_sum > weather_sum and date_sum > time_sum and date_sum > 0.5):
                { 
                date():
                print("\n date wins!\n")
                }
        else:
            if(time_sum > weather_sum and time_sum > date_sum and time_sum > 0.5):
                {
                    time():
                    print("\n time wins!\n")
                }
            else:
                {
                    print('\n Nobody wins!')
                }

    
    
    
    