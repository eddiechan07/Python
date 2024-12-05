from . import card

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for suit in suits:
            for point_val in range(1,14):
                string_val = ""
                if point_val == 1:
                    string_val = "Ace"
                elif point_val == 11:
                    string_val = "Jack"
                elif point_val == 12:
                    string_val = "Queen"
                elif point_val == 13:
                    string_val = "King"
                else:
                    string_val = str(i)
                self.cards.append( card.Card( suit , point_val , string_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

