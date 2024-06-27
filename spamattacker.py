import pyautogui,keyboard,tine
from pyfiglet import Figlet
from colorama import Fore

title = Figlet(font="doom")
ascii = title.renderText("Spam Attack")
print(Fore.LIGHTGREEN_EX + ascii)

message = input("Enter the message you want to send: ")

delay = int(input("Interval in seconds between each message: "))

print("Press the Shift key to start the spam attack.")

while True:
    if keyboard.is_pressed("shift"):
        print("Spam attack started.")
        while True:
            pyautogui.typewrite(message)
            pyautogui.press("enter")
            time.sleep(delay)
