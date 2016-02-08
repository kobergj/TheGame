# Difficult File. Split print commands from calling functions?


def Arrive(Planet, Player):
    while True:

        print "\n You are at Planet %s" % Planet.Name
        print "Goods Produced: %s" % Planet.goodsProduced
        print "Goods Consumed: %s" % Planet.goodsConsumed
        print "Possible Actions:"
        print "[0] quit game"
        print "[1] buy goods"
        print "[2] sell goods"
        print "[3] depart"

        choice = input()

        if choice == 0:
            return 'quit'

        elif choice == 1:
            BuyGoods(Planet, Player)

        elif choice == 2:
            SellGoods(Planet, Player)

        elif choice == 3:
            next_dest_name = ChooseDestination(Planet, Player)
            return next_dest_name

        else:
            print 'Sorry, %s not valid' % choice
            choice = input()


def ChooseDestination(Planet, Player):
    print "\n Choose Destination"

    i = 1
    destList = list()
    for destination in Planet.distances:
        print "[%s] %s, distance: %s" % (i, destination, Planet.distances[destination])
        i += 1
        destList.append(destination)

    choice = input()

    next_dest = destList[choice-1]

    return next_dest


def BuyGoods(Planet, Player):
    i = 1
    print '\n Possiblities:'
    print "[0] Buy Nothing"
    for good in Planet.goodsProduced:
        print "[%s] buy %s" % (i, good)
        i += 1

    choice = input()

    good_to_buy = Planet.goodsProduced[choice-1]

    print 'Bought %s' % good_to_buy


def SellGoods(Planet, Player):
    i = 1
    print '\n Possiblities:'
    print "[0] sell Nothing"
    for good in Planet.goodsConsumed:
        print "[%s] sell %s" % (i, good)
        i += 1

    choice = input()

    good_to_sell = Planet.goodsConsumed[choice-1]

    print 'Sold %s' % good_to_sell
