import urllib.request
import threading
import sys


def run_check():
    threading.Timer(2.0, run_check).start()
    print("HTTP Request sent.")
 
run_check()

while (True):
    name = input("Enter a name: ")
    print(name)
