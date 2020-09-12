import subprocess
try:
    stdo = subprocess.check_output(['scrapy','crawl','Manganelo','-o','Some.csv'],
                               stderr=subprocess.STDOUT,
                               timeout=30)
except:
    print("Done Gathering data")