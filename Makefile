
install:
	virtualenv .
	bin/pip install -r requirements.txt

flake8:
	@flake8 \{\{cookiecutter.repo_name\}\}
	@flake8 hooks
