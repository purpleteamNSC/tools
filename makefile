push:
	@git add .
	@git commit -m 'update code'
	@git push
	
umbrella:
	@python app/umbrella.py

relatorio:
	@python -m app/relatorio/app.py

