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
set text="test_text_here, change content in send_text.txt"

echo.
echo The Text To Send :
set /p Build=<send_text.txt
echo %Build%
set text="%Build%"
 
echo.
pause

adb shell am start -a android.intent.action.VIEW -d 'https://wa.me/%my_no%' com.whatsapp
TIMEOUT 2

adb shell "input text '%text%'"
 
adb shell input keyevent 61
adb shell input keyevent 61
::adb shell input keyevent 61
adb shell input keyevent 66

for /F "delims=" %%a in (number_list.txt) do (

	TIMEOUT 2
    echo Messaging %%a
	adb shell am start -a android.intent.action.VIEW -d 'https://wa.me/%%a' com.whatsapp
	TIMEOUT 2
	
	adb shell "input text '%text%'"
	
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