#Import Required Libraries
from selenium import webdriver
import time
import sys


#Set The Webdriver & Host To Open
driver = webdriver.Chrome("C:/chromedriver.exe")       #'chromedriver.exe' Of Your Chrome Version Must Placed In The Specific Path Mentioned
driver.get('https://web.whatsapp.com/')


#Initializing Used/Global Variables
name = "~"       #Wha Info For Storing Target Name
msg = "~"        #Wha Info For The Msg To Send
count = 0       #Wha Info For No. Of Loops
inp = 0         #To Store Usr Input In Menu


#Begin Text Spam Loop
def start():
    print("\nPress 'CTR+C' To Break The Loop...")       #A Lil Info To Break The Loop, Not Perfect As It Terminates The Program

    for i in range(count):
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')   #Finds Msg Box (Still Confused By The Xpath Name)
        msg_box.send_keys(msg)                                                                      #Selectes & Enters The Text Info Msg Box
        button = driver.find_element_by_class_name('_1U1xa')                                        #Finds Enter Key WIth Class Name
        button.click()                                                                              #Clicks Enter Key


#Selects Entered Target's Name
def tar():
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))   #Finds Target's Name
    user.click()                                                                #Clicks On Targets Name


#First Time Entry
def firsttime():
    name = input('\nEnter Group/Target Name : ')   #Collects Target Name
    tar()                                          #Searchs for Target
    msg = input('Text To Send : ')                 #Gets Text Field
    count = int(input('No. Of count : '))          #Gets No. Of Loop


#*Display The Menu OF The Program
def menu():
    global name    #Imported Global Variable
    global msg     #Imported Global Variable
    global count   #Imported Global Variable
    global inp     #Imported Global Variable

    print("\n1. Change Target ( : " + name + ")")            #To Change/Display Target Name
    print("2. Change Text ( : "     + msg + ")")             #To Change/Display Text Msg Field
    print("3. Change Count ( : "    + str(count) + ")")      #To Display Count No. (Converte To String Before Displaying)
    print("4. Start")                                       #Show Start
    print("5. Quit")                                        #Show Quit 


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
        start()                                         #Start The Program
    if inp == "5":     
        driver.close()                                  #Close Browser Window
        quit()                                          #Quit Program


while True:
    menu()                #Call Menu Func
    inp = input("> ")     #Collect Usr Inp For Menu
    do()                  #Do Condition


    #text from txt files,
    #loop stop at any point without crashing
    #send imgs, mp3, video (media)
    #show percentage and count no.
    #ability to auto respond to chat
    #auto list available targets to select from
    #Convert Into Executable & Addd Gui