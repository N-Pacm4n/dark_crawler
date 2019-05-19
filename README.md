# dark_crawler
Dork scanner and exploiter

This tool scans different search engines for a dork and return URL's.

[This tool is under development phase some features might not work] 

# Requirements
1. Linux
2. Python 3 or above
```
apt-get install python3
```


# How to
```
python3 dark_cralwer.py
```
# Options
```
-h, --help            show this help message and exit
  -d DORK, --dork=DORK                  String to search [eg:- index.php?id=]
  --engine=bing                         Search engine to use google,bing,all
  --pages=5                             Number of pages to scan
  --site=SITE                           Specify site for specific results
  --output=file.txt                     Save ouput to file
  --threads=2                           Number of parallel processes
```
# Example
```
python3 dark_crawler.py -d inurl:index.php?id= --pages=5 --threads=7
```

# Devoloped By
```
Aman Pachauri ( paradox47.blogspot.com )
```
