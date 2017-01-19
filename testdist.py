# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#this is Python3, so print statements look different. It should be backwards-compatible with Python2
#doing this in list vs using csv
#import googlemaps
#import csv
#reading files, spliting by new line, then splitting by comma
with open('origin.csv','r') as o:
    origins=o.read().split("\n")
    print("raw origin data\n", origins)
for index, city in enumerate(origins):
    origins[index]=city.split(",")
    print("leaving from: ",origins)
    #you might need to do something like map to read the coordinates as integers vs string
with open('destination.csv','r') as d:
    destinations=d.read().split("\n")
    print("raw destination data\n", destinations)    
for index, city in enumerate(destinations):
    destinations[index]=city.split(",")
    print("Going to: ",destinations)    
    #you might need to do something like map to read the coordinates as integers vs string
for from_index, leavingfrom in enumerate(origins):
    #looping through each origin
    #you don't really need enumerate here; it helped me think this through, and I was too lazy to remove it
    for to_index, goingto in enumerate(destinations):
        #for each origin, looping through each destination
        print("This is pairing {0} for origin {1}".format(to_index+1, from_index+1))
        print("Going from {0} origin to {1} destination".format(leavingfrom+1,goingto))
        #this is where you'd put the code to calculate distance
        with open('output.csv','a') as output:
            #putting all the output in a string. There are different ways to do this-CSV probably works
            #add the distance info somewhere here, and whatever else you need to write
            outputrow=",".join(leavingfrom)+","+",".join(goingto)+"\n"
            print(outputrow)
            output.write(outputrow)
                
