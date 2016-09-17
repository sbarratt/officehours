all:
	rm app.db
	python initdb.py
	python filldb.py
