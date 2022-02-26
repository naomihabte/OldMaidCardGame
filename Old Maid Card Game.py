
import random

def attend_le_joueur():
    '''()->None
    Pauses programme until player clicks enter
    '''
    try:
         input("Press enter to continue. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Returns a list of character chaines that represent all cards,
        except the black jack.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') 
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Mix the list that represents the card packet     
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns 2 lists that represents the 2 hands of cards.  
     Dealer gives a card to the other, one to himself,
     continues until the end of packet p.
     ''' 
     donneur=[]
     autre=[]
     var = 1

     for i in range (len(p)):
         if var==0:
             donneur.append(p[i])
             var=1
         elif var==1:
             autre.append(p[i])
             var=0
     
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Returns a copy of list l with all pairs eliminated
     and mix the remaining elements.

     Test:
     (Note that the order of the elements in the result could be different)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    resultat=[]
    if len(l)<2:
        return l
    l.sort()
    l.append([''])
    x=1
    while x < len(l):
        if l[x-1][:-1] != l[x][:-1]:
            resultat.append(l[x-1])
            x+=1
        else:
            x+=2
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Displays the elements of the list p separated by spaces
    '''
    print(' '.join(p))

    
def entrez_position_valide(n):
     '''
     (int)->int
     Returns an integer from the keyboard, from 1 to n (1 and n inclusive).
     Keep asking if the user enters an integer that is not in the range [1,n]
     
     Precondition: n>=1
     '''

     x = int(input("Please enter a value from 1 to "+str(n)+": "))
     if n>= x >=1:
         return x
     else:
         while True:
             x = int(input("Inalid position. Please enter a position from 1 to "+str(n)+": "))
             if n>= x >=1:
                 return x
             else:
                 continue
                

def joue():
     '''()->None
     This plays the game'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Hello. My name is Robot and I deal the cards.")
     print("Your hand is:")
     affiche_cartes(humain)
     print("Don't worry, I can't see your cards or their order.")
     print("Now discard all pairs from your hand. I will do it too.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     tour=0

     while 1 >= tour >= 0:
         if len(humain) == 0:
             print ('**********************************')
             print ("I have completed all the cards.")
             print ("Congratulations! You, Human, have won.")
             break
         elif len (donneur) == 0:
             print ('**********************************')
             print ("I have completed all the cards.")
             print ("You have lost! I, Robot, have won.")
             break
         else:
             if tour == 0:
                 print ('**********************************')
                 print ("Your turn")
                 print ("Your hand is:")
                 affiche_cartes(humain)
                 n = len(donneur)
                 print ("I have", n, "cards. If 1 is the position of my first card and\n", str(n), " the position of my last card, which of my cards do you want?") 
                 user_inpt = entrez_position_valide(n)
                 print ("You have asked for card #", str(user_inpt))
                 print ("There it is. it's", donneur[int(user_inpt)-1])
                 print ("With ", donneur[int(user_inpt)-1], " added, your hand is:")
                 humain.append(donneur[int(user_inpt)-1])
                 donneur.remove(donneur[int(user_inpt)-1])
                 affiche_cartes(humain)
                 print("After discarding all pairs and shuffling the cards, your hand is:")
                 humain = elimine_paires(humain)
                 affiche_cartes(humain)
                 tour = 1
                 attend_le_joueur()
             elif tour == 1:
                 print ('**********************************')
                 print("My turn")
                 n = len(humain)
                 robot_inpt = random.randint(1,n)
                 print ("I took your card #", str(robot_inpt))
                 donneur.append(humain[int(robot_inpt)-1])
                 humain.remove(humain[int(robot_inpt)-1])
                 donneur = elimine_paires(donneur)
                 tour = 0
                 attend_le_joueur()
            
                 
joue()
