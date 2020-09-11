#!/bin/sh
sudo apt-get update
sudo apt install python3-venv -y
python3 -m venv venv
. venv/bin/activate
pip install Flask