push:
	@git add .
	@git commit -m 'update code'
	@git push

umbrella:
	@python app/umbrella.py

azion:
	@python app/azion.py

relatorio:
	@python app/relatorio.py

