# Goal 1
bread = 4
pb = 3
jelly = 10
sandwich = 0

while bread >= 2 and pb >= 1 and jelly >= 1:
    sandwich = sandwich + 1
    print "I am making sandwich number {0}".format(sandwich)
    bread = bread - 2
    pb = pb - 1
    jelly = jelly - 1
print "All done! I made {0} sandwich(es)".format(sandwich)

# Goal 2
bread = 10
pb = 10
jelly = 4
sandwich = 0
ran_out = [""]

while bread >= 2 and pb >= 1 and jelly >= 1:
    sandwich = sandwich + 1
    print "I am making sandwich number {0}".format(sandwich)
    bread = bread - 2
    pb = pb - 1
    jelly = jelly - 1
    print "I have enough bread for {0} sandwiches, enough pb for {0} sandwiches, and enough jelly for {0} sandwiches".format(bread/2,pb,jelly)
if bread == 0:
    ran_out.append("bread")
if pb == 0:
    ran_out.append("pb")
if jelly == 0:
    ran_out.append("jelly")
print "All done! I made {0} sandwich(es) and ran out of {1}".format(sandwich, ran_out[1:])
