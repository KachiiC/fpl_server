# FPL server

This is a simple fantasy premier league server built using django rest framework.

### Requirements
- You will need to have a version of [python 3](https://www.python.org/downloads/) installed.

check this by using the following command
```bash
python3 --version
```

### Installation

Once you've cloned/forked the repository, navigate to the repository. Create a virtual environment and activate it using the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
```

Once you've activated your virtual environment install your python packages by running:
```
pip install -r requirements.txt
python manage.py migrate
```

Now let's migrate our django project:
```
python manage.py migrate
```

If there are no hitches here you should now be able to open your server by running: 
```
python manage.py runserver
```

# Endpoints
All the endpoints are **GET** requests.

| Endpoint    | Input Type| Example |
| ----------- | --------- | ----------- |
| League      | League Id | http://127.0.0.1:8000/league=LEAGUE_ID
| Player      | Entry Id  | http://127.0.0.1:8000/league=ENTRY_ID

## Player Example
To get a entry Id, navigate to your points page in your browser and take the following from the URL:

This endpoint will be: [http://127.0.0.1:8000/player=127136](http://127.0.0.1:8000/player=127136)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/djpykyu4tw1eoo6ndong.png)

## League Example
To get a league Id, navigate to the league in your browser and take the following from the URL:

This endpoint will be: [http://127.0.0.1:8000/league=401369](http://127.0.0.1:8000/league=401369)
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/oi1zn7p5zgh9bhdxoxew.png)

# Data

### League Data
League returns an array of players 

### Player Data:

| Key    | Value | Example |
|--------|-------|---------|
|   player_id | The entry Id of the player | 127136,
|   player_name | Full name of player | "Kachi Cheong"
|   team_name | Team name | "The 7th Hokage"
|   current_gameweek | The current gameweek | 37
|   last_gameweek_points | Points from last Gameweek| 117
|   points_total | Current points total | 2259
|   transfers_total | Total Number of transfers | 36
|   points_on_transfers | Points sarcraficed for transfers| 28
|   team_value | Total value of team | 995
|   chips | List of chips used | *please refer to Chips*  
|   matches | List of player's matchdays | *please refer to MatchDay*  


### Chips Data
| Key    | Value | Example |
|--------|-------|---------|
| name     | Name of the chip used | "wildcard",
| matchday | Matchday chip was used | 7 
| date     | Date chip was used  | "02/10/2021"

### MatchDay Data
| Key    | Value | Example |
|--------|-------|---------|
| gameweek| Match day gameweek | 1
| game_week_points| Points scored during gameweek | 102
| points_total| Current points total | 102
| transfers| Transfers made this gameweek | 0
| team_value| Gameweek Team Value | 1000
| transfers_cost| Total points spent on transfers  | 0
| bench_points| Points scored by bench players | 9
