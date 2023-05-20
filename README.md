# Dodo
Dodo is an application meant for everyday organization of tasks through to-do lists. It is developed using *Flask* and *Angular* frameworks as well as *Cassandra* database.

## Backend

*Python 3.10.0*

*Cassandra 4.0.4*

1. Installation of python modules using *pip*
	```bash
	pip install -r requirements.txt
	```

2. Populate database:
	```bash
	python create_and_populate_db.py
	```
3. Run app: 
	```bash
	python app.py
	```
## Frontend
1. Node.js and npm installationn (https://nodejs.org/en/download/)
2. Installation of Angular using npm
	```bash
	npm install -g @angular/cli
	```
3. Run app
	```bash
	ng serve --open
	```
