import time
import pandas as pd
import pywhatkit
import pyautogui
from pynput.keyboard import Key , Controller

keyboard = Controller()
def send_whatsapp_message(msg: str, phone_numbers: list):
    try:
        for phone_no in phone_numbers:
            pywhatkit.sendwhatmsg_instantly(
                phone_no=phone_no,
                message=msg,
                ##close whatsappTabs
                tab_close=True
            )
            ##time.sleep(1)
            ##pyautogui.click()
            time.sleep(1)
            ##keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            keyboard.press(Key.esc)
            print(f"Message sent to {phone_no}!")
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    # List of phone numbers of your customers
    with open('list.py') as f:
        lines = [line.rstrip('\n') for line in f]        
    message = "Whatsapp Toplu mesaj Listesi..."
    send_whatsapp_message(msg=message, phone_numbers=lines)

