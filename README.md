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
