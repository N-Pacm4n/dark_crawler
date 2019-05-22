# dark_crawler
#### *version stable-1.2*

Dork scanner and exploiting framework

This tool scans different search engines using a dork and return URL's corresponding to that dork.

[This tool is under development phase some features might not work]

## Requirements

1. Python 3 or above

### On Linux
```
apt-get install python3
```
### On Windows
* [python-3.7](https://www.python.org/downloads/) - Python Version 3.7

2. Install requirements
```
pip install -r requirements.txt
```

## How to Execute

#### Linux
```
python3 dark_cralwer.py -h
```
#### Windows
```
dark_crawler.py -h
```
## Options
```
-  -h, --help            show this help message and exit
  -d DORK, --dork=DORK  String to search [eg:- index.php?id=]
  --engine=bing         Search engine to use google,bing,all
  --pages=2             Number of pages to scan
  --domain=DOMAIN       Specify domain for specific results
  --output=file.txt     Save ouput to file
  --threads=2           Number of parallel processes

  Misc:
    --filter            Turn on URL filter(gives specific result)

```
## Example
```
python3 dark_crawler.py -d inurl:index.php?id= --pages=5 --threads=7
```

# Devoloped By
```
Aman Pachauri ( paradox47.blogspot.com )
```
