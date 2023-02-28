@echo off

Title Whascript-adb by Jesvi Jonathan

@echo off
echo Whascript-adb by Jesvi Jonathan
echo.
echo Intended for bulk messaging
echo.
echo.
echo "Place the list of phone nunmbers in <number_list.txt>, each number being seperated line by line" 

echo "Place the text to be sent to the numbers in <send_text.txt>"
echo.
echo Make sure your android device has adb turned on and has your computer as a trusted device
echo.
@echo off

adb kill-server
adb devices

set my_no="7010493945"
::the above shit is a test number, just for test case...

::set text="test_text_here, change content in send_text.txt"

echo.
echo The Text To Send : from clipboard
echo.
::pause

::adb shell am start -a android.intent.action.VIEW -d 'https://wa.me/%my_no%' com.whatsapp.w4b
::TIMEOUT 2


for /F "delims=" %%a in (number_list.txt) do (

    echo Messaging %%a
	adb shell am start -a android.intent.action.VIEW -d 'https://wa.me/%%a' com.whatsapp.w4b
	::
	TIMEOUT 2
	
	adb shell "input text ''"
	
	adb shell input keyevent 279
	
	adb shell input keyevent 61
	::adb shell input keyevent 61
	adb shell input keyevent 61
	adb shell input keyevent 66	

)

TIMEOUT 2
echo.
echo.
echo Script has been successfully executed !
echo Whascript-adb By Jesvi Jonathan
pause