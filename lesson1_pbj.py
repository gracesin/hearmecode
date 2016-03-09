# Peanut Butter Jelly Time!

#confession: I snuck into lesson 2 without going to lesson 1 first. Nearly a year later, I'm doing this mostly for posterity, and so I actually remember this exercise when I TA...


##Trying one big happy program
pb = 2
bread = 4
jelly = 3

if pb > 0 and bread/2 > 0 and jelly > 0:
    print "I can make a sandwich!"#goal 1
    print "Now let's figure out how many sandwiches I can make"#goal 2
    if pb <= jelly and pb <= bread/2:
        print "Number of sandwiches I can make: {0}".format(pb)
    elif jelly <= pb and jelly <= bread/2:
        print "Number of sandwiches I can make: {0}".format(jelly)
    elif bread/2 <= pb and bread/2 <= jelly:
        print "Number of sandwiches I can make: {0}".format(bread/2)
    else:
        print "I think I accounted for all possibilities and there's no way this would ever print. Hope so!"
    print "If I use the min function, I can do this in one line without all these crazy ifs."
    print "It looks like min(pb, jelly, bread/2)"
    print "Number of sandwiches I can make: {0}".format(min(pb, jelly, bread/2))
elif bread%2 == 1 and pb > 0 and jelly > 0:
    print "I can make an open-faced PB&J sandwich, at least"#goal 3
elif (pb + jelly > 0) or bread > 1:#goal 4
    if bread <= 1:
        print "I need bread"
    if pb == 0:
        print "I need pb"
    if jelly ==  0:
        print "I need jelly"
elif bread > 0 and pb > 0 and jelly == 0:
    if bread%2 > 0:
        print "No jelly, but I can have a sad, sad peanut butter sandwich"#goal 5
    else:#just for kicks
        print "I can have a pitiful open-faced peanut butter sandwich at least"#can't lie, I've done this. Not bad toasted.
else:
    print "No sandwiches for me! Total ingredients: {0}".format(pb + jelly + bread/2)
    print "That line had better say we have zero ingredients."


#Going goal by goal
# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
pb = 2
bread = 4
jelly = 3

if pb > 0 and bread/2 > 0 and jelly > 0:
    print "I can make a sandwich!"
    lunch = True
else:
    print "No sandwiches for me!"

# Second Goal: Create a program to tell you: if you can make a sandwich, how many you can make
if lunch == True:
    if pb <= jelly and pb <= bread/2:
        print "Number of sandwiches I can make: {0}".format(pb)
    elif jelly <= pb and jelly <= bread/2:
        print "Number of sandwiches I can make: {0}".format(jelly)
    elif bread/2 <= pb and bread/2 <= jelly:
        print "Number of sandwiches I can make: {0}".format(bread/2)
    else:
        print "I think I accounted for all possibilities and there's no way this would ever print. Hope so!"
else:
    print "No lunch for me"
#moved to the end
#else:
    #print "No sandwiches for you!"
# Third Goal: Create a program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )
if bread%2 == 1 and pb > 0 and jelly > 0:
    print "I can make an open-faced sandwich, at least"
else:
    print "No sandwiches for me!"
# Fourth Goal: Create a program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches
if pb == 0 and bread/2 == 0 and jelly == 0:
    print "Time to go shopping. I need everything!"
elif pb > 0 or jelly > 0 or bread > 0:
    if bread <= 1:
        print "I need bread"
    if pb == 0:
        print "I need pb"
    if jelly ==  0:
        print "I need jelly"
else:
    print "I think I accounted for all possibilities and there's no way this would ever print. Hope so!"

# Fifth Goal: Create a program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.
if bread/2 > 0 and pb > 0 and jelly == 0:
    print "No jelly, but I can have a sad, sad peanut butter sandwich"


#oops, for goal 4, I assumed I was trying to make the maximum number of sandwiches, not just *a* sandwich
#here's how I did it. This is so much easier if you know about max or loops!
if pb == 0 and bread/2 == 0 and jelly == 0:
    print "Time to go shopping. I need everything!"
elif pb == jelly == bread/2:
    print "I miraculously have just the right amount of stuff to make {0} sandwich(es) with no leftover ingredients".format(pb)
else:
    if jelly < pb or jelly < bread/2:
        print "I need jelly"
    if pb < jelly or pb < bread/2:
        print "I need pb if I'm going to make the maximum possible number of sandwiches"
    if bread/2 < pb or bread/2 < jelly:
        print "I need bread if I'm going to make the maximum possible number of sandwiches"






# What are the step-by-steps to recreate this?
# First, you need variables to store your information.  Remember, variables are just containers for your information that you give a name.

# You need three ingredients to make a PB&J, so you'll want three different variables:
# 		How much bread do you have? (make this a number that reflects how many slices of bread you have)
#		How much peanut butter do you have? (make this a number that reflects how many sandwiches-worth of peanut butter you have)
#		How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)

# For this exercise, we'll assume you have the requisite tools (plate, knife, etc)

# Once you've defined your variables that tell you how much of each ingredient you have, use conditionals to test whether you have the right amount of ingredients

# Based on the results of that conditional, display a message.

# To satisfy the first goal:
#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
#		If you don't; print a message like "Looks like I don't have a lunch today"

# To satisfy the second goal:
#		Continue from the first goal, and add:
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before
#   To calculate which ingredient you have the least of, the min() function will be useful.
#   min() will calculate the smallest number of all of the numbers in the parentheses and tell you which it is
#   For example, min(4, 83, 6) will return 4

# To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01_(basics)/simple_math.py

# To satisfy the fourth goal:
#		Continue from the third goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches

# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.
