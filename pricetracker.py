import requests
from bs4 import BeautifulSoup
import smtplib
import time
import data #file that stores username and password

#OSU Trash Can
URL = 'https://www.amazon.com/NCAA-State-Buckeyes-Trash-Cooler/dp/B001CLHWXE/ref=sr_1_1?dchild=1&keywords=osu+trash+can&qid=1571931151&sr=8-1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

def get_price():
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    price = soup2.find(id='priceblock_ourprice').get_text()
    price = float(price[1:])

    return price

def notify():
    username = data.username #sending email from this email
    pwd = data.pwd
    send_to = 'kushpatel5749@gmail.com' #my email as recipient

    subject = 'The product is under your target price!'
    body = 'Buy now: ' + URL

    email_text = f'Subject: {subject}\n\n{body}'

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, pwd)
        server.sendmail(username, send_to, email_text)
        server.quit()

        print('Email sent!')
    except:
        print("Email did not send")


current_price = get_price()
target_price = 35

while(True):
    if (current_price <= target_price):
        notify()
        break;
    print('Price is too high right now. Check back later.')
    time.sleep(60*60*24) #seconds in a day
