from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\Shalini\Desktop\CovidNoti\icon3.ico",
        timeout = 6
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        # notifyMe("Knightro","Be Safe,Stay In Home")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr += (tr.get_text())
            
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Maharashtra','West Bengal','Delhi']
        for item in itemList[0:23]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases Of Covid-19'
                nText = f"state {dataList[1]} \nIndian Cases : {dataList[2]} & Foreign Cases :{dataList[3]} \nCured:{dataList[4]} \nDeaths:{dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)
        
