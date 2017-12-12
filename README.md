# Challenge

- Title: Mistune

- Text: Markdown parsers are fun. Now click here and steal the cookie!

- Points: ~50-100

- Dowload:

- Solution: https://ctftime.org/task/4773

---

# Setup

- create virtual venv (python3 virtualenv3)
	`virtualenv venv`

- activate it
	`source venv/bin/activate`

- install requirements
	`pip install -r requirements.txt`


- create database
	`python createdb.py`

- run it
	`gunicorn -w 4 -b 0.0.0.0:80 ctfapp:app`

- or for debug
	`python run.py`

