wall = range(99, 0, -1)
for bottles in wall:
    print "{0} bottles of beer on the wall, {0} bottles of beer".format(bottles)
    print "if one of those bottles should happen to fall,  {0} bottles of beer on the wall".format((bottles-1))

    
