#!/bin/bash

#colours
red='\e[1;31m'
black='\e[1;30m'
green='\e[1;32m'
cayan='\e[1;36m'
yellow='\e[1;33m'
white='\e[1;37m'
reset='\e[1;0m'
cd ~
echo -e $red
apt install wget -y
echo "========================================================="
wget  https://raw.githubusercontent.com/SadhukhanR/bmiconsole/main/LICENSE
wget  https://raw.githubusercontent.com/SadhukhanR/bmiconsole/main/main.py 
# wget  https://raw.githubusercontent.com/SadhukhanR/bmiconsole/main/bmiconsole
wget  https://raw.githubusercontent.com/SadhukhanR/bmiconsole/main/main.txt
wget  https://raw.githubusercontent.com/SadhukhanR/bmiconsole/main/help.txt
wget  https://raw.githubusercontent.com/SadhukhanR/bmiconsole/main/bmi
echo -e $cayan
cat main.txt
# chmod +x bmiconsole
chmod +x bmi
sleep 5
echo -e $yellow
echo "========================================================"
cat LICENSE
echo "========================================================"
rm -rf LICENSE
sleep 5
cd /usr/local/bin
mkdir .bmiconsole
cd .bmiconsole
mkdir src
cd ~
#mv -f bmiconsole /usr/local/bin
mv -f main.py /usr/local/bin/.bmiconsole/src
mv -f main.txt /usr/local/bin/.bmiconsole/src
mv -f help.txt /usr/local/bin/.bmiconsole/src
#mv -f bmi /usr/local/bin/.bmiconsole/src
mv -f bmi /usr/local/bin
echo -e $green
echo "Installing bmiconsole ......"
sleep 10
echo -e $yellow
apt install python3-pip -y
sleep 5
pip3 install numpy
sleep 5
pip3 install matplotlib
sleep 5
echo -e $red
echo "==============================================================="
echo "Starting bmiconsole ......"
sleep 5
bmi