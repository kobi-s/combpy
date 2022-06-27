import json
import hashlib
from itertools import chain, permutations
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--token", help="Your hash token", dest="token")
parser.add_option("-a", "--algorithem", choices=list(hashlib.algorithms_available), help='The name of the hash algorithm to use', dest="algorithem", default='md5')
parser.add_option("-w", "--words", help="Wordlist separated by a comma without spaces", dest="words")
parser.add_option("-s", "--separators", help="Your separators, separated by a comma (If not provided all separators will be used)", dest="separators")

(options, args) = parser.parse_args()

hashtoken =  options.token.lower()
wordlist = set(options.words.split(","))
separators = list()
list_combinations = list()

if options.separators is None:
     separators = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '.', ',', '/', '\/', '~', ';', '`', '>', '<', '<>', '|', '||', ':', '::', ':::', '?')
else: 
     separators = options.separators.split(',')

for n in range(len(wordlist) + 1):
    list_combinations = list(chain.from_iterable([permutations(wordlist, x) for x in range(len(wordlist)+1)]))

def build(separator, combination):
    return separator.join(combination)

if __name__ == "__main__":
    success = None
    counter = len(list_combinations) * len(separators) 
    for combination in list_combinations:
        for sep in separators:
            row = build(sep, combination)
            h = hashlib.new(options.algorithem)
            h.update(row.encode('utf-8'))
            checksum = h.hexdigest()
            if(hashtoken == checksum):
                success = row
                break
            print(row, checksum)
    if success is not None:
        print('\n# Hash Found!   ', hashtoken)
        print('# From String:  ', success)
    else: 
        print('\n0 hashes were found in ' + str(counter) +' attempts')
