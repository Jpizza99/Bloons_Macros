# BloonsMacro

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

The Monkey Class Takes in 4 peramiters
Monkey(int: x location, int: y location, str: Monkey Type, **OPTIONAL** str: Targeting)






