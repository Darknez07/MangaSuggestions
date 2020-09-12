import subprocess
try:
    stdo = subprocess.check_output(['scrapy','crawl','Manganelo','-o','Some.csv'],
                               stderr=subprocess.STDOUT,
                               timeout=120)
except:
    print("Done Gathering data")