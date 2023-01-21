# Dodo
Dodo je aplikacija namenjena svakodnevnoj organizaciji obaveza kroz to-do liste. Razvijena je korišćenjem *Flask* i *Angular* okruženja i Cassandra baze podataka.

## Backend

*Verzija Python-a 3.10.0*

*Verzija Cassandre 4.0.4*

Pokretanje:
1. Instalacija potrebnih modula korišćenjem pip packet manager-a
	```bash
	pip install -r requirements.txt
	```

2. Kreiranje i dodavanje podataka u bazu:
	```bash
	python create_and_populate_db.py
	```
3. Pokretanje aplikacije: 
	```bash
	python app.py
	```
## Frontend
1. Instalacija Node.js-a i npm-a (https://nodejs.org/en/download/)
2. Instalacija Angular framework-a korišćenjem npm packet manager-a
	```bash
	-npm install -g @angular/cli
	```
3. Pokretanje aplikacije
	```bash
	-ng serve --open
	```
