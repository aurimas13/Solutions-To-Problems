class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        for i, ticket in enumerate(tickets):
            if i <= k:
                time += min(ticket, tickets[k])
            else:
                time += min(ticket, tickets[k] - 1)
        return time
