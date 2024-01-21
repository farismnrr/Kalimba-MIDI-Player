@echo off
echo Updating pip...
python.exe -m pip install --upgrade pip

echo Updating and installing required modules...
pip install --upgrade mido midi keyboard pyautogui argparse

echo Installation and update complete. Running kalimba_player...
kalimba_player.exe
