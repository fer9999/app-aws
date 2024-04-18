#!/bin/bash
sudo apt update
sudo apt install make python3.10-venv -y
git clone https://github.com/fer9999/app-aws
cd app-aws

make installdep
make buildfront
make buildback
make

