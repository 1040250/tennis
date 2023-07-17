#!/usr/bin/env python
"""
Simulates tennis matches for any number of winning sets.
Takes number of matches to be simulated and probability of player A making any given point.
Returns portion of matches won by player A as well as other stats.
"""

import random

sets_to_win = 3     # number of sets needed to win the match
n_matches = 10 ** 4 # number of matches to be simulated
quali_A = 0.51       # probability of player A making any given point (same for serve and return)
quali_adj = 0       # reduces probability of scoring by this many percentage points per point player is in the lead

def tennis():
    matchesA, matchesB, sets, points, pointsA, pointsB, games, sets, tiebreaks = 0, 0, 0, 0, 0, 0, 0, 0, 0
    for n in range(n_matches):  # MATCH
        setsA, setsB = 0, 0
        while max([setsA, setsB]) < sets_to_win:  # SET
            gamesA, gamesB = 0, 0
            while (max([gamesA, gamesB]) < 7 and min([gamesA, gamesB]) > 4) or max([gamesA, gamesB]) < 6:  # GAME
                pointsA, pointsB = 0, 0
                target = 7 if gamesA == 6 and gamesB == 6 else 4  # tie-break at 6:6
                while max([pointsA, pointsB]) < target or abs(pointsA - pointsB) < 2:
                    if random.randint(1, 1000) <= quali_A * 1000 * (1 - quali_adj * (pointsA - pointsB)):
                        pointsA += 1
                    else:
                        pointsB += 1
                    points += 1  # point counter
                if pointsA > pointsB:
                    gamesA += 1
                elif pointsA < pointsB:
                    gamesB += 1
                else:
                    pointsA, pointsB = 0, 0
                games += 1  # game counter
                if target == 7:
                    tiebreaks += 1  # tie-break counter
            if gamesA > gamesB:
                setsA += 1
            else:
                setsB += 1
            sets += 1  # set counter
        if setsA > setsB:
            matchesA += 1
        else:
            matchesB += 1

    print('Wins for A:      ', round(matchesA / n_matches, 4) * 100, '%')
    print('Points/game:     ', round(points / games, 2))
    print('Games/match:     ', round(games / n_matches, 2))
    print('Sets/match:      ', round(sets / n_matches, 2))
    print('Tie-breaks/match:', round(tiebreaks / n_matches, 2))
    print('Points played:   ', round(points / 10 ** 6, 3), 'M')


if __name__ == '__main__':
    tennis()

