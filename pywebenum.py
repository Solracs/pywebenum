#!/usr/bin/python3

import requests
import argparse
import sys
#import threading

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', type = str, required = True, help = "Target's url")
    parser.add_argument('-w', type = str, required = True, help = "Wordlist")
    #parser.add_argument('-t', type = int, required = True, help = "Number of threads")

    args = parser.parse_args()

    if args.u and args.w:
        url = args.u
        path = args.w
        opened = []
    else:
        print("Incorrect input")
        print("python3 pywebnum -u <url> -w <path to wordlist>")
        sys.exit()

    with open(path, 'r') as wordlist:
        for i in wordlist:
            if url[-1] != '/':
                url = url + '/'
            urlextended = url + i
            r = requests.get(urlextended)
            if r.status_code == 200:
                print(urlextended, " -> "+str(r.status_code))
                opened.append(urlextended)
