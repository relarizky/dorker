#!/usr/bin/python3

from time import sleep
from sys import argv, exit
from dorker.dorker import MyDorker
from dorker.parse_argument import args

def banner(function):
    def printed_text(*args, **kwargs):
        print(" _____   ___       _    ____")
        print("|  __ \ / _ \     | |  |___ \\")
        print("| |  | | | | |_ __| | __ __) |_ __")
        print("| |  | | | | | '__| |/ /|__ <| '__|")
        print("| |__| | |_| | |  |   < ___) | |")
        print("|_____/ \___/|_|  |_|\_\____/|_|")
        print("        [C0ded by br0k3nh34rtz]\n")
        function(*args, **kwargs)
    return printed_text


def write_file(filename, content):
    try:
        with open(filename, "a+") as file:
            for url in content: file.write(url + "\n")
            print("[+] Saved in {}".format(filename))
    except Exception:
        print("[!] Check your directory permission!")
        exit(1)
    finally:
        file.close()


@banner
def main(dork, search_engine = None, save_file = None):
    if search_engine == None:
        print('[+] Use both Google and Bing Search Engine')
    else:
        print('[+] Use {} Search Engine'.format(search_engine.capitalize()))

    sleep(1)

    try:
        my_dorker = MyDorker(dork)
        if search_engine == 'google':
            url_found = set(my_dorker.google_dorker())
        elif search_engine == 'bing':
            url_found = set(list(my_dorker.bing_dorker()))
        else:
            url_found = set(my_dorker.google_dorker(), list(my_dorker.bing_dorker()))
    except KeyboardInterrupt as Error:
        print('[-] You stopped the program.')
        exit(1)

    if bool(url_found) != False:
        for url in url_found:
            print(url)
        if save_file != None:
            write_file(save_file, url_found)

if __name__ == '__main__':

    if args.google == True:
        search_engine = 'google'
    elif args.bing == True:
        search_engine = 'bing'
    elif args.all == True:
        search_engine = None
    else:
        search_engine = None

    main(args.dork, search_engine, args.file)
