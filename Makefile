run: venv
	. venv/bin/activate && python3 manage.py runserver

venv: venv/touch

venv/touch: requirements.txt
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	touch $@

clean-all:
	rm -rf venv
