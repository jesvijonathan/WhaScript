# Wha-Script
# v0.01 | 11.Aug.2020
# By @JesviJonathan

#Import Required Libraries
from selenium import webdriver
import time
import sys


#Set The Webdriver & Host To Open
driver = webdriver.Chrome("C:/chromedriver.exe")       #'chromedriver.exe' Of Your Chrome Version Must Placed In The Specific Path Mentioned
driver.get('https://web.whatsapp.com/')


#Initializing Used/Global Variables
name = "~"       #Wha Info For Storing Target Name
msg = '~'        #Wha Info For The Msg To Send
count = 0        #Wha Info For No. Of Loops
inp = 0          #To Store Usr Input In Menus


#Check For Faults
def check():
    global inp

    if name == "~":
        print("\n! Target/Group Name Not Entered !")
        fl=1
    if msg == '~':
        print("\n! Spam Text Not Entered !")
        fl=1
    if fl == 1:
        time.sleep(3)
        inp = 0
    else:
        return 0


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
        driver.close()                                  #Close Browser Window
        print("\nProgramed By @JesviJonatham")          #Developer Credits
        quit()                                          #Quit Program


#First Time Entry, Get The User To Scan The QR Code
input('\nScan The QR Code & Press Enter ->')       #Wait For Usr To Respond


while True:
    print("\n\n----  What-Script  ----")    #Program Title
    menu()                  #Call Menu Func
    inp = input("\n> ")     #Collect Usr Inp For Menu
    do()                    #Do Condition
