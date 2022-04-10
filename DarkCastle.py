from BloonsMacro.macros import Monkey
from BloonsMacro.macros import startgame_Speed
from time import sleep
import pyautogui as pg
import threading


roundnum = 1

def start_level_tracking():
   
    global roundnum
    roundnum = 1
    print('Round: 1')
    
    lvl= pg.screenshot(region=(1442,1,118,69))
    # lvl.save('imag.png')
            
    while True:

        if(pg.locateOnScreen(lvl) != None):
            # print('I see it!')
            sleep(.9)
        else: 
            roundnum += 1
            print('Round: ' + str(roundnum))
            lvl= pg.screenshot(region=(1442,1,118,69))
            # lvl.save('imag.png')
            sleep(.2)   

def level():
    sub = Monkey(1104,396, 'sub')
    sauda = Monkey(526, 448, 'hero')
    dart = Monkey(735, 385 , 'dart')
    startgame_Speed()
    global roundnum
    while roundnum <= 4:
        if(roundnum == 4):
            # print('R4')
            sub.upgrade(3)
            sub.upgrade(1)
            break
    while roundnum <= 26:
        if(roundnum == 26):
            # print('R26')
            sub.upgrade(3)
            sub.upgrade(3)
            sub.upgrade(3)
            sub.upgrade(1)
            break
    while roundnum <= 29:
        if(roundnum == 29):
            cannon = Monkey(708,736, 'cannon')
            cannon.upgrade(3)
            cannon.upgrade(3)
            cannon.upgrade(2)
            break
    # while roundnum <= 44:
    #     if(roundnum == 44):
    #         pg.click(954, 911)
    #         sleep(.5)
    #         pg.click(701,857)
    #         sleep(4)
    #         pg.click(1817,941)
    #         sleep(.5)
    #         pg.click(1341, 977)
    #         sleep(.2)
    #         pg.click(1341, 977)
    #         sleep(.2)
    #         pg.click(955,253)
    #         b = threading.Thread(name='background', target=start_level_tracking)
    #         f = threading.Thread(name='foreground', target=level)

    #         b.start()
    #         f.start()

            



b = threading.Thread(name='background', target=start_level_tracking)
f = threading.Thread(name='foreground', target=level)

b.start()
f.start()
