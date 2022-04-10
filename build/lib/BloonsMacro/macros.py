#############################
# INFO
############################


# (First -> Last -> Close -> Strong (loop)



################
# STATICS
################

HERO = 1712,210


DART = 1839,225
BOOMER = 1712, 331
CANNON = 1855, 371
TACK = 1701,495
ICE = 1837, 489
GLUE = 1712, 617


SNIPER = 1827, 627
SUB = 1712, 769
BOAT = 1833, 753
ACE = 1712, 897
HELI = 1841, 903

################
# IMPORTS
################

import time

import pyautogui as pg


#################
# CLICK
#################

def click(x: int, y: int):
    (q,g) = pg.position()
    pg.click(x,y)
    pg.moveTo(q,g)


def drag(start_pos_x, start_pos_y, end_pos_x, end_pos_y, doclick = None):
    if(doclick == None):
        pg.moveTo(start_pos_x,start_pos_y)
    else: 
        click(start_pos_x,start_pos_y)
        pg.dragTo(end_pos_x,end_pos_y, duration=1)

class Monkey():

    def __init__(self, posx, posy, monktype, targeting=None):
        self.posx = posx 
        self.posy = posy
        self.monktype = monktype
        self.current_targeting = 'first'
        self.targeting = targeting
        self.place_monk()
        time.sleep(.5)
        if(targeting != None):
            self.set_targeting(self.targeting)


   


    def place_monk(self):
        if(self.monktype.lower() == 'dart'):
            self.buy_dart()
        elif(self.monktype.lower() == 'hero'):
            self.buy_hero()
        elif(self.monktype.lower() == 'tack'):
            self.buy_tack()
        elif(self.monktype.lower() == 'boomer'):
            self.buy_boomer()
        elif(self.monktype.lower() == 'cannon'):
            self.buy_cannon()
        elif(self.monktype.lower() == 'ice'):
            self.buy_ice()
        elif(self.monktype.lower() == 'glue'):
            self.buy_glue()
        elif(self.monktype.lower() == 'snipe'):
            self.buy_sniper()
        elif(self.monktype.lower() == 'sub'):
            self.buy_sub()
        elif(self.monktype.lower() == 'boat'):
            self.buy_boat()
        elif(self.monktype.lower() == 'ace'):
            self.buy_ace()
        elif(self.monktype.lower() == 'heli'):
            self.buy_heli()
        elif(self.monktype.lower() == 'mortar'):
            self.buy_mortar()
        elif(self.monktype.lower() == 'dartling'):
            self.buy_dartling()
        elif(self.monktype.lower() == 'wizard'):
            self.buy_wizard()
        elif(self.monktype.lower() == 'super'):
            self.buy_super()
        elif(self.monktype.lower() == 'ninja'):
            self.buy_ninja()
        elif(self.monktype.lower() == 'alch'):
            self.buy_alch()
        elif(self.monktype.lower() == 'druid'):
            self.buy_druid()
        elif(self.monktype.lower() == 'farm'):
            self.buy_farm()
        elif(self.monktype.lower() == 'sfactory'):
            self.buy_sfactory()
        elif(self.monktype.lower() == 'village'):
            self.buy_village()
        elif(self.monktype.lower() == 'engineer'):
            self.buy_engineer()
        else:
            print('Monkey Name Is Not Recognised Check For Spelling Errors!')
        time.sleep(.3)

        #click(self.posx,self.posy)

######################
# HERO
######################

    def buy_hero(self):
        click(HERO[0], HERO[1])
        time.sleep(.3)
        pg.moveTo(self.posx,self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        time.sleep(.4)
        print('Purchased Hero At (' + str(self.posx) + ', ' + str(self.posy) + ')')

#######################
# PRIMAIRY
#######################

    def buy_dart(self):
        click(DART[0],DART[1])
        time.sleep(.2)
        pg.moveTo(self.posx, self.posy)
        time.sleep(.2)
        click(self.posx, self.posy)
        time.sleep(.2)
        print('Purchased Dart Monkey At (' + str(self.posx) + ', ' + str(self.posy) + ')')
        

    def buy_boomer(self):
        click(BOOMER[0], BOOMER[1])
        time.sleep(.3)
        pg.moveTo(self.posx, self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        print('Purchased Boomerang Monkey At (' + str(self.posx) + ', ' + str(self.posy) + ')')


    def buy_cannon(self):
            click(CANNON[0],CANNON[1])
            time.sleep(.3)
            pg.moveTo(self.posx, self.posy)
            time.sleep(.3)
            click(self.posx, self.posy)
            print('Purchased Bomb Shooter At (' + str(self.posx) + ', ' + str(self.posy) + ')')


    def buy_tack(self):
        click(TACK[0],TACK[1])
        time.sleep(.3)
        pg.moveTo(self.posx,self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        print('Purchased Tack Shooter At (' + str(self.posx) + ', ' + str(self.posy) + ')')


    def buy_ice(self):
        click(ICE[0], ICE[1])
        time.sleep(.3)
        pg.moveTo(self.posx, self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        print('Purchased Ice Monkey At (' + str(self.posx) + ', ' + str(self.posy) + ')')


    def buy_glue(self):
            click(GLUE[0],GLUE[1])
            time.sleep(.3)
            pg.moveTo(self.posx, self.posy)
            time.sleep(.3)
            click(self.posx,self.posy)
            print('Purchased Glue Gunner At (' + str(self.posx) + ', ' + str(self.posy) + ')')

#######################
# MILLITAIRY
#######################

    def buy_sniper(self):
        click(SNIPER[0], SNIPER[1])
        time.sleep(.3)
        pg.moveTo(self.posx, self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        print('Purchased Sniper Monkey At (' + str(self.posx) + ', ' + str(self.posy) + ')')


    def buy_sub(self):
        click(SUB[0], SUB[1])
        time.sleep(.3)
        pg.moveTo(self.posx, self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        print('Purchased Monkey Sub At (' + str(self.posx) + ', ' + str(self.posy) + ')')


    def buy_boat(self):
        click(BOAT[0],BOAT[1])
        time.sleep(.3)
        pg.moveTo(self.posx, self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        print('Purchased Monkey Buccaneer At (' + str(self.posx) + ', ' + str(self.posy) + ')')


    def buy_ace(self):
        click(ACE[1], ACE[2])
        time.sleep(.3)
        pg.moveTo(self.posx, self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        print('Purchased Monkey Ace At (' + str(self.posx) + ', ' + str(self.posy) + ')')


    def buy_heli(self):
        click(HELI[0], HELI[1])
        time.sleep(.3)
        pg.moveTo(self.posx, self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        print('Purchased Heli Pilot At (' + str(self.posx) + ', ' + str(self.posy) + ')')


    def buy_mortar(self):
        pg.moveTo(1712,897)
        drag(1712, 897, 1712, 100, True)
        click(1712,210)
        time.sleep(.3)
        pg.moveTo(self.posx,self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        time.sleep(.4)
        print('Purchased Mortar At (' + str(self.posx) + ', ' + str(self.posy) + ')')
        pg.moveTo(1712, 210)
        drag(1712, 200, 1712, 912, True)


    def buy_dartling(self):
        pg.moveTo(1712,897)
        drag(1712, 897, 1712, 100, True)
        click(1812,219)
        time.sleep(.3)
        pg.moveTo(self.posx,self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        time.sleep(.4)
        print('Purchased Dartling Gunner At (' + str(self.posx) + ', ' + str(self.posy) + ')')
        pg.moveTo(1812,219)
        drag(1712, 200, 1712, 912, True)


#######################
# MAGIC
#######################

    def buy_wizard(self):
        pg.moveTo(1712,897)
        drag(1712, 897, 1712, 100, True)
        click(1705,339)
        time.sleep(.3)
        pg.moveTo(self.posx,self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        time.sleep(.4)
        print('Purchased Wizard Monkey At (' + str(self.posx) + ', ' + str(self.posy) + ')')
        pg.moveTo(1812,219)
        drag(1712, 200, 1712, 912, True)


    def buy_super(self):
        pg.moveTo(1712,897)
        drag(1712, 897, 1712, 100, True)
        click(1829,343)
        time.sleep(.3)
        pg.moveTo(self.posx,self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        time.sleep(.4)
        print('Purchased Super Monkey At (' + str(self.posx) + ', ' + str(self.posy) + ')')
        pg.moveTo(1812,219)
        drag(1712, 200, 1712, 912, True)


    def buy_ninja(self):
        pg.moveTo(1712,897)
        drag(1712, 897, 1712, 100, True)
        click(1712,475)
        time.sleep(.3)
        pg.moveTo(self.posx,self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        time.sleep(.4)
        print('Purchased Ninja Monkey At (' + str(self.posx) + ', ' + str(self.posy) + ')')
        pg.moveTo(1812,219)
        drag(1712, 200, 1712, 912, True)


    def buy_alch(self):
        pg.moveTo(1712,897)
        drag(1712, 897, 1712, 100, True)
        click(1835,479)
        time.sleep(.3)
        pg.moveTo(self.posx,self.posy)
        time.sleep(.3)
        click(self.posx,self.posy)
        time.sleep(.4)
        print('Purchased Alchemist At (' + str(self.posx) + ', ' + str(self.posy) + ')')
        pg.moveTo(1812,219)
        drag(1712, 200, 1712, 912, True)


    # def buy_alch(self):
    #         pg.moveTo(1712,897)
    #         drag(1712, 897, 1712, 100, True)
    #         click(1835,479)
    #         time.sleep(.3)
    #         pg.moveTo(self.posx,self.posy)
    #         time.sleep(.3)
    #         click(self.posx,self.posy)
    #         time.sleep(.4)
    #         print('Purchased Alchemist At (' + str(self.posx) + ', ' + str(self.posy) + ')')
    #         pg.moveTo(1812,219)
    #         drag(1712, 200, 1712, 912, True)


    def buy_druid(self):
            pg.moveTo(1712,897)
            drag(1712, 897, 1712, 100, True)
            click(1712,615)
            time.sleep(.3)
            pg.moveTo(self.posx,self.posy)
            time.sleep(.3)
            click(self.posx,self.posy)
            time.sleep(.4)
            print('Purchased Druid At (' + str(self.posx) + ', ' + str(self.posy) + ')')
            pg.moveTo(1812,219)
            drag(1712, 200, 1712, 912, True)


#######################
# SUPPORT
#######################

    def buy_farm(self):
            pg.moveTo(1712,897)
            drag(1712, 897, 1712, 100, True)
            click(1829,621)
            time.sleep(.3)
            pg.moveTo(self.posx,self.posy)
            time.sleep(.3)
            click(self.posx,self.posy)
            time.sleep(.4)
            print('Purchased Bannana Farm At (' + str(self.posx) + ', ' + str(self.posy) + ')')
            pg.moveTo(1812,219)
            drag(1712, 200, 1712, 912, True)


    def buy_sfactory(self):
            pg.moveTo(1712,897)
            drag(1712, 897, 1712, 100, True)
            click(1712,755)
            time.sleep(.3)
            pg.moveTo(self.posx,self.posy)
            time.sleep(.3)
            click(self.posx,self.posy)
            time.sleep(.4)
            print('Purchased Spike Factory At (' + str(self.posx) + ', ' + str(self.posy) + ')')
            pg.moveTo(1812,219)
            drag(1712, 200, 1712, 912, True)


    def buy_village(self):
            pg.moveTo(1712,897)
            drag(1712, 897, 1712, 100, True)
            click(1821,751)
            time.sleep(.3)
            pg.moveTo(self.posx,self.posy)
            time.sleep(.3)
            click(self.posx,self.posy)
            time.sleep(.4)
            print('Purchased Monkey Village At (' + str(self.posx) + ', ' + str(self.posy) + ')')
            pg.moveTo(1812,219)
            drag(1712, 200, 1712, 912, True)


    def buy_engineer(self):
            pg.moveTo(1712,897)
            drag(1712, 897, 1712, 100, True)
            click(1712,909)
            time.sleep(.3)
            pg.moveTo(self.posx,self.posy)
            time.sleep(.3)
            click(self.posx,self.posy)
            time.sleep(.4)
            print('Purchased Engineer Monkey At (' + str(self.posx) + ', ' + str(self.posy) + ')')
            pg.moveTo(1812,219)
            drag(1712, 200, 1712, 912, True)


#######################
# MONKEY ACTIONS
#######################

    def set_targeting(self, new_target):
        if(self.posx > 834):
            leftopening = True
        else:
            leftopening = False


        print('Setting Targeting To ' + self.current_targeting)
        click(self.posx, self.posy)
        print('Opened Menu!')
        if not leftopening:
            print('rightOpening')
            if(self.current_targeting == None or new_target == None):
                return
            if(self.current_targeting == 'first'):
                if(new_target.lower() == 'last'):		
                    print('Setting Monkey Targeting To Last!')
                    click(1580,378)
                    self.current_targeting = 'last'
                elif(new_target.lower() == 'close'):
                    print('Setting Monkey Targeting To Close!')
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    self.current_targeting = 'close'
                elif(new_target.lower() == 'strong'):
                    print('Setting Monkey Targeting To Strong!')
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    self.current_targeting = 'strong'
                else:
                    print('Need A Valid Targeting Not: ' + new_target)
            elif(self.current_targeting == 'close'):
                if(new_target.lower() == 'strong'):		
                    print('Setting Monkey Targeting To Stong!')
                    click(1580,378)
                    self.current_targeting = 'strong'
                elif(new_target.lower() == 'first'):
                    print('Setting Monkey Targeting To First!')
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    self.current_targeting = 'first'
                elif(new_target.lower() == 'last'):
                    print('Setting Monkey Targeting To Last!')
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    self.current_targeting = 'last'
                else:
                    print('Need a targeting')
            elif(self.current_targeting == 'last'):
                if(new_target.lower() == 'close'):		
                    print('Setting Monkey Targeting To Close!')
                    click(1580,378)
                    self.current_targeting = 'close'
                elif(new_target.lower() == 'strong'):
                    print('Setting Monkey Targeting To Strong!')
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    self.current_targeting = 'strong'
                elif(new_target.lower() == 'first'):
                    print('Setting Monkey Targeting To First!')
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    self.current_targeting = 'first'
                else:
                    print('Need a targeting')
            elif(self.current_targeting == 'strong'):
                if(new_target.lower() == 'first'):		
                    print('Setting Monkey Targeting To First!')
                    click(1580,378)
                    self.current_targeting = 'first'
                elif(new_target.lower() == 'last'):
                    print('Setting Monkey Targeting To Last!')
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    self.current_targeting = 'last'
                elif(new_target.lower() == 'close'):
                    print('Setting Monkey Targeting To Close!')
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    time.sleep(.2)
                    click(1580,378)
                    self.current_targeting = 'close'
                else:
                    print('Need a targeting you typed' + new_target)
            else:
                print('Thats Not A Possible Target Option!!! Please Enter first, close, last, or strong!')
        else:
            print('leftOpening')
            if(self.current_targeting == None or new_target == None):
                return
            if(self.current_targeting == 'first'):
                if(new_target.lower() == 'last'):		
                    print('Setting Monkey Targeting To Last!')
                    click(360,378)
                    self.current_targeting = 'last'
                elif(new_target.lower() == 'close'):
                    print('Setting Monkey Targeting To Close!')
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    self.current_targeting = 'close'
                elif(new_target.lower() == 'strong'):
                    print('Setting Monkey Targeting To Strong!')
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    self.current_targeting = 'strong'
                else:
                    print('Need A Valid Targeting Not: ' + new_target)
            elif(self.current_targeting == 'close'):
                if(new_target.lower() == 'strong'):		
                    print('Setting Monkey Targeting To Stong!')
                    click(360,378)
                    self.current_targeting = 'strong'
                elif(new_target.lower() == 'first'):
                    print('Setting Monkey Targeting To First!')
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    self.current_targeting = 'first'
                elif(new_target.lower() == 'last'):
                    print('Setting Monkey Targeting To Last!')
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    self.current_targeting = 'last'
                else:
                    print('Need a targeting')
            elif(self.current_targeting == 'last'):
                if(new_target.lower() == 'close'):		
                    print('Setting Monkey Targeting To Close!')
                    click(360,378)
                    self.current_targeting = 'close'
                elif(new_target.lower() == 'strong'):
                    print('Setting Monkey Targeting To Strong!')
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    self.current_targeting = 'strong'
                elif(new_target.lower() == 'first'):
                    print('Setting Monkey Targeting To First!')
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    self.current_targeting = 'first'
                else:
                    print('Need a targeting')
            elif(self.current_targeting == 'strong'):
                if(new_target.lower() == 'first'):		
                    print('Setting Monkey Targeting To First!')
                    click(360,378)
                    self.current_targeting = 'first'
                elif(new_target.lower() == 'last'):
                    print('Setting Monkey Targeting To Last!')
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    self.current_targeting = 'last'
                elif(new_target.lower() == 'close'):
                    print('Setting Monkey Targeting To Close!')
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    time.sleep(.2)
                    click(360,378)
                    self.current_targeting = 'close'
                else:
                    print('Need a targeting you typed' + new_target)
            else:
                print('Thats Not A Possible Target Option!!! Please Enter first, close, last, or strong!')
        click(self.posx,self.posy)

    def sell(self):
        click(self.posx,self.posy)
        if(self.posx > 834):
            leftopening = True
        else:
            leftopening = False

        if(leftopening == True):
            click(317 , 900)
        else: click(1527, 900)
        
        
        click(self.posx,self.posy)
        print('sold!')
        


    def upgrade(self, path):
        print('Upgrading...')
        click(self.posx , self.posy)
        time.sleep(.2)

        if(self.posx > 834):
            leftopening = True
        else:
            leftopening = False

        if(path == 1 and leftopening == False):
            pg.moveTo(1553, 481)
            time.sleep(.3)
            click(1553, 481)
          
            print('Bought UPG 1')
        elif(path == 2 and leftopening == False):
            pg.moveTo(1553, 631)
            time.sleep(.3)
            click(1553, 631)
           
            print('Bought UPG 2')
        elif(path == 3 and leftopening == False):
            pg.moveTo(1553, 780)
            time.sleep(.3)
            click(1553, 780)
           
            print('Bought UPG 3')
        elif(path == 1 and leftopening == True):
            pg.moveTo(333, 469)
            time.sleep(.3)
            click(333, 481)
          
            print('Bought UPG 1')
        elif(path == 2 and leftopening == True):
            pg.moveTo(333, 631)
            time.sleep(.3)
            click(333, 631)
           
            print('Bought UPG 2')
        elif(path == 3 and leftopening == True):
            pg.moveTo(333, 780)
            time.sleep(.3)
            click(333, 780)
      
        click(self.posx , self.posy)
        print('Upgraded!')




def startgame_Speed():
	click(1829,1014)
	click(1829,1014)
	print('Started Game!')

def startgame_Normal():
    click(1829,1014)
    print('Started Game!')


        