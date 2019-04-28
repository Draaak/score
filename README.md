[![Build Status](https://travis-ci.com/Draaak/score.svg?branch=master)](https://travis-ci.com/Draaak/score)
# Score
A demo python script to process sports match scores.
## Prerequisites
### Pip
```bash
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && sudo python get-pip.py
```
## Setup
The app contains a requirements.txt file with all the dependancies.
Run the following command to set them up:
```
 $ pip install -r requirements.txt
```
## Examples
A test file is included, called scores.txt.
```bash
$ python rank scores.txt
```
or
```bash
$ cat scores.txt | python rank.py
```

