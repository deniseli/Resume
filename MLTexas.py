# This script deals with suitless hands in Texas Hold'em.  If you
# are looking for a Texas Hold'em hand analyzer, congratulations!
# You've come to the right file.  If you were looking to analyze
# hands for some other kind of poker, then you're shit out of luck.
#
# Denise Li 2013
#
import math
import random
import itertools
from sets import Set


def cardsEqual(card1, card2):
    return card1[0] == card2[0] and card1[1] == card2[1]


def drawCard():
    card = plaindeck[random.randint(0,len(plaindeck)-1)]
    plaindeck.remove(card)
    return card


def printDecks():
    print '\n\n' + str(plaindeck)
    print '\n\n' + str(deckBySuit)
    print '\n\n' + str(deckByVal)
    return 0

# Poker Hands from BEST to WORST:
### 0 Royal Flush........(I)0,        (I)0
### 1 Straight Flush.....(I)highcard, (I)0
### 2 Four of a Kind.....(I)value,    (I)0
### 3 Full House.........(I)3value,   (I)2value
### 4 Flush..............(I)highcard, (I)0
### 5 Straight...........(I)highcard, (I)0
### 6 Three of a Kind....(I)value,    (I)0
### 7 Two Pair...........(I)highpair, (I)lowpair
### 8 One Pair...........(I)value,    (I)highcard
### 9 High Card..........(I)value,    (I)0
#Return rank (above) and (int(rank), int, int)
def checkHand(cards):
    sCount = [0, 0, 0, 0]
    vCount = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    highCard = 2
    # sCount, vCount, highcard found
    for i in range(5):
        if cards[i][0] == 'C':
            sCount[0]+=1
        elif cards[i][0] == 'D':
            sCount[1]+=1
        elif cards[i][0] == 'H':
            sCount[2]+=1
        elif cards[i][0] == 'S':
            sCount[3]+=1
        vCount[cards[i][1]-2]+=1
        if cards[i][1] > highCard:
            highCard = cards[i][1]
    # isFlush found
    isFlush = sCount[0] == 4 or sCount[1] == 4 or sCount[2] == 4 or sCount[3] == 4
    # flush highcard found
    if isFlush:
        highCard = 2
        for card in cards:
            if card[0] == 'C' and sCount[0] == 4 and card[1] > highCard:
                highCard = card[1]
            if card[0] == 'D' and sCount[1] == 4 and card[1] > highCard:
                highCard = card[1]
            if card[0] == 'H' and sCount[2] == 4 and card[1] > highCard:
                highCard = card[1]
            if card[0] == 'S' and sCount[3] == 4 and card[1] > highCard:
                highCard = card[1]
    # isStraight is -1 if not a straight, else the highest card
    isStraight = -1
    for i in range(9):
        if vCount[i]!=0 and vCount[i+1]!=0 and vCount[i+2]!=0:
            if vCount[i+3]!=0 and vCount[i+4]!=0:
                isStraight = i+6
    # isQuad is -1 if no quads, else the quad's value
    # isTriple is -1 if no triples, else the triple's value
    # isPair is [-1, -1] if no pairs exist,
    # else highest pair in isPair[0], next highest pair (if exists) in isPair[1]
    isQuad = -1
    isTriple = -1
    isPair = [-1,-1]
    for i in range(12):
        if vCount[i] == 4:
            isQuad = i+2
        if vCount[i] == 3:
            isTriple = i+2
        if vCount[i] == 2:
            isPair[1] = isPair[0]
            isPair[0] = i+2
    # royal flush
    if isFlush and isStraight == 14:
        return (0, 0, 0)
    # straight flush
    if isFlush and isStraight != -1:
        return (1, isStraight, 0)
    # four of a kind
    if isQuad != -1:
        return (2, isQuad, 0)
    # full house
    if isTriple != -1 and isPair[0] != -1:
        return (3, isTriple, isPair[0])
    # flush
    if isFlush:
        return (4, highCard, 0)
    # straight
    if isStraight != -1:
        return (5, isStraight, 0)
    # three of a kind
    if isTriple != -1:
        return (6, isTriple, 0)
    # two pair
    if isPair[0] != -1 and isPair[1] != -1:
        return (7, isPair[0], isPair[1])
    # pair
    if isPair[0] != -1:
        return (8, isPair[0], highCard)
    # high card
    return (9, highCard, 0)


# given hands a and b, returns:
#   1 for a's win
#   0 for b's win
# 0.5 for split pot
def compareHands(a, b):
    #dif ranks
    if a[0] != b[0]:
        return 1 if a < b else 0
    # same ranks
    if a[1] == b[1]:
        if a[2] == b[2]:
            return .5
        return 1 if a[2] > b[2] else 0
    return 1 if a[1] > b[1] else 0


# given 7 cards, return the best possible hand
def makeBestHand(cards):
    possHands = list(itertools.combinations(cards,5))
    while len(possHands) > 1:
        if compareHands(possHands[0], possHands[1]) == 1:
            possHands.remove(possHands[1])
        else:
            possHands.remove(possHands[0])
    return possHands[0]


#initialize deck
suits = ('C', 'D', 'H', 'S')
values = (2,3,4,5,6,7,8,9,10,11,12,13,14)
plaindeck = []
for s in suits:
    for v in values:
        plaindeck.append((s,v))

posspairs = []
for c1 in plaindeck:
    for c2 in plaindeck:
        if not cardsEqual(c1, c2) and set([c1, c2]) not in posspairs:
            posspairs.append(set([c1, c2]))

conf = {}
for p in posspairs:
    conf[frozenset(p)] = [1,2]

deal = []
oppDeal = []
hand = []
oppHand = []
win = 0
shared = []
bet = 0
totalGained = 0
totup = 0
totdown = 0
roundNum = 1
lastThouUp = 0
lastThouDown = 0
firstThouUp = 0
firstThouDown = 0
cf = 0

processLength = 100000
averageGains = []

for i in range(processLength):
    # deal
    deal.append(drawCard())
    deal.append(drawCard())
    oppDeal.append(drawCard())
    oppDeal.append(drawCard())
    # burn card
    burn = drawCard()
    # no flop, shows all 5 community cards at once
    for i in range(5):
        shared.append(drawCard())
    # find best hand for both players
    hand = makeBestHand(deal+shared)
    oppHand = makeBestHand(oppDeal+shared)
    # make bet
    cf = (-1/(1+math.pow(1.1,conf[frozenset(deal)][1])))+.5
    if conf[frozenset(deal)][0] / conf[frozenset(deal)][1] > .5:
        bet = 100 * cf * (conf[frozenset(deal)][0] / conf[frozenset(deal)][1])
    else:
        bet = 0
    # find winner
    win = compareHands(hand, oppHand)
    # reset confidences based on own hand
    conf[frozenset(deal)][0] += win
    conf[frozenset(deal)][1] += 1
    # reset confidences based on opponent's hand
    conf[frozenset(oppDeal)][0] += (1-win)
    conf[frozenset(oppDeal)][1] += 1
    # total gains / losses
    if win == 1:
        totalGained += bet
        totup += bet
        if roundNum >= processLength-(processLength/10):
            lastThouUp += bet
        if roundNum < processLength-(processLength/10):
            firstThouUp += bet
    if win == 0:
        totalGained -= bet
        totdown -= bet
        if roundNum >= processLength-(processLength/10):
            lastThouDown -= bet
        if roundNum > (processLength/10):
            firstThouDown -= bet
    # print details
#    print 'ROUND ' + str(roundNum)
#    print 'deal:    ' + str(deal)
#    print 'oppDeal: ' + str(oppDeal)
#    print 'shared:  ' + str(shared)
#    print 'best hand:      ' + str(hand)
#    print 'opps best hand: ' + str(oppHand)
#    print 'bet: ' + str(bet)
#    print 'won? ' + str(win)
#    print 'confidence on deal now:   ' + str(conf[frozenset(deal)][0]) + '/' + str(conf[frozenset(deal)][1])
#    print 'total gains and losses:   ' + str(totalGained)
#    print 'average gained per round: ' + str((totalGained/(roundNum))) + '\n\n'
    # add to stats
    if (roundNum) % (processLength/10) == 0:
        averageGains.append(totalGained/(roundNum))
        print 'reached ' + str(roundNum)
    # remake deck, reset values
    roundNum += 1
    plaindeck.extend(deal)
    plaindeck.extend(oppDeal)
    plaindeck.extend(shared)
    plaindeck.append(burn)
    deal = []
    oppDeal = []
    hand = []
    oppHand = []
    shared = []

averageGains.append(totalGained/(roundNum))

# statistics and analysis
print '\nAverage gains over time'
print '\t\tTime\tAverage Gain\tDifference'
for i in range(11):
    diff = ''
    if i is not 0:
        diff = str(averageGains[i] - averageGains[i-1])
    print 'From time\t' + str(i * (processLength/10)) + '\t' + str(averageGains[i]) + '\t' + diff
print '\ntotal gained:    ' + str(totup)
print 'total lost:      ' + str(totdown)
print 'gain/loss ratio: ' + str(-1*totup/totdown) + '\n'
print 'gains in last 10%:           ' + str(lastThouUp)
print 'losses in last 10%:          ' + str(lastThouDown)
print 'gain/loss ratio in last 10%: ' + str(-1*lastThouUp/lastThouDown) + '\n'
print 'gains in first 10%:           ' + str(firstThouUp)
print 'losses in first 10%:          ' + str(firstThouDown)
print 'gain/loss ratio in first 10%: ' + str(-1*firstThouUp/firstThouDown) + '\n'
