@echo off
echo Automatic run as admin...
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
set CURRENT_PATH=/d %~dp0
cd %CURRENT_PATH%

echo Updating pip...
python.exe -m pip install --upgrade pip

echo Updating and installing required modules...
pip install --upgrade mido keyboard pyautogui argparse

echo Installation and update complete. Running kalimba_player...
kalimba_player.exe
