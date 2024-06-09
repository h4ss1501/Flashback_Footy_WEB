from models import db

# Players total goals scored in all tournaments combined
def get_top_scorers():
    query = """
    SELECT scorer, COUNT(*) as goals
    FROM goalscorers
    """

    result = db.session.execute(query)
    return [dict(row) for row in result]

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
    """

    result = db.session.execute(query)
    return [dict(row) for row in result]

# Teams with most penalty shootout wins in all tournaments combined
def get_shootouts():
    query = """
    SELECT winner
    FROM shootouts
    """

    result = db.session.execute(query)
    return [dict(row) for row in result]

# Teams with most world cup wins in all tournaments combined
def get_winners():
    query ="""
    SELECT Winner
    FROM WorldCups
    """

    result = db.session.execute(query)
    return [dict(row) for row in result]


# Teams with most matches played in all tournaments combined
def get_most_played_teams():
    query = """
    SELECT home_team, away_team
    FROM fifa_wc_matches
    """

    result = db.session.execute(query)
    return [dict(row) for row in result]

# Total goals scored at a given tournament
def get_total_goals(year):
    query = """
    SELECT date, home_score, away_score
    FROM fifa_wc_matches
    WHERE strftime('%Y', date) = ?
    """
    
    result = db.session.execute(query, year)
    i = 0
    for row in result:
        i = i + row.home_score + row.away_score
    return i

# Total matches played in a single tournament
def get_matches_count(year):
    query = """
    SELECT COUNT(*)
    FROM fifa_wc_matches
    WHERE strftime('%Y', date) = ?
    """

    result = db.session.execute(query, year)
    return result
    
# Players with most goals at a given tournament
def get_top_scorer(year):
    query="""
    SELECT scorer
    FROM goalscorers
    WHERE own_goal = 'FALSE'
    AND strftime('%Y', date) = ?
    """

    result = db.session.execute(query, year)
    return [dict(row) for row in result]

# Multiple search system
def get_search(date, player, tournament):
    query="""
    SELECT gs.scorer, gs.minute, gs.date, fwm.home_team, fwm.away_team, fwm.home_score, fwm.away_score
    FROM goalscorers gs
    JOIN fifa_wc_matches fwm ON fwm.date = gs.date
    WHERE gs.own_goal = 'FALSE'
    AND (date = ? OR ? IS NULL)
    AND (tournament = ? OR ? IS NULL)
    AND (player = ? OR ? IS NULL)
    """

    result = db.session.execute(query, date, tournament, player)
    return result

# Top four best teams at given tournament
def get_top_four(year):
    query="""
    SELECT Winner, Runners-Up, Third, Fourth
    FROM WorldCups
    WHERE Year = ?
    """

    result = db.session.execute(query, year)
    return result

