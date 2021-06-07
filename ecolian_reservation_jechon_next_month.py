import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

############### 예약 제외일자 설정하기 ##################################################
# (week, 요일) 1=일, 2=월, 3=화, 4=수, 5=목, 6=금, 7=토) 
# 2번째주 수요일을 제외할 경우: except_date = [(2, 4)]
# 2번째주 수요일과 3번째주 토요일을 제외할 경우: except_date = [(2, 4), (3, 7)]

except_date = [] 
#######################################################################################

open_flag = False
def ecolian_action():
    global open_flag

    options = webdriver.ChromeOptions()
    options.add_argument('window-size=240,200')
    
    driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver', options=options)
    driver.implicitly_wait(2)

    driver.get(url='https://jc.ecolian.or.kr/asp/ecolian/login.asp')

    id_input = driver.find_element_by_id('txtId')
    id_input. send_keys('maranta')

    pass_input = driver.find_element_by_id('txtPwd')
    pass_input.send_keys('xxxxx')

    login_button = driver.find_element_by_id('btnLogin')
    login_button.send_keys(Keys.RETURN)
    
    sleep(1)

    reserve_link = driver.find_element_by_xpath('//*[@id="navi"]/li[4]/a/img')
    reserve_link.click()

    next_monath_link = driver.find_element_by_xpath('//*[@id="contents"]/p/a[2]/img')
    next_monath_link.click()

    for i in range(2, 8):
        except_cnt = 0
        for j in range(1, 8):
            date_xpath = '//*[@id="contents"]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']/p'
            try:
                date_link = driver.find_element_by_xpath(date_xpath)
                print(i, j, date_link.text)
                if(date_link.text == '[예약가능]' and (i-1, j) not in except_date):
                    date_link.click()
                    comfirm_link = driver.find_element_by_xpath('//*[@id="rspop_01"]/div[1]/div[3]/div/a[1]')
                    comfirm_link.click()
                    time_link = driver.find_element_by_xpath('//*[@id="contents"]/table/tbody/tr[2]/td[2]/span')
                    time_link.click()
                    alert_box = driver.switch_to_alert()
                    alert_box.accept()
                    
                    duration = 1  # seconds
                    freq = 440  # Hz
                    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                    open_flag = True
            except:
                except_cnt += 1
                print(i, j, 'No Schedule')
        # except가 7번 발생하면 예약화면이 아니므로(로그인 실패 등) 종료
        if(except_cnt >= 7):
            break
    if(not open_flag):
        driver.close()   

i = 0
starttime = time.time()
while True:
    i += 1
    if(not open_flag):
        print("close", i, open_flag)
        ecolian_action()
    else:
        print("open", i, open_flag)

    time.sleep(5 - ((time.time() - starttime) % 5))
