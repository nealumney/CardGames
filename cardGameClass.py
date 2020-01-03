# This is an abstract Class
# game implementation is dependent upon the inheriting classes
# This Class implements a deck of card
# provides a basic implementation in trms of title
# provides:
#   dealCard() returns file_name (name of card), value, randomly selected
#   initialises the playing surface
#   New Game Button calls newGame
#   Deal button (can be given other name e.g."twist") calls dealCard()
#
#
from tkinter import *
from random import choice, randint


class CardGame:
    # suits
    saved_clubs = [["ace_of_clubs", 11], ["2_of_clubs", 2], ["3_of_clubs", 3], ["4_of_clubs", 4], ["5_of_clubs", 5],
             ["6_of_clubs", 6],
             ["7_of_clubs", 7], ["8_of_clubs", 8], ["9_of_clubs", 9], ["10_of_clubs", 10], ["jack_of_clubs", 10],
             ["queen_of_clubs", 10], ["king_of_clubs", 10]
             ]
    saved_hearts = [["ace_of_hearts", 11], ["2_of_hearts", 2], ["3_of_hearts", 3], ["4_of_hearts", 4], ["5_of_hearts", 5],
              ["6_of_hearts", 6], ["7_of_hearts", 7], ["8_of_hearts", 8], ["9_of_hearts", 9], ["10_of_hearts", 10],
              ["jack_of_hearts", 10], ["queen_of_hearts", 10], ["king_of_hearts", 10]
              ]
    saved_diamonds = [["ace_of_diamonds", 11], ["2_of_diamonds", 2], ["3_of_diamonds", 3], ["4_of_diamonds", 4],
                ["5_of_diamonds", 5],
                ["6_of_diamonds", 6], ["7_of_diamonds", 7], ["8_of_diamonds", 8], ["9_of_diamonds", 9],
                ["10_of_diamonds", 10],
                ["jack_of_diamonds", 10], ["queen_of_diamonds", 10], ["king_of_diamonds", 10]
                ]
    saved_spades = [["ace_of_spades", 11], ["2_of_spades", 2], ["3_of_spades", 3], ["4_of_spades", 4], ["5_of_spades", 5],
              ["6_of_spades", 6], ["7_of_spades", 7], ["8_of_spades", 8], ["9_of_spades", 9], ["10_of_spades", 10],
              ["jack_of_spades", 10], ["queen_of_spades", 10], ["king_of_spades", 10]
              ]

    # the suits can be implemented by inheriting deck below, or by overiding deck to choose a different mix o suits.

    # deck = [clubs, hearts, diamonds, spades]

    def __init__(self, gui, imgPath, gameTitle = "Basic Game", numCards = 6 ):
        self.game = gui
        self.game.title(gameTitle)

        self.imgPath = imgPath
        self.cardBack = PhotoImage(file=self.imgPath + "cardBack.png")  # should be modifiable

        # required arrays and instance variables
        self.numCards = numCards
        self.playerImages = [None] * self.numCards  # Tkinter PhotoImage objects
        self.dealerImages = [None] * self.numCards
        self.playerScores = [None] * self.numCards  # value of each card drawn
        self.dealerScores = [None] * self.numCards
        self.playerCardLabels = [None] * self.numCards  # where each card image is stored
        self.dealerCardLabels = [None] * self.numCards
        self.playerScore = 0  # running scores
        self.dealerScore = 0
        # self.newGame should be over-ridden in the implementing class

        self.game.geometry(str(125*numCards)+"x500+100+100")
        # Title label
        l1 = Label(self.game, bg="green", borderwidth=2, relief="groove",
                   text="This is BlackJack, well a NOT bad go at it", )
        l1.grid(row=0, column=0, columnspan=10)

        # basic buttons
        dealButton = Button(self.game, text="Twist", width=10, command=self.deal)
        dealButton.grid(column=0, row=5, pady=1)
        stickButton = Button(self.game, text="Stick", width=10, command=self.stick)
        stickButton.grid(column=1, row=5, pady=1)
        newGameButton = Button(self.game, text="New Game", width=10, command=self.newGame)
        newGameButton.grid(column=2, row=5)
        exitButton = Button(self.game, text="End Game", width=10, command=self.exit)
        exitButton.grid(column=3, row=5)

    def getCard(self):
        suit = choice(self.deck)
        file, score = suit.pop(randint(0, len(suit)-1))
        # print(file, score)
        return(file, score)

    def youLostLabel(self, col):
        # col = empty column
        Label(self.game, text="I'm sorry you lost\n want to try again?").grid(column=col, row=3)


    def deal(self):
        pass

    def stick(self):
        pass

    def newGame(self):
        # create / reset the pack
        self.clubs=[]
        for card in self.saved_clubs:
            self.clubs.append(card)
        self.hearts = []
        for card in self.saved_hearts:
            self.hearts.append(card)
        self.diamonds = []
        for card in self.saved_diamonds:
            self.diamonds.append(card)
        self.spades = []
        for card in self.saved_spades:
            self.spades.append(card)
        # print(len(self.clubs), len(self.diamonds), len(self.spades), len(self.hearts))
        self.deck = [self.clubs, self.hearts, self.diamonds, self.spades]
        self.playerImages = [None] * self.numCards  # Tkinter PhotoImage objects
        self.dealerImages = [None] * self.numCards
        self.playerScores = [None] * self.numCards  # value of each card drawn
        self.dealerScores = [None] * self.numCards
        self.playerCardLabels = [None] * self.numCards  # where each card image is stored
        self.dealerCardLabels = [None] * self.numCards
        self.playerScore = 0  # running scores
        self.dealerScore = 0

        # set up basic game environment
        for i in range(self.numCards):
            self.playerCardLabels[i] = Label(self.game, borderwidth=2, relief="groove",
                                             text="", width=16, height=12)
            self.playerCardLabels[i].grid(column=i, row=3)
            self.dealerCardLabels[i] = Label(self.game, borderwidth=2, relief="groove",
                                             text="", width=16, height=12)
            self.dealerCardLabels[i].grid(column=i, row=4)

    def getScore(self, scoresList):
        score = 0
        ace = False
        for s in scoresList:
            if s:
                # print(s)
                score = score + s
                if s == 11:
                    # print("we got an ace")
                    ace = True
        if score > 21 and ace == True:
            # print("now we subtract 10")
            score = score - 10
        return score


    def exit(self):
        self.game.destroy()


if __name__ == "__main__":

    game = Tk()
    cards = CardGame(game, imgPath = "/home/neal/Documents/Python oop/blackjack/Small_PNG/", numCards=6)
    '''
    images=[None]*2
    cardLabels=[None]*2
    for c in range(2):
        # file, score = self.getCard()
        images[c] = PhotoImage(file= "H:\My Documents\Year 12\pythonOOP\Playing Cards\Small_PNG\jack_of_diamonds.png")
        print(c, images[c])
        cardLabels[c] = Label(game, image = images[c], borderwidth=2, relief="groove")
        cardLabels[c].grid (column = c, row = 3)
        print(images, cardLabels)    '''

    game.mainloop()