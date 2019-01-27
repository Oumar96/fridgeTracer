from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import inside_Freeze
import speech_recognition as sr
import re
import datetime
# Create your views here.

# Record Audio

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

# def parseVoice(voiceString):
# 	list = re.split("\s", voiceString)
# 	print (list[0])
# 	print (list[1])
# 	print (list[2])
# 	# now = datetime.datetime.now()
# 	list.append(datetime.datetime.now().strftime("%Y-%m-%d"))
# 	print (list[3])
# 	return list

# class Item():
# 	def __init__(self, itemList):
# 		self.amount = int(itemList[0])
# 		self.name = itemList[1]
# 		self.price = float(itemList[2])
# 		self.date_Entered = itemList[3]

# # Speech recognition using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     str = r.recognize_google(audio)
#     testItem = Item(parseVoice(str))
#     print("You said: " + str)
#     print(testItem.amount, testItem.name, testItem.price)
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))


def home(request):
    return render(request, "Tracker/home.html")

def addItem(request):
    return render(request, "Tracker/addItem.html")

def removeItem(request):
    return render(request, "Tracker/removeItem.html")

def fridgeContent(request):
    context = {'contain_of_freeze': inside_Freeze.objects.all()}
    voice_value = request.GET.get('voice_value')

    for element in inside_Freeze.objects.all():
        if voice_value  == element.items:
            print(f'{voice_value} is {element.amount}')
        else:
            print(f'{voice_value} is not exist')

    return render(request, "Tracker/fridgeContent.html" ,context)

def addItem_submission(request):
    voice_value = request.GET.get('voice_value')
    print(voice_value)
    if voice_value :
        voice_values = voice_value.split(' ')
        print(voice_values)
        voice_values_in_db = inside_Freeze(amount=voice_values[0], items=voice_values[1], expire_date=voice_values[2])
        voice_values_in_db.save()

    return render(request, "Tracker/addItem.html")

