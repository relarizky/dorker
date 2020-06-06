from sys import exit
from argparse import ArgumentParser as ArgParseClass

class ArgumentParser(ArgParseClass):
    def error(self, message):
        self.print_help()
        exit(1)

parser = ArgumentParser(description = 'Simple python based script for dorking with Google and Bing')
groups = parser.add_mutually_exclusive_group()

groups.add_argument('-b', '--bing', help = 'dorking with bing search engine', action = 'store_true')
groups.add_argument('-g', '--google', help = 'dorking with google search engine', action = 'store_true')
groups.add_argument('-a', '--all', help = 'dorking with both bing and google search engine', action = 'store_true')
parser.add_argument('-f', '--file', help = 'filename you\'d like to use for saving output')
parser.add_argument('dork', help = 'dork that you would like to search with')

args = parser.parse_args()

if __name__ == '__main__':
    exit(1)
