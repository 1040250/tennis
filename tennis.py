#!/usr/bin/env python
"""
Simulates tennis matches for any number of winning sets.
Takes number of matches to be simulated and probability of player A making any given point.
Returns portion of matches won by player A as well as other stats.
"""

__author__ = "MJ"

from numpy.random import choice as pick_winner

# Set variables here
sets_to_win = 3     # Number of sets needed to win the match
n_matches = 1000    # Number of matches to be simulated
quali_A = 0.51      # Probability of player A making any given point (same for serve and return)
quali_adj = 0       # Reduces probability of scoring by this many percentage points per point player is in the lead

def tennis():
    matchesA, matchesB, sets, points, pointsA, pointsB, games, sets, tiebreaks = 0, 0, 0, 0, 0, 0, 0, 0, 0
    for n in range(n_matches):  # Start a new MATCH
        setsA, setsB = 0, 0     # Start match with zero sets each
        while max([setsA, setsB]) < sets_to_win:  # Start new SET
            gamesA, gamesB = 0, 0                 # Start set with zero games each
            # Start new GAME if
            # ...no player has won six of them or if
            # ...one player has won six but the other one has won five
            # Or start tie-break if the score is 6:6 games
            while (max([gamesA, gamesB]) < 7 and min([gamesA, gamesB]) > 4) or max([gamesA, gamesB]) < 6:
                pointsA, pointsB = 0, 0           # Start game / tie-break with zero points each
                target = 7 if gamesA == 6 and gamesB == 6 else 4  # Play seven-point tie-break at 6:6 games
                # Play points as long as no play has won enough of them or does not have a two-point lead yet
                while max([pointsA, pointsB]) < target or abs(pointsA - pointsB) < 2:
                    winner_of_point = pick_winner(['A', 'B'], p=[quali_A, 1 - quali_A])      # Play the point, finally
                    if winner_of_point == 'A':
                        pointsA += 1
                    else:
                        pointsB += 1
                    points += 1  # Point counter
                if pointsA > pointsB:
                    gamesA += 1
                elif pointsA < pointsB:
                    gamesB += 1
                games += 1  # Game counter
                if target == 7:
                    tiebreaks += 1  # Tie-break counter
            if gamesA > gamesB:
                setsA += 1
            else:
                setsB += 1
            sets += 1  # Set counter
        if setsA > setsB:
            matchesA += 1
        else:
            matchesB += 1

    print(f'{"Wins for A":.<20}{matchesA / n_matches * 100: .1f} %')
    print(f'{"Points/game":.<20}{points / games: .2f}')
    print(f'{"Points/set":.<20}{points / sets: .2f}')
    print(f'{"Games/set":.<20}{games / sets: .2f}')
    print(f'{"Games/match":.<20}{games / n_matches: .2f}')
    print(f'{"Sets/match":.<20}{sets / n_matches: .2f}')
    print(f'{"Tie-breaks/match":.<20}{tiebreaks / n_matches: .2f}')
    print(f'{"Points played":.<20}{points/1e6: ,.3f} M')


if __name__ == '__main__':
    tennis()

