ENV_NAME = sms-spam-predictor
PYTHON_VER = 3.10

.PHONY: setup export-env install uninstall update

setup:
	conda env create -n $(ENV_NAME) -f environment.yml
	pip install -e .

export-env:
	conda env export -n $(ENV_NAME) --no-builds | grep -v "sms-spam-predictor" > environment.yml

install:
	conda install -n $(ENV_NAME) -y $(filter-out $@,$(MAKECMDGOALS))
	$(MAKE) export-env

uninstall:
	conda remove -n $(ENV_NAME) -y $(filter-out $@,$(MAKECMDGOALS))
	$(MAKE) export-env

update:
	conda update -n $(ENV_NAME) -y $(filter-out $@,$(MAKECMDGOALS))
	$(MAKE) export-env