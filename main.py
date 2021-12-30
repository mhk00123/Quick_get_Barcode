from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

import time

# Selenium Setup
opts = Options()
# opts.add_argument('--headless')  #不顯示Chrome
opts.add_argument('--disable-gpu')
webdriver_path = './chromedriver'
chrome = webdriver.Chrome(executable_path = webdriver_path, chrome_options = opts)

def Test_function(user_id, user_pass):
    time.sleep(1)
    url = 'https://www2.cpttm.org.mo/corpreg/app/'
    chrome.get(url)

    login_fill_id = chrome.find_element_by_xpath('/html/body/span/form/table/tbody/tr[1]/td[2]/input')
    password_fill_id = chrome.find_element_by_xpath('/html/body/span/form/table/tbody/tr[2]/td[2]/input')

    login_fill_id.send_keys(user_id)
    password_fill_id.send_keys(user_pass)

    chrome.find_element_by_xpath('/html/body/span/form/table/tbody/tr[4]/td[2]/input[1]').click()
    
    rec_f = ["今生餐飲有限公司" , "安泰物業管理有限公司" , "松花湖飲食一人有限公司" , "松花湖飲食一人有限公司" , "松花湖飲食一人有限公司" , "松花湖飲食一人有限公司" , "徐進民" , "徐進民" , "陳瑞榮" , "陳鳳霞" , "陳燕輝" , "詠軒餐飲管理服務有限公司" , "詠軒餐飲管理服務有限公司" , "詠軒餐飲管理服務有限公司" , "鄭浩榮" , "盧永權" , "蕭永傑"]
    des_f = ["今生" , "松花湖水餃" , "松花湖水餃" , "松花湖水餃" , "松花湖水餃" , "松花湖水餃" , "冰站" , "冰站" , "咖喱榮" , "跑馬地美食" , "蝦兵蟹將" , "有麵子" , "那個鍋" , "鍋說話" , "卓仁菜館" , "榮記咖啡室" , "美味廚"]
    
    chrome.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[2]/td[4]/ul/li[1]/a').click()
    
    for i in range(16):
    # ------ #
        url2 = 'https://www2.cpttm.org.mo/corpreg/app/?wicket:bookmarkablePage=:mo.org.cpttm.corpreg.LetterPage'
        chrome.get(url2)
        
        rec_fill = chrome.find_element_by_xpath('/html/body/div[2]/form/table/tbody/tr[2]/td[2]/input')
        des_fill = chrome.find_element_by_xpath('/html/body/div[2]/form/table/tbody/tr[3]/td[2]/textarea')
        
        rec_fill.send_keys(rec_f[i])
        des_fill.send_keys(des_f[i] + " 澳門餐飲業後台電子化資助計劃逾期通知書")
        
        selectA = chrome.find_element_by_id('dept')
        select = Select(selectA)
        select.select_by_value('18')
        chrome.find_element_by_xpath('/html/body/div[2]/form/input[1]').click()
        
        time.sleep(1)
        
        bar_code = chrome.find_element_by_xpath('/html/body/div[2]/input').get_attribute('value')
        b_code = bar_code+'.png'
        Dimg = chrome.find_element_by_xpath('/html/body/div[2]/p[2]/img')
        with open(b_code, 'wb') as f:
            f.write(Dimg.screenshot_as_png)
        
        time.sleep(2) 

          
if __name__ == '__main__':

    Test_function('leotam','SSSS')
