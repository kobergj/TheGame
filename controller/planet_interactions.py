def Arrive(Planet):
    print "\n You are at Planet %s" % Planet.Name
    print "Goods Produced: %s" % Planet.goodsProduced
    print "Goods Consumed: %s" % Planet.goodsConsumed
    print "Possible Actions:"
    print "[1] buy goods"
    print "[2] sell goods"
    print "[3] depart"

    choice = input()

    if choice == 3:
        next_dest = ChooseDestination()
        return next_dest
    elif choice == 2:
        SellGoods(Planet)
    elif choice == 1:
        BuyGoods(Planet)
    return


def ChooseDestination():
    print "\n Choose Destination"
    print "[1] Earth"
    print "[2] Mars"

    choice = input()

    return choice - 1


def BuyGoods(Planet):
    i = 1
    print '\n Possiblities:'
    print "[0] Buy Nothing"
    for good in Planet.goodsProduced:
        print "[%s] buy %s" % (i, good)

    choice = input()

    if choice == 0:
        Arrive(Planet)
    else:
        BuyGoods(Planet)


def SellGoods(Planet):
    print "Sorry, not implemented"
    Arrive(Planet)
