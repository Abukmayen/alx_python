#!/usr/bin/python3
'''a python script that fetches a url'''


import urllib.request 


if __name__ == '__main__':
    with urllib.reguset.urlopen('https://alu-intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
