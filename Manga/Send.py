import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# import subprocess
from sys import argv as cmd
import pandas as pd
import  numpy as np
# print(subprocess.Popen(['scrapy','crawl','Manganelo','-o','Some.csv']).communicate()[0])
df = pd.read_csv('Some.csv')

def create_style(link_collect):
    style_link = """<style>"""
    for i in range(len(link_collect)):
        # print(style_link)
        style_link+="""
        .img-class{0}{{
                content:url("{1}")
            }}""".format(i, link_collect[i])
    style_link+="""</style>"""
    return style_link

def CreateMessage(links, names, genres,dates,ratings, lastchaps, imgs):
    html = """ """
    for i in range(len(links)):
        html+="""<h2>{}</h2>
            <a href="{}">
                <img class="img-class{}" src="{}"/>
            </a>
            <h3>Genres: </h3>""".format(names[i], links[i], i, imgs[i])
        html+="""<ul>"""
        for j in genres[i].split(','):
            html+="""<li>{}</li>""".format(j)
        html+="""</ul>"""
        html+="""<h5>Rating: {}</h5>
        <h5> Latest Chap: {} </h5>
        """.format(ratings[i], lastchaps[i])
    return html

def send_mail(email,Name, Link, Genre,date,rated,chap, imgs):
    sender_email = "rishikakkar42@gmail.com"
    receiver_email = email
    # print(receiver_email)
    password = "9997201D8C7D66D74C9EB1606C02EB87F91B"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Manga Suggestion By Rishi Kakkar"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """<!DOCTYPE html>
        <html>
        Hi there
        """
    # Create the plain-text and HTML version of your message
    text ="""This may not work"""
    html+= CreateMessage(Link,Name,Genre,date,rated, chap,imgs)
    html+="""</body></html>"""
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    # print(html)
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.elasticemail.com", 465, context=context) as server:
        # server.ehlo()
        # server.starttls()
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
# for i in range(150):
#     count = 0
#     if str(pd.to_datetime(df.loc[i,2],format="%b %d,%y")) == str(pd.to_datetime("today").replace(hour=0,minute=0,second=0))[:-7]:
#         if "Action" in df.loc[i,8].split(','):
#             send_mail(df.loc[i,0],df.loc[i, 7],df.loc[i, 8].split(','),df.loc[i, 2],df.loc[i, 10],df.loc[i,1])
#             count+=1
#         if count == 60:
#             break
    # break
email = ""
try:
    email = cmd[1]
except:
    email = ""
finally:
    email="darknez077@gmail.com"
indx = np.random.randint(40,df.shape[0],10)
send_mail(email,df.loc[indx,'Name'].reset_index(drop=True),
      df.loc[indx, 'Link'].reset_index(drop=True),
      df.loc[indx, 'Genre'].reset_index(drop=True),
      df.loc[indx, 'Dated Released'].reset_index(drop=True),
      df.loc[indx,'Rating'].reset_index(drop=True),
      df.loc[indx,'Latest Chapter'].reset_index(drop=True),
      df.loc[indx, 'img-link'].reset_index(drop=True))
#   df[df['Name'] == 'One Piece'])
