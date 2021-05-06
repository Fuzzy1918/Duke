# importing the module
import speech_recognition as sr
import gensim
from gensim.models import Word2Vec

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
    except sr.UnknownValueError:
        print("Could not understand audio")
    print(sentence.lower())
def convert(lst): 
    return (lst.split()) 

#sentence = "hour"

h =  convert(sentence)
print(h) 

model1 = Word2Vec.load("C:\\Users\\19787\\Desktop\\Duke\\model1")
better = [0]*10

def reload(ss, x):
    return (model1.wv.__getitem__(ss[x]))

data = model1.wv.__getitem__("is")

print(data)
