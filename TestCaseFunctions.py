import tkinter as tk
import urllib.request
import random
import sys

def URLFilter():
    with open('website_list.txt', 'r') as f:
        # creating an array for "pass" cases
        succ_listU = []
        # creat ping an array for "fail" cases
        fail_listU = []
        while(True):
                content = f.readline()
                url = content
                if content == "":
                    break
                try:
                    urllib.request.urlopen(url)
                    succ_listU.append(url)  #array gets success events
                    #print("Gained access to "+ url)  #acknowledgement of success events
                    #global p0
                    #p0 = str(len(succ_listU))
                except Exception as e:
                    print(e)  #print exception cases
                    #global p1
                    #p1 = str(len(fail_listU))

                #print('Number of URL pass: ' + str(len(succ_listU)))  #Number of success events
                #print('Number of URL fail: ' + str(len(fail_listU)))  #Number of fail events
                #p1=str(len(fail_listU))

        a = str(len(succ_listU))
        b= str(len(fail_listU))

    return a, b


def FileBlocking():
    # creating an array for "pass" cases
    succ_listF = []
    # creating an array for "fail" cases
    fail_listF = []
    with open('download_list.txt', 'r') as f:
        i = 0
        while(True):
                content = f.readline()
                url = content
                if content == "":
                    break
                try:
                    succ_listF.append(url)  # array gets success events
                    full_name = str(i) +".jpg"
                    i = i +1
                    x = urllib.request.urlretrieve(url, full_name)
                    print('gained access to '+ url)
                except Exception as e:
                    print(e)
                    fail_listF.append(url)  # array gets fail events

                #print('Number of File Blocks pass: ' + str(len(succ_listF)))  # Number of success events
                #print('Number of File Blocks fail: ' + str(len(fail_listF)))  # Number of fail events

                #error correction
                # #GUI status bar, clear it and tell them to input again
                #      print('did not have access to '+ url)
        c = str(len(succ_listF))
        d= str(len(fail_listF))

    return c,d



URLenable = 1
FileBlocking_enable = 0

if URLenable == 1:
    URLFilter()
if FileBlocking_enable == 1:
    FileBlocking()
