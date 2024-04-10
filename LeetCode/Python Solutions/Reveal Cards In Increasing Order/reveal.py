from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort(reverse=True)
        revealOrder = deque()
        
        for card in deck:
            if revealOrder:
                revealOrder.appendleft(revealOrder.pop())
            revealOrder.appendleft(card)
            
        return list(revealOrder)
