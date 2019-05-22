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
from multiprocessing import Pool, freeze_support
import textwrap
import random
from random import randint
from time import sleep




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


def save_output(results, filename) :
    list = results
    with open(filename, 'w') as file:
        for x in results :
            file.write(x + '\n')
    file.close()

def banner() :
    print(Fore.YELLOW + Style.BRIGHT +"""
 ╔╦╗┌─┐┬─┐┬┌─  ╔═╗┬─┐┌─┐┬ ┬┬  ┌─┐┬─┐
  ║║├─┤├┬┘├┴┐  ║  ├┬┘├─┤││││  ├┤ ├┬┘
 ═╩╝┴ ┴┴└─┴ ┴  ╚═╝┴└─┴ ┴└┴┘┴─┘└─┘┴└─
    """+Fore.RESET)
    print(Fore.GREEN + Style.NORMAL  +'Developed by Aman pachauri (paradox47.blogspot.com)'+Fore.RESET)
    print(Fore.BLUE + Style.NORMAL+'\t\t\t\tversion [stable-1.2]\n\n'+ Fore.RESET)

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
    group_misc = OptionGroup(parser, "Misc")
    group_misc.add_option("--filter", dest="filter", action="store_true", help="Turn on URL filter(gives specific result)")
    parser.add_option_group(group_misc)
    (options, args) = parser.parse_args()
    if options.dork != None :
        engine = options.engine
        search = options.dork
        pages = options.pages
        domain = options.domain
        filter_op = options.filter
        processes = options.processes
        file = options.ofile
        msg.info('Starting Crawler')
        msg.blue('[ENGINE] '+ engine)
        msg.warning('Excess use of this tool can get your IP address banned and you may get 0 or false results ')
        start = timer()
        if engine == "google" :
            if domain != None :
                search = str(search + ' SITE:'+ domain)
            result_c = google_c.dork_scanner(search, pages, processes)
            result = google.dork_scanner(search, pages, processes)
            if not result or not result_c :
                msg.error('It seems like google has BANNED your IP ADDRESS. we recommend you use different engine [--engine=] or search google using browser')
                msg.shutdown()
            else :
                if filter_op == True :
                    msg.info('Starting filter')
                    sleep(1)
                    result = filter(result)
                    result_c = filter(result_c)
                    for x in result :
                        print('[LINK] '+ x)
                    for x in result_c :
                        print('[LINK] '+ x)

                else :
                    for x in result :
                        print('[LINK] '+ x )
                    for x in result_c :
                        print('[LINK] '+ x)
                msg.info('Total Url Grabbed : '+ str(len(result) + len(result_c)))
                msg.info('Total time taken : '+ str((timer() - start)))
                if options.ofile != None :
                    save_output(result, file)
                    msg.info(' Urls written to '+ file)
                msg.shutdown()
        elif engine == "bing" :
            if domain != None :
                search = str(search + ' SITE:'+ domain)
            result = bing.dork_scanner(search, pages, processes)
            if not result :
                msg.error('It seems like bing has BANNED your IP ADDRESS. we recommend you use different engine [--engine=] or search bing using browser')
                msg.shutdown()
            else:
                if filter_op == True :
                    msg.info('Starting filter')
                    result = filter(result)
                    for x in result :
                        print('[LINK] '+ x)
                else :
                    for x in result :
                        print('[LINK] '+ x)
                msg.info('Total Url Grabbed : '+ str(len(result)))
                msg.info('Total time taken : '+ str((timer() - start)))
                if options.ofile != None :
                    save_output(result, file)
                    msg.info(' Urls written to '+ file)
                msg.shutdown()
        elif engine == "all" :
            if domain != None :
                search = str(search + ' SITE:'+ domain)
            result_wc = webcrawler.dork_scanner(search,pages,processes)
            result_b = bing.dork_scanner(search, pages, processes)
            if filter_op == True :
                msg.info('Starting filter')
                result_f = result_b + result_wc
                result_f = filter(result_f)
                for x in result_f :
                    print('[LINK] '+ x)
            else :
                for x in result_f :
                    print('[LINK] '+ x )
            msg.info('Total Url Grabbed : '+ str(len(result_b) + len(result_wc)))
            msg.info('Total time taken : '+ str((timer() - start)))
            if options.ofile != None :
                save_output(result_wc, file)
                save_output(result_b, file)
                msg.info(' Urls written to '+ file)
            msg.shutdown()
        elif engine == "webcrawler" :
            if domain != None :
                search = str(search + ' SITE:'+ domain)
            result = webcrawler.dork_scanner(search, pages, processes)
            if not result :
                msg.error('It seems like Web-crawler has BANNED your IP ADDRESS. we recommend you use different engine [--engine=] or search use browser')
                msg.shutdown()
            else:
                if filter_op == True :
                    msg.info('Starting filter')
                    result = filter(result)
                    for x in result :
                        print('[LINK] '+ x)
                else :
                    for x in result :
                        print('[LINK] '+ x)
                msg.info('Total Url Grabbed : '+ str(len(result)))
                msg.info('Total time taken : '+ str((timer() - start)))
                if options.ofile != None :
                    save_output(result, file)
                    msg.info(' Urls written to '+ file)
                msg.shutdown()
        else :
            msg.error("\nInvalid Engine")
            msg.shutodwn()
    else :
        parser.print_help()


if __name__ == '__main__':
    main()
