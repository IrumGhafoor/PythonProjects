#Python Advanced Project 7: Creating an Amazon Product Availability Checker

from lxml import html
import requests
from time import sleep
import time
import schedule 
import smtplib

#Email id for who want to check availability 
receiver_email_id = "EMAIL_ID_TO_USER"

def check(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    
    page = requests.get(url, headers= headers)
    for i in range(20):
        sleep(3)
    doc = html.fromstring(page.content)
    XPATH_AVAILABILITY = '//div[@id = "availability"]//text()'
    RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
    AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None 
    return AVAILABILITY

def sendemail(ans, product):
    GMAIL_USERNAME = "your_email_address"
    PASSWORD = "your_password"
    
    
    recipient = receiver_email_id
    body_of_email = ans 
    email_subject = product + 'product availability'
    
    #creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    #start TLS for security 
    s.starttls()

def sendmail(ans, product):
    
    #authentication
    s.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    
    #message to be sent 
    headers = "\r\n".join(["from:" + GMAIL_USERNAME,
                           "subject" + email_subject,
                           "to:" + recipient,
                           "mime-version: 1.0",
                           "content-type: text/html"])
    content = headers + "\r\n\r\n" + body_of_email
    s.sendmail(GMAIL_USERNAME, recipient, content)
    s.quit()
    
def ReadAsIn():
    Asin = 'B077PWK5BT'
    url = "https://www.amazon.com/toys/b?ie=UTF8&node=165793011"
    print("Processing:" +url)
    ans = check(url)
    arr = [
        'Only 1 left in stock',
        'Only 2 left in stock',
        'In stock'
    ]
    print(ans)
    if ans in arr:
        sendemail(ans, Asin)

def job():
    print("Tracking....")
    ReadAsIn()
    
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
            