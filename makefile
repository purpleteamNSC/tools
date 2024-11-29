umbrella:
	@python app/umbrella.py

relatorio:
	@python -m app/relatorio/app.py

push:
	@git add .
	@git commit -m 'update code'
	@git push