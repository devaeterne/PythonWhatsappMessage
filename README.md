# PythonWhatsappMessage
WhatsappMessageBot

## import library
time
pandas
pywhatkit
pyautogui
pynput.keyboard import Key , Controller


### Description
After installing the necessary libraries, you can update the contact list and start sending messages via WhatsApp.


If you, like every company, want to send messages to your customers via WhatsApp. You need a bulk whatsapp message for your potential customers.

- First Step
Let’s start by adding the necessary libraries…

```
import time`
import pandas as pd
import pywhatkit
import pyautogui
from pynput.keyboard import Key , Controller
```
**You must add controller**
```
keyboard = Controller()
```
  
**Now we can start writing our function**

```
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
```

When you run the code, your message will be automatically sent to all numbers in the
list.py file. It does not need to be saved on your phone.

The country codes of the numbers we will send messages to must be written between the “ “ symbols.