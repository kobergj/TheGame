def planetArrival(Planet, Player):
    print "\n You are at Planet %s" % Planet.Name
    print "Goods Produced: %s" % Planet.goodsProduced
    print "Goods Consumed: %s" % Planet.goodsConsumed
    print "Possible Actions:"
    print "[0] quit game"
    print "[1] buy goods"
    print "[2] sell goods"
    print "[3] depart"

    choice = input()

    return choice


def invalidChoice(choice):
    print 'Sorry, %s not valid' % choice
    choice = input()
