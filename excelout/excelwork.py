#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   This example uses pyexcel to perform Excel manipulation."""


import pyexcel

def get_ip_data():
    input_ip = input("\nWhat is the IP Address?")
    input_driver = input("\nWhat is the driver associated with this device?")
    d = {"IP":input_ip, "driver":input_driver}
    return d


mylistdict = []

print("Hello! This program will make you a *.xlsx file")

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue or enter 'q' to quit: ")
    if(keep_going.lower() == 'q'):
        break


filename = input("\nEnter the name of the file you want to save your data.")


pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")
