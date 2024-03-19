.PHONY: install-dependencies format-python clean-python format-js clean-js format clean

# Caminho para o diretório atual
CURRENT_DIR:=$(shell pwd)

# Instala as dependências necessárias para Python e Node.js
install-dependencies: install-python-dependencies install-js-dependencies

install-python-dependencies:
	@echo "Verificando e instalando dependências Python..."
	@command -v isort > /dev/null || pip install isort
	@command -v black > /dev/null || pip install black

install-js-dependencies:
	@echo "Instalando dependências Node.js..."
	@cd $(CURRENT_DIR) && npm install

# Formata o código Python usando black e isort
format-python: install-python-dependencies
	@echo "Formatação dos arquivos Python com black e isort..."
	@isort .
	@black .

# Limpeza do projeto Python (ajuste conforme necessário)
clean-python:
	@echo "Limpeza do projeto Python..."
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete

# Formata o código JS usando scripts definidos em package.json
format-js: install-js-dependencies
	@echo "Formatação dos arquivos JavaScript..."
	@npm run format

# Limpeza do projeto JS usando scripts definidos em package.json
clean-js:
	@echo "Limpeza do projeto JavaScript..."
	@npm run clean

# Comandos agregadores para formatação e limpeza
format: format-python format-js
clean: clean-python clean-js
