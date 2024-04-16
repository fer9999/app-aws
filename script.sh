#!/bin/bash
git clone https://github.com/fer9999/app-aws
cd app-aws
make installdeps
make buildfront
make buildback
make

