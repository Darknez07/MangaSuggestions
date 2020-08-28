# Manga Suggestions via Email
### This repositry just run "./Ex.sh" in as bash script
## Note Please follow the following request for the fresh data
## Each day update the data
1 Go into Manga folder
2 Go into send
3 Ucomment two lines written as:
    a) import subprocess
    b) subprocess.Popen(['scrapy','crawl','Manganelo','-o','Some.csv']).communicate()[0]
## For data you can wait at least 40 sec and press CTRL + C
## After this Comment the mentioned lines back
### Note Comment the lines back after updation is complete
4) For programmers it's fun to play around with the code
#### Date format input is
### Month first three (First Capital) letters space and date comma and then years in last two digit
Example
Aug 26,19
### Thanks please give me credit if you use it
### Notification facility is dependent on the running of app