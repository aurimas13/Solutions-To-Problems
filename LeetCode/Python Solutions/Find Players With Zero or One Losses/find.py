class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Initialize sets for players with no losses and exactly one loss
        no_losses = set()
        one_loss = set()

        # Dictionary to keep track of the number of losses for each player
        loss_count = {}

        for winner, loser in matches:
            # Add winner to no_losses set (since they haven't lost)
            no_losses.add(winner)

            # Update loss count for the loser
            if loser in loss_count:
                loss_count[loser] += 1
                # If a player's loss count reaches 2, remove them from one_loss
                if loss_count[loser] == 2:
                    one_loss.discard(loser)
            else:
                # For first loss, add to one_loss and set loss_count to 1
                loss_count[loser] = 1
                one_loss.add(loser)

        # Remove players from no_losses who have lost any match
        for player in loss_count:
            no_losses.discard(player)

        # Return sorted lists of players with no losses and exactly one loss
        return [sorted(no_losses), sorted(one_loss)]
