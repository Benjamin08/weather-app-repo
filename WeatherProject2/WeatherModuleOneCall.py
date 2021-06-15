'''
Created on May 24, 2021

@author: Colby Bradley
'''
import requests
import tkinter as tk
import datetime as datetime

from tkinter import Button
from tkinter import Label
from tkinter.tix import ButtonBox
from Tools.scripts.combinerefs import read

url = 'https://api.openweathermap.org/data/2.5/onecall?lat=45.98&lon=-67.2189&exclude=,current,minutely,hourly&appid=5d2d76c89f948fe60bef22415ab8d870&units=metric'

res = requests.get(url)

data = res.json()

temp = data['daily'][0]['feels_like']['day']

#===============BUTTON CLICKED CODE========================

def testButtonClicked():
    print("method")
    
#=========================================================


#=============================OTHER DAYS CLASS=============================

class OtherDay:
    def _init_(self, xPos,yPos):
        self.dateLabel = tk.Label(window, text="the date",font=("Arial Bold",20))
        self.dateLabel.place(xPos,yPos)
        #self.dateLabel.config(text = unixTime)
        
    
#================================================================

#=====================SET CURRENT DAY============================
def SetCurrentDay():
    dateData = datetime.datetime.now()
    print(dateData.strftime("%A"))
    todaysDate = dateData.strftime("%A")
    todaysTemp = data["daily"][0]["temp"]["day"]
    todaysPOP = data["daily"][0]["pop"]
    todaysPOP = todaysPOP * 100
    todaysHumidity = data["daily"][0]["humidity"]
    currentDayLabel.config(text = todaysDate)
    currentDayTempLabel.config(text = "{:.1f}".format(todaysTemp) + " *C")
    currentDayPOPLabel.config(text = str(todaysPOP) + "% POP")
    currentDayHumidityLabel.config(text = str(todaysHumidity) + "% HUM")
#================================================================

#============================SET OTHER DAYS==============================

##def SetOtherDays():
    ##day0 = OtherDay(700,300)

#========================================================================





#=====================WINDOW CODE=================================
window = tk.Tk()

#to rename the title of a window
window.title("Homestead Weather System")

#resize our window when program starts
window.geometry('1250x1080')

                
#pack is used to show the object in the window
#label = tkinter.Label(window, text = "Hello Shay").pack()

#create a label a different way
firstLabel = tk.Label(window, text="Monday",font=("Arial Bold",20))

#add the label to the window
firstLabel.grid(column=0,row=0)

secondLabel = tk.Label(window, text="Tuesday",font=("Arial Bold",20))

secondLabel.grid(column=1,row=0)

thirdLabel = tk.Label(window, text="Wednesday",font=("Arial Bold",20))

thirdLabel.grid(column=2,row=0)

fourthLabel = tk.Label(window, text="Thursday",font=("Arial Bold",20))

fourthLabel.grid(column=3,row=0)

fifthLabel = tk.Label(window, text="Friday",font=("Arial Bold",20))

fifthLabel.grid(column=4,row=0)

sixthLabel = tk.Label(window, text="Saturday",font=("Arial Bold",20))

sixthLabel.grid(column=5,row=0)

seventhLabel = tk.Label(window, text="Sunday",font=("Arial Bold",20))

seventhLabel.grid(column=6,row=0)

currentDayLabel = tk.Label(window,text="Current Day",font=("Arial Bold", 50))

currentDayLabel.place(x=100,y=250)

currentDayTempLabel = tk.Label(window,text = "-99*C",font=("Arial Bold", 40))

currentDayTempLabel.place(x=200,y=350)

currentDayPOPLabel = tk.Label(window,text = "-1%",font=("Arial Bold", 40))

currentDayPOPLabel.place(x=200,y=420)

currentDayHumidityLabel = tk.Label(window,text = "-1%",font=("Arial Bold", 40))

currentDayHumidityLabel.place(x=200,y=500)

SetCurrentDay()
##SetOtherDays()

window.mainloop()
#================================================================


if __name__ == '__main__':
    pass