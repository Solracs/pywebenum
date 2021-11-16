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
    else:
        print("Incorrect input")
        print("python3 pywebnum -u <url> -w <path to wordlist>")
        sys.exit()

    with open(path, 'r') as wordlist:
        for i in wordlist:
            r = requests.get(url+i)
            if r.status_code == 200:
                print(url+i, "status: "+str(r.status_code))
