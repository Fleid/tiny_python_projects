# Tiny Python Projects

## Chapter 0 - Installation

First pip was missing so:

```BASH
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py
python3 -m pip install -U pip
```

Got an error message : ` The scripts pip, pip3 and pip3.8 are installed in '/home/fleide/.local/bin' which is not on PATH`
Which means I need to add that directory to the `PYTHONPATH`.
On Ubuntu (WSL), that's in `~/.bashrc` where you add `export PYTHONPATH="${PYTHONPATH}:/my/other/path"`

Then after forking the repo:

```BASH
git clone https://github.com/Fleid/tiny_python_projects
cd tiny_python_projects
python3 -m pip install -r requirements.txt
```
The requirements installed:
- Code formatters : black, yapf
- Linters : Pylint, flake8
- Type hints : Mypy
- Interactive (notebook) Python : ipython

### NB

```BASH
yapf -i hello.py
bin/new.py HelloWorld.py
```

## Chapter 1 - Write and test a Python program

```BASH
pytest -v -x test.py
```

Add a shush bang (#!) to get the file executable from the shell
Use `which python3` to find which one to link to, then add `#!/usr/bin/python3` to the file
Or default to the env via `#!/usr/bin/env python3` to make it portable
Then run with `./hello.py` (if necessary `chmod +x hello.py`)

Nice to have:
- make with a `Makefile` for testing

### Parameters

Using `argparse`


```Python
import argparse

parser = argparse.ArgumentParser(description='Say Hello')
#parser.add_argument('name', help='Name to greet, positional')
parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet, optional')
args = parser.parse_args()
```

### Linting

```BASH

flake 8 hello.py
pylint hello.py

```


## Chapter 2 - Working with strings

### Getting part of a string

```Python

help(str)

word[n]     # from left, 1 char starting at 0
word[-n]    # from right, 1 char starting at -1

# slicing a string as a list of strings

word[n:p]   # substring()
word[:p]    # left()
word[n:]    # right()

```

## Chapter 3 - Working with lists

``` Python

items = list()
len(items)

items.append('b')
items.append(['c','d']) # ['b', ['c', 'd']]
items.extend(['c','d']) # ['b', 'c', 'd']

items.insert(0, 'a')
items.index('chips')    # returns 0, unsafe - check if there before
                        # slicing applies, and is safe

items.pop()             # removes index -1 (last)
items.pop(0)            # a

items.remove('b')       # removes the first occurence, unsafe - check if there before

items.sort()            # in-place
items.sort(reverse=True)
items.reverse()         #in-place
sorted(items)           # returns a new sorted list
reversed(items)         #returns a new reversed list, lazy, needs to be invoked via list(...)

items_joined = ', '.join(items)        # output a single list with separator


```
