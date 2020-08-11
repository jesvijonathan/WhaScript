# Wha-Script
# v0.01 | 11.Aug.2020
# By @JesviJonathan

#Import Required Libraries
from selenium import webdriver
import time
import sys


#Set The Webdriver & Host To Open
def invoke():
    try:
        driver = webdriver.Chrome("C:/chromedriver.exe")       #'chromedriver.exe' Of Your Chrome Version Must Placed In The Specific Path Mentioned
        driver.get('https://web.whatsapp.com/')
    except:
        input("Oops !, Something Wednt Wrong ! Press Enter To Try Again...")
        invoke()

#Initializing Used/Global Variables
version = 0.01   #Version Info
name = "~"       #Wha Info For Storing Target Name
msg = '~'        #Wha Info For The Msg To Send
count = 0        #Wha Info For No. Of Loops
inp = 0          #To Store Usr Input In Menus
fi = 0


#Check For Faults Before Start
def check():
    global inp
    global f1
    if name == "~":         #Check For Empty Name Variable
        print("\n! Target/Group Name Not Entered !")
        fl=1                #Turn Flag On
    elif msg == '~':          #Check For Empty Msg Variable
        print("\n! Spam Text Not Entered !")
        fl=1                #Turn Flag On
           #If Everything Good, Do Normal Code
    return 0


#Begin Text Spam Loop
def start():
    print("\nPress 'CTR+C' To Break The Loop...")       #A Lil Info To Break The Loop, Not Perfect As It Terminates The Program

    for i in range(count):
        b = str((i/count)*100) + "%" + " Complete... | (" + str(i) + "/" + str(count) + ")"
        print (b, end="\r")
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')   #Finds Msg Box (Still Confused By The Xpath Name)
        msg_box.send_keys(msg)                                                                      #Selectes & Enters The Text Info Msg Box
        button = driver.find_element_by_class_name('_1U1xa')                                        #Finds Enter Key WIth Class Name
        button.click()                                                                              #Clicks Enter Key


#Selects Entered Target's Name
def tar():
    global name
    try:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))   #Finds Target's Name
        user.click()                                                                #Clicks On Targets Name
    except:
        print("\n! No Such Name/Group/Target Found !")
        name = "~"
        time.sleep(3)


#*Display The Menu OF The Program
def menu():
    global name    #Imported Global Variable
    global msg     #Imported Global Variable
    global count   #Imported Global Variable
    global inp     #Imported Global Variable

    print("\n1. Group/Target Name ( : " + name + ")")            #To Change/Display Target Name
    print("2. Text Field ( : '"     + msg + "')")                #To Change/Display Text Msg Field
    print("3. Loop Count ( : "    + str(count) + ")")            #To Display Count No. (Converte To String Before Displaying)
    print("4. Start")                                            #Show Start
    print("5. Quit")                                             #Show Quit 


def do():
    global name    #Imported Global Variable
    global msg     #Imported Global Variable
    global count   #Imported Global Variable
    global inp     #Imported Global Variable
    
    if inp == "1":   
        name = input('\nEnter Group/Target Name : ')    #Get Target Name
        tar()
    if inp == "2":     
        msg = input('\nText To Send : ')                #Get Text Msg
    if inp == "3":      
        count = int(input('\nNo. Of count : '))         #Get No. Loop
    if inp == "4":
        if check() == 0:                                #Check Usr Field Before Start
            start()                                     #Start The Program
    if inp == "5":     
        try:
            driver.close()                              #Close Browser Window
        finally:
            print("\nWha-Script v{0} Programed By @JesviJonatham".format(version))      #Developer Credits
            quit()                                      #Quit Program


invoke()


#First Time Entry, Get The User To Scan The QR Code
input('\nScan The QR Code & Press Enter ->')       #Wait For Usr To Respond


while True:
    print("\n\n----  What-Script v{0}  ----".format(version))    #Program Title
    menu()                  #Call Menu Func
    inp = input("\n> ")     #Collect Usr Inp For Menu
    do()                    #Do Condition
