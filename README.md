# Python-Kniffel
[![Pylint](https://github.com/Tobias-Jung-DHBW/Python-Kniffel/actions/workflows/pylint.yml/badge.svg)](https://github.com/Tobias-Jung-DHBW/Python-Kniffel/actions/workflows/pylint.yml)
[![Dependency Review](https://github.com/Tobias-Jung-DHBW/Python-Kniffel/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/Tobias-Jung-DHBW/Python-Kniffel/actions/workflows/dependency-review.yml)

![image](https://user-images.githubusercontent.com/99813121/166121459-89470b1b-7a9b-4438-ad6d-4fdfae450076.png)


## Running the game on Linux
Sadly the terminal cant be resized on linux programatically. Which is why the terminal has to be big enough to \
fit the entire game otherwise the error addstr will be raised.

## Installation
To build the project run in the Python-Kniffel directory "python setup.py build" \
To the install the project run "python setup.py install"

## Development
pip install -e . (install by linking to code) has to be rerun after change on setup.py \
add project root to pythonpath

## Testing
Some tests test animations which have time delays which means that they will require a little of time
### Testing on Windows 
Terminal cannot be in full-screen otherwise reload failes
