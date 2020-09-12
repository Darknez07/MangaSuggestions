#! /bin/bash
if ! command -v pip &> /dev/null
then
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get install python3-pip python-dev
    elif [["$OSTYPE" == "win32"]]; then
        curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py
        python3 get-pip.py
    elif [["$OSTYPE" == "cygwin"]]; then
        curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py
        python3 get-pip.py
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        python3 get-pip.py
    else
        echo "Not Windows cygwin and Linux"
    fi
fi
pip install scrapy numpy pandas
echo -e "Please give your email id"
read name
echo -e "Please enter a genre"
read genre
echo -e "Please enter a date"
read date
python Prepare.py
python Send.py $name $genre $date
