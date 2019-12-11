import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import requests
#import pickle
import datetime

today = datetime.datetime.today()
tom = datetime.datetime.today() + datetime.timedelta(days=1)
tomorrow = tom.strftime('%A')


def send_email(toEmail, body):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login('*********@gmail.com', '**********')

    msg = MIMEMultipart()
    msg['From'] = '*********@gmail.com'
    msg['To'] = toEmail
    msg['Subject'] = 'Tomorrows Garbage'
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail('*********@gmail.com', toEmail, text)
    server.quit()


website = 'http://www.burbio.com/states/New-Jersey/Fair-Lawn/borough-of-fair-lawn-sanitation-recycling-schedule-monday-pickup-section-3'

source = requests.get(website)
soup = BeautifulSoup(source.text, 'lxml')
StatementTxt = soup.find_all('div', class_='tile-body')
DateTxt = soup.find_all('div', class_='tile-head')


def get_date(DateTxt, index):
    body = str(DateTxt[index])
    ran = body.split('>')
    idk = ran[2]
    end = idk.split('\n')[1]
    end = end[8:]
    end = end.split(" ")[0]
    return end


def get_statement(StatementTxt, index):
    body = str(StatementTxt[index])
    ran = body.split('>')
    idk = ran[3]
    end = idk.split('<')[0]
    return end


#pickleIn = open('garbage.pickle', 'rb')
#numberDict = pickle.load(pickleIn)
#pickleIn.close()
#numberDict example
#numberDict = '*********': ('*********@tmomail.net', '*********')}
numberDict = ["1*********@tmomail.net"]
while True:
    if get_date(DateTxt, 0) == tomorrow:
        for i in numberDict:
            send_email(i, get_date(DateTxt, 0) + ' ' + get_statement(StatementTxt, 0) + '  ')
    elif get_date(DateTxt, 1) == tomorrow:
        for i in numberDict:
            send_email(i, get_date(DateTxt, 1) + ' ' + get_statement(StatementTxt, 1) + '  ')
