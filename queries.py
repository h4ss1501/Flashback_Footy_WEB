import pandas as pd
import sqlite3
conn = sqlite3.connect('output_database.db')
cursor = conn.cursor()

# Players total goals scored in all tournaments combined
def get_top_scorers():

    query = """
    SELECT scorer, COUNT(*) as goals
    FROM goalscorers
    GROUP BY scorer
    ORDER BY goals DESC
    """

    cursor.execute(query)
    result = cursor.fetchall()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in result]


# Teams with most match wins in all tournaments combined
def get_most_winning_teams():
    query = """
    SELECT team, COUNT(*) AS wins
    FROM (
        SELECT home_team AS team
        FROM results
        WHERE tournament = 'FIFA World Cup' AND home_score > away_score
        UNION ALL
        SELECT away_team AS team
        FROM results
        WHERE tournament = 'FIFA World Cup' AND away_score > home_score
    ) AS all_wins
    GROUP BY team
    ORDER BY wins DESC
    """

    cursor.execute(query)
    result = cursor.fetchall()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in result]


# Teams with most penalty shootout wins in all tournaments combined
def get_shootouts():
    query = """
    SELECT winner, COUNT(*) AS wins
    FROM shootouts
    GROUP BY winner
    ORDER BY wins DESC
    """

    cursor.execute(query)
    result = cursor.fetchall()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in result]


# Teams with most world cup wins in all tournaments combined
def get_winners():
    query ="""
    SELECT Winner, COUNT(*) AS wins
    FROM WorldCups
    GROUP BY Winner
    ORDER BY wins DESC
    """

    cursor.execute(query)
    result = cursor.fetchall()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in result]



# Teams with most matches played in all tournaments combined
def get_most_played_teams():
    query = """
    SELECT team, COUNT(*) AS played
    FROM (
        SELECT home_team AS team
        FROM fifa_wc_matches
        UNION ALL
        SELECT away_team AS team
        FROM fifa_wc_matches
        )
    GROUP BY team
    ORDER BY played DESC
    """

    cursor.execute(query)
    result = cursor.fetchall()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in result]


# Total goals scored at a given tournament
def get_total_goals(year):
    query = """
    SELECT date, home_score, away_score
    FROM fifa_wc_matches
    WHERE strftime('%Y', date) = ?
    """
    
    cursor.execute(query, (year,))
    result = cursor.fetchall()
    i = 0.0
    for row in result:
        i = i + float(row[1]) + float(row[2])
    return i


# Total matches played in a single tournament
def get_matches_count(year):
    query = """
    SELECT COUNT(*)
    FROM fifa_wc_matches
    WHERE strftime('%Y', date) = ?
    """

    cursor.execute(query, (year,))
    result = cursor.fetchall()
    return result
    


# Players with most goals at a given tournament
def get_top_scorer(year):
    query="""
    SELECT scorer, COUNT(*) AS goals
    FROM goalscorers
    WHERE own_goal = 'FALSE'
    AND strftime('%Y', date) = ?
    GROUP BY scorer
    ORDER BY goals DESC
    """

    cursor.execute(query, (year,))
    result = cursor.fetchall()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in result]


# Multiple search system
def get_search(date, player, tournament):
    query="""
    SELECT gs.scorer, gs.minute, gs.date, fwm.home_team, fwm.away_team, fwm.home_score, fwm.away_score
    FROM goalscorers gs
    JOIN fifa_wc_matches fwm ON fwm.date = gs.date
    WHERE gs.own_goal = 'FALSE'
    AND (strftime('%Y', date) ? OR ? IS NULL)
    AND (tournament = ? OR ? IS NULL)
    AND (player = ? OR ? IS NULL)
    """

    cursor.execute(query, (date, tournament, player))
    result = cursor.fetchall()
    return result


# Top four best teams at given tournament
def get_top_four(year):
    query="""
    SELECT Winner, "Runners-Up", Third, Fourth
    FROM WorldCups
    WHERE Year = ?
    """

    cursor.execute(query, (year,))
    result = cursor.fetchall()
    return result

print(get_top_four('1930'))
