
class PlayerScore:
    def __init__(self, id, roundScores):
        self.id = id
        self.roundScores = roundScores

playerScores = [
    PlayerScore(5, [1, 1, 1, 0]),
    PlayerScore(2, [-2, -1, -1, -1]),
    PlayerScore(6, None),
    PlayerScore(3, [0, 0, -2, -1]),
    PlayerScore(4, [0, 0, -1, -1]),
    PlayerScore(1, [1, 0, -2, -1])
    ]

class PlayerName:
    def __init__(self, id, name):
        self.id = id
        self.name = name

playerNames = [
    PlayerName(4, "Bob"),
    PlayerName(5, "Ann"),
    PlayerName(1, "Joe"),
    PlayerName(2, "Sue"),
    PlayerName(3, "Jane"),
    PlayerName(6, "Larry")
    ]

class LeaderBoard:
    def __init__(self, id, name, score, winner):
        self.id = id
        self.name = name
        self.score = score
        self.winner = winner

expectedLeaderboard = [
    LeaderBoard(3, "Jane", -3, False),
    LeaderBoard(2, "Sue", -5, True),
    LeaderBoard(4, "Bob", -2, False),
    LeaderBoard(5, "Ann", 3, False),
    LeaderBoard(1, "Joe", -2, False)
    ]
expectedLeaderboard.sort(key=lambda x: x.score)

# Function: get_leaderboard()
#
# Matches players with scores to provide a leaderboard sorted(ascending) by the sum of the roundScores
# and determines a winner based on the lowest score.
# If roundScores is null or empty for a player, then that player is not included in the results.
#
# Returns: List of LeaderBoard objects, sorted(ascending) by score
def get_leaderboard(playerNames, playerScores):
    leaderBoards = []
    for name in playerNames:
        for score in playerScores:
            if name.id == score.id:
                if score.roundScores != None or score.roundScores == []:
                    leaderBoards.append(LeaderBoard(name.id, name.name, sum(score.roundScores), False))
                break
    leaderBoards.sort(key=lambda x: x.score)
    leaderBoards[0].winner = True
    return leaderBoards

# Function: run_test()
#
# Compares 2 lists of LeaderBoard objects. Sort order matters.
#
# Returns: True if they match, false otherwise
def run_test(actualLeaderboard, expectedLeaderboard):
    if actualLeaderboard == None or actualLeaderboard == []: return False
    if len(actualLeaderboard) != len(expectedLeaderboard): return False
    for index, leaderboard in enumerate(actualLeaderboard):
        if leaderboard.id != expectedLeaderboard[index].id: return False
        if leaderboard.name != expectedLeaderboard[index].name: return False
        if leaderboard.score != expectedLeaderboard[index].score: return False
        if leaderboard.winner != expectedLeaderboard[index].winner: return False
    return True

# Function: print_leaderboard()
#
# Print to screen a list of LeaderBoard objects. Highlighting the winner.
#
# Returns: void
def print_leaderboard(leaderboard):
    for player in leaderboard:
        if player.winner:
            print('id: {} name: {} score: {} {}'.format(player.id, player.name, player.score, "WINNER"))
        else:
            print('id: {} name: {} score: {}'.format(player.id, player.name, player.score))

actualLeaderboard = get_leaderboard(playerNames, playerScores)
result = run_test(actualLeaderboard, expectedLeaderboard)
if result == True: 
    print("Test (1) passed.")
    print_leaderboard(actualLeaderboard)
else: print("Test (1) failed.")




