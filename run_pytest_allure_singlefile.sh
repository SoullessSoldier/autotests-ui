#!/bin/bash
pytest -m "regression" --alluredir=./allure-results --clean-alluredir && allure generate ./allure-results --clean -o ./chromium-webkit-firefox --single-file