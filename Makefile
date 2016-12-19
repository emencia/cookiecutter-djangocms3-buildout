
install:
	virtualenv .
	bin/pip install -r requirements.txt

flake8:
	@flake8 \{\{cookiecutter.repo_name\}\} --exclude=\{\{cookiecutter.repo_name\}\}/project/mods_available,'{{cookiecutter.repo_name}}/project/*/migrations'
	@flake8 hooks
