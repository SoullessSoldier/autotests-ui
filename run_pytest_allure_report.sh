#!/bin/bash
pytest -m 'regression' --alluredir=./allure-results --clean-alluredir && allure generate ./allure-results --output=./allure-report --clean