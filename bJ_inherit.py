from cardGameClass import CardGame
from tkinter import *
from random import choice, randint
# still to fix (Ace can be 1 or 11 (eleven)
class BlackJack(CardGame):

    def __init__(self, game, imgPath = "Small_PNG/", gameTitle = "Basic Game",
                 numCards = 6):
        super().__init__(game, imgPath, gameTitle, numCards)
        self.newGame()

    def deal(self):
        # TODO: check that the user has NOT already won or lost!

        # Check twisting legal (<22)
        # need to get another card, display the card, find the new score, determine if game won or lost or ongoing
        for i in range(len(self.playerImages)-1):
            if self.playerImages[i]:
                continue
            else:
                if self.playerScore < 22:
                    # print(i)
                    file, self.playerScores[i] = self.getCard()
                    # print(len(self.clubs), len(self.diamonds), len(self.spades), len(self.hearts))
                    self.playerImages[i] = PhotoImage(file=self.imgPath + file + ".png")
                    self.playerCardLabels[i] = Label(self.game, image=self.playerImages[i], borderwidth=2, relief="groove")
                    self.playerCardLabels[i].grid(column=i, row=3)
                    self.playerScore = self.getScore(self.playerScores)
                    # self.playerScore = self.playerScore + int(self.playerScores[i])
                    if self.playerScore > 21:
                        self.youLostLabel(i+1)
                    self.scoreLabel.config(text = "Player score is: {}".format(self.playerScore))
                    # print( self.getScore(self.playerScores))
                    return
                else:
                    self.youLostLabel(i+1)
                    return

    def stick(self):
        # find empty column in case of message need:
        for p in range(len(self.playerImages)-1):
            if self.playerImages[p]:
                #print(p)
                continue
            # i is the empty column
            break

        # check sticking is legal ( > 13)
        if self.playerScore > 13:
            # they can stick
            # turn over the dealers cards, show score
            self.dealerCardLabels[0].configure(image=self.dealerImages[0])
            self.dealerCardLabels[1].configure(image=self.dealerImages[1])

            # calculate the player score
            # get the dealer score
            d = 2
            while self.dealerScore < self.playerScore:
                file, self.dealerScores[d] = self.getCard()
                self.dealerImages[d] = PhotoImage(file=self.imgPath + file + ".png")
                self.dealerCardLabels[d] = Label(self.game, image=self.dealerImages[d], borderwidth=2, relief="groove")
                self.dealerCardLabels[d].grid(column=d, row=4)
                self.dealerScore = self.getScore(self.dealerScores)
                d=d+1
            self.dealerScoreLabel.configure(text="Dealer score is: {}".format(self.dealerScore))
            #    then dealer gets new card
            #    if dealerScore > playerScore AND dealerScore <= 21
            #        dealer wins
            if self.dealerScore > 21:
                # player has one
                winLoss = "won"
            else:
                winLoss = "Lost"

            message = "{}\n{}\n Player has {}".format(self.scoreLabel.cget("text"),self.dealerScoreLabel.cget("text"), winLoss)
            # print("p is: {}, d is {}".format(p,d))
            if p > d:
                Label(self.game,text=message).grid(column=d, row = 4)
            elif p == d:
                Label(self.game, text=message).grid(column=p, row=3)
            else:
                Label(self.game, text=message).grid(column=p, row=3
        )

        else:
            msg = "I'm sorry you must \nhave more than \n13 to stick"
            Label(self.game, text=msg).grid(column = p, row=3)  # player row is 3
            return

    def newGame(self):
        super().newGame()
        # deal the players first two cards
        for c in range(2):
            file, self.playerScores[c] = self.getCard()
            self.playerImages[c] = PhotoImage(file=self.imgPath + file + ".png")
            # print(self.imgPath+file+".png")
            self.playerCardLabels[c] = Label(self.game, image=self.playerImages[c], borderwidth=2, relief="groove")
            self.playerCardLabels[c].grid(column=c, row=3)
            self.playerScore = self.getScore(self.playerScores)
        self.scoreLabel = Label(self.game, text="Player score is: {}".format(self.playerScore), borderwidth=2,
                                relief="groove")
        self.scoreLabel.grid(row=8, column=1)
        # print(self.playerScores)
        # print(self.getScore(self.playerScores))
        # Now deal the dealers cards and display the backs of the cards.
        for d in range(2):
            file, self.dealerScores[d] = self.getCard()
            self.dealerImages[d] = PhotoImage(file=self.imgPath + file + ".png")
            self.dealerCardLabels[d] = Label(self.game, image=self.cardBack, borderwidth=2, relief="groove")
            # cardLabels[c] = Label(self.game, text=file+" "+str(scores[c]), borderwidth=2, relief="groove")
            self.dealerCardLabels[d].grid(column=d, row=4)
            self.dealerScore = self.getScore(self.dealerScores)
        self.dealerScoreLabel = Label(self.game,
                                      text="Dealer score is: {}".format(self.dealerScore),
                                      borderwidth=2, relief="groove")
        # self.dealerScoreLabel.grid(row=8, column=2)





# testing the game
if __name__ == "__main__":
    game = Tk()
    bj = BlackJack(game, gameTitle = "Inherited Game")

    game.mainloop()
