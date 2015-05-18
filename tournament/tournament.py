#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM Matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM Players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM Players;")
    for row in c:
        return row[0]
    db.commit()
    db.close()


def registerPlayer(name):
    """Adds a player to the tournament database.
      The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
      Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO players (name) values (%s)", (name, ))
    db.commit()
    db.close()


def playerStandings():
    """Select all from the player standings view that shows a table
of player id, name, wins(in descending order),
and matches played
    """
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM playerStandings;")
    rows = c.fetchall()
    db.close()
    return rows
    db.commit()
    db.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    I used columns for winner and loser as it was easier for me to understand the insert
    into the matches table.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)",
              (winner, loser))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of tuples, each of which contains
      (id1, name1, id2, name2)Id1: the first player's unique id
       name1: the player's name
      id2: the second player's unique id
      name2: the second player's name
    """
    """
    For loops are traditionally used when you have a piece of
     code which you want to repeat a number of times.
     turorials http://www.dotnetperls.com/list-python
     """
    # Iterate over each of the players and pair them
    # add another element to te end of the loop
    swisspairing = playerStandings()
    pairings = []
    for i in range(0, len(swisspairing), 2):
        pairings.append((swisspairing[i][0], swisspairing[i][1],
                         swisspairing[i+1][0], swisspairing[i+1][1]))
    return pairings
