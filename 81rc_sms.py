import time

import bs4
import requests
import schedule
from ronglian_sms_sdk import SmsSDK

RC81_URL = 'http://81rc.81.cn/'
RC81_URL_TEST = 'https://www.jiangtianyu.xyz/rc81_test'
LATEST_LIST = []

accId = '8aaf0708762cb1cf0176749bb8751cb2'
accToken = 'f75940aefc62439cb425555663070262'
appId = '8aaf0708762cb1cf0176749bb96e1cb9'


def send_message(msg):
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = '15198044376'
    datas = (msg, '0')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)


def schedule_job():
    global LATEST_LIST
    detail_list = []
    search_response = requests.get(RC81_URL)
    search_response.encoding = 'utf-8'
    search_soup = bs4.BeautifulSoup(
        search_response.text, "html.parser")
    tmp_content = search_soup.find('div', {'class': "left-gzdt"})
    detail_content = tmp_content.ul.find_all('a')
    for item in detail_content:
        detail_list.append(item.text)
    print(detail_list)
    if len(LATEST_LIST) == 0:
        LATEST_LIST = detail_list
    print(LATEST_LIST)
    for item in detail_list:
        if item in LATEST_LIST:
            pass
        else:
            LATEST_LIST.append(item)
            send_message(item)


if __name__ == "__main__":
    schedule.every(5).minutes.do(schedule_job)
    while True:
        schedule.run_pending()
