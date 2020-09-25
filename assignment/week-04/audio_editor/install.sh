#!/bin/sh
sudo apt-get update
sudo apt install python3-venv -y
sudo apt-get install libsndfile1-dev -y
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install Flask
pip install Pillow
pip install scipy
pip install librosa
pip install numpy
