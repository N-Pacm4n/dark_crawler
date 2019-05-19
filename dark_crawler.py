from lib.colorama import *
import sys
import os

try:
    from optparse import *
    import requests
    from bs4    import BeautifulSoup
    from functools import partial
    from  time         import time as timer
    from multiprocessing import Pool, freeze_support
    import textwrap
    import random
    from random import randint
    from time import sleep
except ImportError:
    import pip
    print('Installing libraries\n')
    pip.main(['install'],['optparse'],['requests'],['re'],['bs4'],['functools'],['time'],['multiprocessing'],['textwrap'],['random'])
    print('\n\n\nPlease restart dark_crawler')
    exit()



class msg :
    def info(string) :
        init()
        print(Fore.GREEN + '[INFO] ' + string + Fore.RESET ,end='\n')

    def warning(string) :
        init()
        print(Fore.YELLOW + '[WARNING] ' + string + Fore.RESET, end='\n')

    def error(string) :
        init()
        print(Fore.RED + '[ERROR] ' + string + fore.RESET, end='\n')

    def blue(string) :
        init()
        print(Fore.BLUE + string + Fore.RESET, end='\n')

    def shutdown() :
        init()
        print(Back.RED + '\nSHUTTING DOWN DARK CRAWLER' + Back.RESET, end='\n')

def random_ua() :
    dir_path = os.path.dirname(os.path.realpath(__file__))
    lines = open(dir_path +'/core/header').read().splitlines()
    myline =random.choice(lines)
    return myline

def random_delay() :
    delay = randint(3,10)
    msg.info('Delay Set to '+ str(delay) + ' Seconds')
    return delay

class google :
    def get_urls(search_string, start):
        temp        = []
        url         = 'http://www.google.com/search'
        payload     = { 'q' : search_string, 'start' : start }
        my_headers  = { 'User-agent' : random_ua() }
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
        url         = 'https://www.webcrawler.com/serp'
        payload     = { 'q' : search_string, 'page' : start }
        my_headers  = { 'User-agent' : random_ua() }
        sleep(random_delay())
        r           = requests.get( url, params = payload, headers = my_headers )
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
    print(Fore.BLUE + Style.NORMAL+'\t\t\t\tversion [testing]\n\n'+ Fore.RESET)

def main() :
    banner()
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-d","--dork", type="string", dest="dork", metavar="DORK", action="store", help="\t\tString to search [eg:- index.php?id=]")
    parser.add_option("--engine", type="string", dest="engine",metavar="bing", action="store",default="all",help="\t\tSearch engine to use google,bing,all")
    parser.add_option("--pages",type="int",dest="pages",metavar='2',action="store",default="2",help="\t\tNumber of pages to scan")
    parser.add_option("--site",type="string",dest="site",action="store",help="\t\tSpecify site for specific results")
    parser.add_option("--output",type="string",dest="ofile",metavar="file.txt",help='''\t\tSave ouput to file''')
    parser.add_option("--threads",type="int",dest="processes",metavar="2",default="2",help="\t\tNumber of parallel processes")
    # group_target = OptionGroup(parser, "Target")
    # group_target.add_option("-d", "--dork", type="string", dest="dork", metavar="DORK", action="store", help="String to search [eg:- index.php?id=]")
    # parser.add_option_group(group_target)
    (options, args) = parser.parse_args()
    if options.dork != None :
        engine = options.engine
        search = options.dork
        pages = options.pages
        processes = options.processes
        file = options.ofile
        msg.info('Starting Crawler')
        sleep(1)
        msg.blue('[ENGINE] '+ engine)
        sleep(1)
        msg.warning('Too much use of this tool can get your IP adress banned by google and you may get 0 or false results ')
        msg.warning('Please wait............')
        start = timer()
        if engine == "google" :
            result = google.dork_scanner(search, pages, processes)
            if not result :
                msg.error('You searched google too much and got you\'re IP BANNED. we recommend you use different engine [--engine=] or search google using browser')
                msg.shutdown()
            else :
                for x in result :
                    print('[LINK] '+ x )
                msg.info('Total Url Grabbed : '+ str(len(result)))
                msg.info('Total time taken : '+ str((timer() - start)))
                if options.ofile != None :
                    save_output(result, file)
                    msg.info(' Urls written to '+ file)
                msg.shutdown()
        elif engine == "bing" :
            result = bing.dork_scanner(search, pages, processes)
            if not result :
                msg.error('You searched bing too much and got you\'re IP BANNED. we recommend you use different engine [--engine=] or search bing using browser')
                msg.shutdown()
            else:
                for x in result :
                    print('[LINK] '+ x )
                msg.info('Total Url Grabbed : '+ str(len(result)))
                msg.info('Total time taken : '+ str((timer() - start)))
                if options.ofile != None :
                    save_output(result, file)
                    msg.info(' Urls written to '+ file)
                msg.shutdown()
        elif engine == "all" :
            result_wc = webcrawler.dork_scanner(search,pages,processes)
            result_b = bing.dork_scanner(search, pages, processes)
            for x in result_wc :
                print('[LINK] '+ x )
            for x in result_b :
                print('[LINK] '+ x )
            msg.info('Total Url Grabbed : '+ str(len(result_b) + len(result_wc)))
            msg.info('Total time taken : '+ str((timer() - start)))
            if options.ofile != None :
                save_output(result_wc, file)
                save_output(result_b, file)
                msg.info(' Urls written to '+ file)
            msg.shutdown()
        elif engine == "google_cache" :
            result = google_c.dork_scanner(search, pages, processes)
            if not result :
                msg.error('You searched google too much and got you\'re IP BANNED. we recommend you use different engine [--engine=] or search google using browser')
            else:
                for x in result :
                    print(color.BLUE_BOLD +'[ LINK ] '+ x + color.END)
                msg.info('Total Url Grabbed : '+ str(len(result)))
                msg.info('Total time taken : '+ str((timer() - start)))
                if options.ofile != None :
                    save_output(result, file)
                    msg.info(' Urls written to '+ file)
                msg.shutdown()
        elif engine == "webcrawler" :
            result = webcrawler.dork_scanner(search, pages, processes)
            if not result :
                msg.error('You searched webcrawler too much and got you\'re IP BANNED. we recommend you use different engine [--engine=] or search google using browser')
                msg.shutdown()
            else:
                for x in result :
                    print('[LINK] '+ x )
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
