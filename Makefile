.ONESHELL:
SHELL:= /usr/bin/bash
.PHONY: all

back: 
	(cd backend; \ 
	./start.sh &) 

front:
	(cd frontend; \ 
	npm run dev &)

buildback: 
	(cd backend; \ 
	python3 -m venv venv 
	source $$PWD/venv/bin/activate; \ 
	pip install -r requirements.txt ) 		

buildfront:
	(cd frontend; \ 
	npm install )

installdep:
	curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
	(source ~/.bashrc && \
	bash -c nvm install --lts )
	

down: 
	pkill -f "python app.py"
	bash -e "ps -fea | grep vite | grep -v grep | awk '{print $2}' | xargs kill -9"

all: front back