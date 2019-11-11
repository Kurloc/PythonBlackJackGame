import random
import sys
import time
from Bank import PlayerBank

card_libary = {
    'H': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
    'C': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
    'S': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
    'D': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
}



class BlackJackGame():
    deck = []
    gamehands = {'dealer': [],
                 'player': []}
    playercash = 0
    username = ""
    password = ""
    
    def __init__(self):
        pass
    def create_game_deck(self):
        spadecount = 0
        clubcount = 0
        heartcount = 0
        diamondcount = 0
        counter = 0
        deck = []
        lastcardspot = ''
        for i in card_libary:
            count =+ 1
            for z in card_libary[i]:
                counter = counter + 1
                suites = ['H','C','S','D']
                cardspot = random.randint(0,counter)
                if cardspot == lastcardspot:
                    cardspot = random.randint(0,counter)
                else:
                    pass
                cardname = str(i) + ' - ' + str(z) 
                deck.insert(cardspot,cardname)
                lastcardspot = cardspot
        return deck
    
    def pull_cards(self, deck, StartingHand, WhomsHand):
        gamehands = self.gamehands
        gamedeck = deck
        WhomsHand = WhomsHand.lower()
        if StartingHand == True:
            for z in range(2):
                gamehands['player'].append(gamedeck[0])
                gamedeck.pop(0)
            for z in range(2):
                gamehands['dealer'].append(gamedeck[0])
                gamedeck.pop(0)
            print('\n')
        else:
            for z in range(1):
                gamedeck.pop(0)
            print('\n')   
        return gamedeck
        
        
    def fetch_player_bet(self, username, password):
        playercash = z.get_current_player_cash(username, password)
        return username, password, playercash
        
    def start_game(self, playercash):
        playerhand = []
        print('\n')
        while True:
            try:
                pbet = int(input('You have $' + str(playercash[2]) +' available. How much would you like to bet player?: '))
                testicle = int(playercash[2])
                if testicle < pbet:
                    1/0 
            except:
                for x in range(0): print('\n')
                print('Bet is greater than your current amount of cash. Or you did not enter a number!')
            else:
                for x in range(0): print('\n')
                print("Let's deal up!")
                break
        
        gamedeck = self.create_game_deck()
    
    ##dealer, dealerturn = true/false
    def count_cards(self, PKey, dealer, dealerturn):
        count3 = 0
        count2 = 0
        count = 0
        playercount3 = []
        if dealer == True:
            playercount = str(self.gamehands[PKey][0]).split(' - ') 
            playercount3.append(playercount[1])
        if dealer == False:
            if dealerturn == False:
                handcount = len(self.gamehands[PKey]) 
                for x in range(handcount):
                    count3 = int(x)
                    playercount = str(self.gamehands[PKey][count3]).split(' - ') 
                    playercount3.append(playercount[1])
            if dealerturn == True:    
                handcount = len(self.gamehands[PKey]) 
                for x in range(handcount):
                    count3 = int(x)
                    if count3 != 0:
                        playercount = str(self.gamehands[PKey][count3]).split(' - ') 
                        playercount3.append(playercount[1])
        
        for x in playercount3:
            if str(x) == 'Jack':
                count = count + 10 
                count2 = count2 + 10
            if str(x) == 'Queen':
                count = count + 10 
                count2 = count2 + 10 
            if str(x) == "King":
                count = count + 10 
                count2 = count2 + 10 
            if str(x) == 'Ace':
                count = count + 11 
                count2 = count2 + 1 
            if (x) == '1':
                count = count + 1
                count2 = count2 + 1 
            if (x) == '2':
                count = count + 2
                count2 = count2 + 2 
            if (x) == '3':
                count = count + 3
                count2 = count2 + 3 
            if (x) == '4':
                count = count + 4
                count2 = count2 + 4 
            if (x) == '5':
                count = count + 5
                count2 = count2 + 5 
            if (x) == '6':
                count = count + 6
                count2 = count2 + 6 
            if (x) == '7':
                count = count + 7
                count2 = count2 + 7
            if (x) == '8':
                count = count + 8
                count2 = count2 + 8 
            if (x) == '9':
                count = count + 9
                count2 = count2 + 9
            if (x) == '10':
                count = count + 10
                count2 = count2 + 10
                   
        return count,count2

    def clean_decks(self):
        self.deck = []
        self.gamehands = {'dealer': [],
                 'player': []}

playerinput = True       
b = BlackJackGame()
z = PlayerBank()
test = z.register_andor_login()
while playerinput == True:        
    b.clean_decks()
    deck = b.create_game_deck()
    b.fetch_player_bet(test[0], test[1])
    b.start_game(test)
    deck = b.pull_cards(deck, True, 'none')
    aa = b.count_cards('player', False, False)[0]
    cc = b.count_cards('dealer', False, False)[0] ## Real score
    while cc < 22 and aa < 22:
        while True:
            try:
                print('Dealers Cards: ',b.gamehands['dealer'], ' - Hand Values: ', cc)
                print('Player Cards: ',b.gamehands['player'], ' - Hand Value: ', aa)
                zz = int(input('Want a hit?: \n 1 for Yes\n 0 for No\n'))
                if zz > 1:
                    raise TypeError
            except:
                for x in range(100):print('\n')
                print('\nERROR!\n')
            else:
                    
                aa = b.count_cards('player', False, False)[0]
                cc = b.count_cards('dealer', False, False)[0] ## Real score
                target1 = 1
                target0 = 0
                
            if int(zz) == 1: 
                        pulledcard = str(deck[0]).split(' - ')
                        pulledacard = b.pull_cards(deck, False, 'players')
                        pulledcard = str(pulledcard[0]) + ' - ' + str(pulledcard[1])
                        cc = b.count_cards('dealer', False, False)[0]
                        aa = b.count_cards('player', False, False)[0]
                        b.gamehands['player'].append(pulledcard)
            if int(zz) == 0: 
                    pulledcard = str(deck[0]).split(' - ')
                    pulledacard = b.pull_cards(deck, False, 'dealer')
                    pulledcard = str(pulledcard[0]) + ' - ' + str(pulledcard[1])
                    aa = b.count_cards('player', False, False)[0]
                    cc = b.count_cards('dealer', False, False)[0]
                    b.gamehands['dealer'].append(pulledcard)
    
                
    print(b.gamehands)
    print('Game over!\nPlayer Score: ', aa, '\nDealer Score: ', cc)
    if (int(aa) >= 22):
        if int(aa) < int(cc):
            print('\nPlayer won!')
        if int(cc) < int(aa):
            print('\nDealer won!')
    if (int(cc) >= 22):
        if int(aa) < int(cc):
            print('\nPlayer won!')
        if int(cc) < int(aa):
            print('\nDealer won!')
    elif int(aa) == 21 or int(cc) == 21:
        if int(aa) == 21:
            print('\nPlayer won!')
        if int(cc) == 21:
            print('\nDealer won!')
    elif int(aa) < 21 or int(cc) < 21:
        if int(aa) > int(cc):
            print('\nPlayer won!')
        if int(cc) > int(aa):
            print('\nDealer won!')
    elif int(aa) == int(cc):
        print('House wins!')
            
            
    while True:
        try:
            target1 = 1
            target0 = 0
            playerinput = int(input('Want to go again chap?\n 1 for yes\n o for no'))
            if zz > 1:
                raise TypeError
        except:
            for x in range(100): print('\n')
            print('\nERROR!\n')
        else:
            playerinput == True
            break