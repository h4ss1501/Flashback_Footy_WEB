from flask import Flask, render_template, request, jsonify
from queries import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/worldcup')
def worldcup():
    tournaments = [
        {'year': 1930, 'host': 'Uruguay', 'date': '13-30 July', 'teams': 13, 'logo': '1930-world-cup-logo-600x400.png'},
        {'year': 1934, 'host': 'Italy', 'date': '27 May - 10 June', 'teams': 16, 'logo': '1934-world-cup-logo-600x400.png'},
        {'year': 1938, 'host': 'France', 'date': '4-19 June', 'teams': 15, 'logo': '1938-world-cup-logo-600x400.png'},
        # Add more tournaments here...
        {'year': 1950, 'host': 'Brazil', 'date': '24 June - 16 July', 'teams': 13, 'logo': '1950-world-cup-logo-600x400.png'},
        {'year': 1954, 'host': 'Switzerland', 'date': '16 June - 4 July', 'teams': 16, 'logo': '1954-world-cup-logo-600x400.png'},
        {'year': 1958, 'host': 'Sweden', 'date': '8-29 June', 'teams': 16, 'logo': '1958-world-cup-logo-600x400.png'},
        {'year': 1962, 'host': 'Chile', 'date': '30 May - 17 June', 'teams': 16, 'logo': '1962-world-cup-logo-600x400.png'},
        {'year': 1966, 'host': 'United Kingdom', 'date': '11-30 July', 'teams': 16, 'logo': '1966-world-cup-logo.png'},
        {'year': 1970, 'host': 'Mexico', 'date': '31 May - 21 June', 'teams': 16, 'logo': '1970-world-cup-logo-600x400.png'},
        {'year': 1974, 'host': 'West Germany', 'date': '13 June - 7 July', 'teams': 16, 'logo': '1974-world-cup-logo-600x400.png'},
        {'year': 1978, 'host': 'Argentina', 'date': '1-25 June', 'teams': 16, 'logo': '1978-world-cup-logo-600x400.png'},
        {'year': 1982, 'host': 'Spain', 'date': '13 June - 11 July', 'teams': 17, 'logo': '1982-world-cup-logo-600x400.png'},
        {'year': 1986, 'host': 'Mexico', 'date': '31 May - 29 June', 'teams': 24, 'logo': '1986-world-cup-logo-600x400.png'},
        {'year': 1990, 'host': 'Italy', 'date': '8 June - 8 July', 'teams': 24, 'logo': '1990-world-cup-logo-600x400.png'},
        {'year': 1994, 'host': 'USA', 'date': '17 June - 17 July', 'teams': 24, 'logo': '1994-world-cup-logo-600x400.png'},
        {'year': 1998, 'host': 'France', 'date': '10 June - 12 July', 'teams': 32, 'logo': '1998-world-cup-logo-600x400.png'},
        {'year': 2002, 'host': 'South Korea & Japan', 'date': '31 May - 30 June', 'teams': 32, 'logo': '2002-world-cup-logo-600x400.png'},
        {'year': 2006, 'host': 'Germany', 'date': '9 June - 9 July', 'teams': 32, 'logo': '2006-world-cup-logo-600x400.png'},
        {'year': 2010, 'host': 'South Africa', 'date': '11 June - 11 July', 'teams': 32, 'logo': '2010-world-cup-logo-600x400.png'},
        {'year': 2014, 'host': 'Brazil', 'date': '12 June - 13 July', 'teams': 32, 'logo': '2014-world-cup-logo-600x400.png'},
        {'year': 2018, 'host': 'Russia', 'date': '14 June - 15 July', 'teams': 32, 'logo': '2018-world-cup-logo-600x400.png'},
        {'year': 2022, 'host': 'Qatar', 'date': '20 November - 18 December', 'teams': 32, 'logo': '2022-world-cup-logo.png'}
    ]
    return render_template('worldcup.html', tournaments=tournaments)

@app.route('/player')
def player():
    return render_template('player.html')


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    playerName = data.get('playerName')
    teamName = data.get('teamName')
    tournament = data.get('tournament')
    sample_data = get_search(data,playerName,tournament)
    print(sample_data)
    # Filter sample data based on search input
    results = []
    for entry in sample_data:
        if (playerName.lower() in entry['goalscorer'].lower() if playerName else True) and \
           (teamName.lower() in (entry['homeTeam'].lower() + entry['awayTeam'].lower()) if teamName else True) and \
           (tournament.lower() in entry['tournament'].lower() if tournament else True):
            results.append(entry)

    return jsonify(results)


@app.route('/tournament/<int:year>')
def tournament(year):
    # Example data, you can extend this as needed
    top_four=get_top_four(year)
    top_teams = get_most_played_teams()
    top_scorer = get_top_scorers()
    
    tournaments = {
        year: {
            'logo': f'{year}-world-cup-logo-600x400.png',
            'details': {
                'date': f'13 July {year} – 30 July {year}',
                'teams': 13,
                'attendants': '590,549',
                'host': 'Uruguay'
            },
            'winners': [
                {'position': '1st Place', 'country': f'{top_four[0][0]}'},
                {'position': '2nd Place', 'country': f'{top_four[0][1]}'},
                {'position': '3rd Place', 'country': f'{top_four[0][2]}'},
                {'position': '4th Place', 'country': f'{top_four[0][3]}'}
            ],
            'teams': [
                {'team': 'Team A', 'won': 5},
                {'team': 'Team B', 'won': 4}
            ],
            'players': top_scorer
        },
        # Add more years as needed
    }

    if year in tournaments:
        data = tournaments[year]
        return render_template('tournament.html', year=year, data=data)
    else:
        return "Tournament not found", 404


if __name__ == '__main__':
    app.run(debug=True)
