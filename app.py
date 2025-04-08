from flask import Flask, jsonify
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# SerpAPI base URL and API key
SERP_API_URL = "https://serpapi.com/search.json"
SERP_API_KEY = os.getenv("SPORTS_API_KEY")

#Defines a new route /sports that only responds to HTTP GET requests.
#When this route is hit, the get_nfl_schedule() function runs immediately.
@app.route('/sports', methods=['GET'])
def get_nfl_schedule():

    #Fetches the NFL schedule from SerpAPI and returns it as JSON
    try:
        # Query SerpAPI
        params = {
            "engine": "google",
            "q": "nfl schedule 2025",
            "api_key": SERP_API_KEY
        }
        response = requests.get(SERP_API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        print(json.dumps(data, indent=2))

        # Safely accesses the nested "games" list inside "sports_results".
        #Defaults to an empty list if "sports_results" or "games" are missing.
        games = data.get("sports_results", {}).get("games", [])
        if not games:
            return jsonify({"message": "No NFL schedule available.", "games": []}), 200

        # Format the schedule into JSON format
        formatted_games = []
        for game in games:
            teams = game.get("teams", [])
            if len(teams) == 2:
                away_team = teams[0].get("name", "Unknown")
                home_team = teams[1].get("name", "Unknown")
            else:
                away_team, home_team = "Unknown", "Unknown"

            game_info = {
                "away_team": away_team,
                "home_team": home_team,
                "venue": game.get("venue", "Unknown"),
                "date": game.get("date", "Unknown"),
                "time": f"{game.get('time', 'Unknown')} ET" if game.get("time", "Unknown") != "Unknown" else "Unknown"
            }
            formatted_games.append(game_info)

        #Returns the list of formatted games and a success message in JSON format with a 200 status code.
        return jsonify({"message": "NFL schedule fetched successfully.", "games": formatted_games}), 200
    
    #If anything in the try block fails, this catches the error and returns a 500 Internal Server Error with a message and the exception details
    except Exception as e:
        return jsonify({"message": "An error occurred.", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
