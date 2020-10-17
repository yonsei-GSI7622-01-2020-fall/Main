#!/bin/sh
sudo apt-get update
sudo apt-get install python3-venv -y
sudo apt-get install libgl1-mesa-glx -y

python3 -m venv venv
. venv/bin/activate
pip install pip --upgrade 
pip install Flask Pillow opencv-python
pip install torch --no-cache-dir
pip install easyocr