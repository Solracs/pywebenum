#!/usr/bin/python3

import requests
import argparse
import sys

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', type = str, required = True, help = "Target url")
    parser.add_argument('-w', type = str, required = True, help = "Wordlist")
    parser.add_argument('-o', type = str, required = False, help = "outputFile")

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

        for ext in wordlist:
            # Remove newline
            ext = ext.strip('\n')

            # Add / at the end of the url if needed
            if url[-1] != '/':
                url = url + '/'

            urlextended = url + ext
            r = requests.get(urlextended)

            if r.status_code == 200:
                print(urlextended, " -> "+str(r.status_code))
                opened.append(urlextended)


    if args.o:

        oFile = args.o

        with open(oFile, 'w') as f:
            f.write("Check github repo -> https://github.com/Solracs/pywebenum\n")
            f.write("Made by: SolracS\n")
            f.write(80*"-")
            f.write("\n")
            f.write("Pywebenum Results:")
            f.write("\n")
            f.write("\n")
            f.write("OK reponses:")
            f.write("\n")
            for url in opened:
                f.write("\t"+url+"\n")

            f.write(80*"-"+"\n")
