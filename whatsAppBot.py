import pyautogui
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsapp_responses import response
# Mouse click for this mf
mouse = Controller()

class WhatsApp:

    # monda
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    # Navigate to the green screen
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_dot.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Execption (nav_green_dot)', e)

    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paper_clip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Execption (nav_input_box)', e)


    def nav_message(self):
        try:
            position = pt.locateOnScreen('paper_clip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(30, -65, duration=self.speed)
        except Exception as e:
            print('Execption (nav_green_dot)', e)

    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(20,-210, duration=self.speed)
        mouse.click(Button.left, 1)
        sleep(1)
        self.message = pc.paste()
        print('User says:', self.message)

    def send_message(self):
        try:
            if self.message != self.last_message:
                bot_response = response(self.message)
                print('you say:',bot_response)
                pt.typewrite(bot_response,interval=.1)
                pt.typewrite('\n') #Sends message disable if messages get sended
                self.last_message = self.message
            else:
                print('No new messages...')
        except Exception as e:
            print('Exeption in send_message: ',e)


wa_bot = WhatsApp(speed=.5, click_speed=.5)
print("llendo a coldown")
sleep(2)
print("empieza")

while True:
    wa_bot.nav_green_dot()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()
    sleep(10)