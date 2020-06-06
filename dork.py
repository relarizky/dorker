#!/usr/bin/python3

from time import sleep
from sys import argv, exit
from dorker_class import MyDorker

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
def main(argv):
    if len(argv) != 2:
        print('[!] Usage : {} "your dork"'.format(argv[0]))
        exit(1)

    my_dorker = MyDorker()
    my_dorker.dork = argv[-1]
    url_found = set(my_dorker.google_dorker() + list(my_dorker.bing_dorker()))

    if bool(url_found) != False:
        for url in url_found:
            print(url)

        save = input('[?] Wanna save this output (y/n) ?').lower()

        if save == 'n' or save == 'no':
            exit(0)
        else:
            filename = input('[+] Your filename : ')
            write_file(filename, url_found)


if __name__ == '__main__':
    main(argv)
