
import pyautogui as pg
import time

round = 18

while True:

    if(pg.locateOnScreen(lvl) != None):
        print('I see it!')
        time.sleep(.9)
    else: 
        round += 1
        print(round)
        lvl= pg.screenshot(region=(1442,1,118,69))
        # lvl.save('imag.png')
        time.sleep(.2)
        
    