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
