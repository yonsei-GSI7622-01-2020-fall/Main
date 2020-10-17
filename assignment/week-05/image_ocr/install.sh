#!/bin/sh
sudo apt-get update
sudo apt-get install cmake libgtk-3-dev -y
sudo apt-get install gcc g++ python3-distutils -y
sudo apt-get install build-essential cmake -y
sudo apt-get install libopenblas-dev liblapack-dev -y
sudo apt-get install libx11-dev libgtk-3-dev -y
sudo apt-get install python python-dev python-pip -y
sudo apt-get install python3 python3-dev python3-pip -y
sudo apt-get install python3-venv -y
python3 -m venv venv
. venv/bin/activate
pip install pip --upgrade 
pip install Flask
pip install Pillow
pip install scikit-build
pip install opencv-contrib-python
pip install numpy
pip install torch --no
pip install easyocr