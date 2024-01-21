#!/bin/bash

# Install pip
sudo apt-get install python3-pip

# Updating pip...
python -m pip install --upgrade pip

# Updating and installing required modules...
pip install --upgrade mido midi keyboard pyautogui argparse

# Installation and update complete. Running kalimba_player...
python kalimba_player.py
