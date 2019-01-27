from django.shortcuts import render
from django.http import HttpResponse
import speech_recognition as sr
import re
import datetime
# Create your views here.

# Record Audio

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

def parseVoice(voiceString):
	list = re.split("\s", voiceString)
	print (list[0])
	print (list[1])
	print (list[2])
	# now = datetime.datetime.now()
	list.append(datetime.datetime.now().strftime("%Y-%m-%d"))
	print (list[3])
	return list

class Item():
	def __init__(self, itemList):
		self.amount = int(itemList[0])
		self.name = itemList[1]
		self.price = float(itemList[2])
		self.date_Entered = itemList[3]

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    str = r.recognize_google(audio)
    testItem = Item(parseVoice(str))
    print("You said: " + str)
    print(testItem.amount, testItem.name, testItem.price)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


def home(request):
    return render(request, "Tracker/base.html")
