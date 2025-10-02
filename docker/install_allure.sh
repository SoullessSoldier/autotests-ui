#!/bin/bash
sudo apt update
sudo apt install default-jre -y
# wget https://github.com/allure-framework/allure2/releases/download/2.35.1/allure-2.35.1.tgz
mkdir ../../allure
tar -xvzf ../allure-distr/allure-2.35.1.tgz -C ../../allure
export PATH=$PATH:/home/vscode/allure/allure-2.35.1/bin
allure --version
