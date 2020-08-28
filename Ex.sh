#! /bin/bash
cd Manga
sudo apt-get install python3-pip python-dev
pip install scrapy numpy pandas
echo -e "Please give your email id"
read name
echo -e "Please enter a genre"
read genre
python Send.py $name $genre