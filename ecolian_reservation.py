import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

############### 예약일자 설정하기 #####################################################

# 1. 이번달(True) or 다음달(False)
# 2. 주
# 3. 요일 

this_month = False # 이번달 선택 True, 이번달이 아니면(다음달) False
week_position = 1 # week_position = 1 번째 주
day_position = 5 # day_position = 7 번째 요일 (일=1, 월=2, 화=3, 수=4, 목=5, 금=6, 토=7)
#######################################################################################

open_flag = False        
def ecolian_action():
    global open_flag

    options = webdriver.ChromeOptions()
    options.add_argument('window-size=800,600')

    driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver', options=options)
    driver.implicitly_wait(2)

    driver.get(url='https://js.ecolian.or.kr:446/asp/ecolian/login.asp')

    id_input = driver.find_element_by_id('txtId')
    id_input. send_keys('maranta')

    pass_input = driver.find_element_by_id('txtPwd')
    pass_input.send_keys('xxxxx')

    login_button = driver.find_element_by_id('btnLogin')
    login_button.send_keys(Keys.RETURN)

    reserve_link = driver.find_element_by_xpath('//*[@id="navi"]/li[4]/a/img')
    reserve_link.click()

    if(not this_month):
        next_monath_link = driver.find_element_by_xpath('//*[@id="contents"]/p/a[2]/img')
        next_monath_link.click()

    date_xpath = '//*[@id="contents"]/table/tbody/tr[' + str(week_position+1) + ']/td[' + str(day_position) + ']/p'
    date_link = driver.find_element_by_xpath(date_xpath)
    if(date_link.text == '[예약가능]'):
        date_link.click()    
        comfirm_link = driver.find_element_by_xpath('//*[@id="rspop_01"]/div[1]/div[3]/div/a[1]')
        comfirm_link.click()
        time_link = driver.find_element_by_xpath('//*[@id="contents"]/table/tbody/tr[2]/td[2]/span')
        time_link.click() 
        try:
            open_flag = True
            result =driver.switch_to_alert()
            print(result.text)
            result.accept()         
            
        except:
            "There is no alert"
    else:
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

