# BloonsMacro

*Note*  **: This Package does make use of your mouse to place monkeys**

Making Bloons Macroing Easier!

Requires 1920x1080p Or Full HD to function
The above will be changed to work on different Settings in the future!

## Install

Use The Package Manager Pip To Install BloonMacro

```bash
pip install BloonsMacro
```


## Usage

```python
from BloonsMacro.macros import Monkey

# Places A Dart Monkey At Coords 500, 600 with strong as its targeting
# Targeting is optional
myDart = Monkey(500, 600, 'dart', 'strong')

# Sets the dart monkeys current targeting to close
myDart.set_targeting('close')


```

#### Example Round Tracker
```python
# For Image Tracking
import pyautogui as pg

# For cooldown
import time

#Initial Round
round = 0

# Round Change Loop
while True:
    
    # Check to see if the round image Changed 
    if(pg.locateOnScreen(lvl) != None):
        time.sleep(.9)
    else: 
        # Increase Rounf Num
        round += 1
        print('Round: ' + round)
        # screenshot location for Full HD monitors
        lvl= pg.screenshot(region=(1442,1,118,69))
        time.sleep(.2)

```

## Syntax
The Monkey Class Takes in 4 peramiters <br/>
```python
#Targeting is optional by default will be first
Monkey(int: x_location, int: y_location, str: monkey_type, str: targeting = None)

# The monkey class has a few branching functions that can be used to upgrade sell and retarget monkeys.
# For example if i created a sub on strong targeting at coords (700 872) and saved a refrence to it
sub = Monkey(700, 872, 'sub', 'strong')

# If i wanted to upgrade the sub to a 1-0-0 then I can do
sub.upgrade(1)

# Finally If i wanted to set the targeting to first I do
sub.targeting('first')

```

## Monkey Type Names

**'hero'<br/>
'dart'<br/>
'tack'<br/>
'boomer'<br/>
'cannon'<br/>
'ice'<br/>
'glue'<br/>
'snipe'<br/>
'sub'<br/>
'boat'<br/>
'ace'<br/>
'heli'<br/>
'mortar'<br/>
'dartling'<br/>
'wizard'<br/>
'super'<br/>
'ninja'<br/>
'alch'<br/>
'druid'<br/>
'farm'<br/>
'sfactory'<br/>
'village'<br/>
'engineer'** <br/>














