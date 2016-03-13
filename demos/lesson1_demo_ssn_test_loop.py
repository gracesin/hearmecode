# -*- coding: utf-8 -*-
#Test to see if SSN is issued by SSA
#Criteroa at http://policy.ssa.gov/poms.nsf/lnx/0110201035
import re

#Doing the same stuff in a loop now - it's less typing!
ssn = ["000-00-0000", "900-12-3456", "888-88-8888", "666-11-5553", "123009876 ", "1234", "a12345", "!09876543", "098-00-1234", "123a34", "012-34-0000", "111111111"]

for test_ssn in ssn:
    test_ssn = test_ssn.replace("-","").strip()
    print "\nTesting {0}{1}{2}{3}{4}. Here we go! Length is {5}".format(test_ssn[:3],"-",test_ssn[3:5],"-",test_ssn[5:],len(test_ssn))
    if len(test_ssn) == 9 and test_ssn.isdigit():#check for correct length and digits only
        #Checking for impossible SSNs
        #The first three digits (former area number) as "000," "666,” or in the 900 series
        if test_ssn[:3] == "000" or test_ssn[:3] == "666" or test_ssn[0] == "9":
            print "SSN starts with an impossible sequence: {0}".format(test_ssn[:3])
        #The second group of two digits (former group number) as "00."
        elif test_ssn[3:5] == "00":
            print "SSN has '00' in the fourth and fifth digits."
        #The third group of four digits (former serial number) as "0000."
        elif test_ssn[5:] == "0000":
            print "SSN ends with '0000.'"
        else:
            print "SSN is not impossible!"
    else:#if ssn is not 9 digits, find out what's wrong
        if re.search(r"[A-Za-z]", test_ssn):#look for alpha characters in SSN using regular expressions
            print "Contains alpha characters: {0}".format(test_ssn)
        elif len(test_ssn) != 9:#check length
            print "Wrong length. Length of {1} is {0}".format(len(test_ssn), test_ssn)
        else:#everything else that can go wrong!
            print "Something else weird. I dunno. Here's the SSN: {0}".format(test_ssn)
