# Ebay Web Scraper - project initialization
#IMPORT MODULES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re
#DESCIPTION URL AND BASE AGENT 
USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.89 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,tr;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
} 
BASE_URL="https://www.ebay.com"
#CHROME SETTİNGS
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",False)
options.add_argument("--start-maximazed")
options.add_argument(f"--user-agent={USER_AGENT}")
#OPEN CHROME
driver=webdriver.Chrome(options=options)
actions=ActionChains(driver)
try:
    driver.get(BASE_URL)
    driver.maximize_window()
    WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.TAG_NAME,"body")))
    print("PAGE OPENED")
except:
    print("PAGE NOT OPEN")
class SeleniumButtons:
    def press_buton_class_name(the_driver,class_name):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,class_name)))
            buton=the_driver.find_element(By.CLASS_NAME,class_name)
            actions.move_to_element(buton).perform()
            buton.click()
            time.sleep(1)
        except:
            print("class name tuşlama yapılmadı")
            pass
    def press_button_id(the_driver,id):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,id)))
            button=the_driver.find_element(By.ID,id)
            actions.move_to_element(button).perform()
            button.click()
            time.sleep(1)
        except:
            print("id tuşlama yapılmadı")
            pass
    def press_button_css_selector(the_driver,css_selector):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,css_selector)))
            buton=the_driver.find_element(By.CSS_SELECTOR,css_selector)
            actions.move_to_element(buton).perform()
            the_driver.execute_script("arguments[0].scrollIntoView({block:'center'});", buton)
            time.sleep(0.8)
                # Güvenli JS tıklama
            the_driver.execute_script("arguments[0].click();", buton)
            
            time.sleep(1)
        
        except:
            print("css selectore göre tuslama yapılmadı")
            pass
    def press_buton_xpath(the_driver,xpath):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,xpath)))
            buton=the_driver.find_element(By.XPATH,xpath)
            actions.move_to_element(buton).perform()
            buton.click()
            time.sleep(1)
        except:
            print("xpathe göre tuşlama yapılmadı")
            pass
    def scroll_to_bottom(start,finish):
        driver.execute_script(f'window.scrollTo({start},{finish});')
        time.sleep(1)
    def find_elements_css(the_driver,css_selector):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,css_selector)))
            buton=driver.find_elements(By.CSS_SELECTOR,f"{css_selector}")
            actions.move_to_element(buton).perform()
            buton.click()
            time.sleep(1)
        except:
            print("css selectore göre bulunamadı")
            pass  
    def find_elements_classname(the_driver,css_selector):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,css_selector)))
            buton=the_driver.find_elements(By.CLASS_NAME,f"{css_selector}")
            actions.move_to_element(buton).perform()
            buton.click()
            time.sleep(1)
        except:
            print("class name göre bulunamadı")
            pass 
#PUSH BUTTONS ON PAGE
SeleniumButtons.press_button_id(driver,"gh-ac-wrap")
computer_name=driver.find_element(By.ID,"gh-ac").send_keys("laptop"+Keys.ENTER)
WebDriverWait(driver,30).until_not(EC.url_contains("splashui"))
element1 = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="16 GB"]')
driver.execute_script("arguments[0].click();", element1) 

WebDriverWait(driver,30).until_not(EC.url_contains("splashui"))
element2 = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="16-17 in"]')
driver.execute_script("arguments[0].click();", element2)      
#EXTRACING DATA
def take_link(the_driver):
    datas=[]
    page=1
    while True:
        time.sleep(2)
        cards=driver.find_elements(By.CSS_SELECTOR,"a.s-card__link")
        datas=[]
        for link in cards:
            href=link.get_attribute("href")
            m=re.search(r"/itm/(\d{9,})",href)
            if m: 
                datas.append("https://www.ebay.com/itm/"+m.group(1))
            
            #CLİCK MORE BUTTONS
        try:
            more_buttons = the_driver.find_elements(By.CSS_SELECTOR, 'a.pagination__next.icon-link')
        except:
            print("more button not find")
        if len(more_buttons) != 0:
            more_button = more_buttons[0]
                # Sayfanın ortasına kaydır
            the_driver.execute_script("arguments[0].scrollIntoView({block:'center'});", more_button)
            time.sleep(0.8)
            # Güvenli JS tıklama
            the_driver.execute_script("arguments[0].click();", more_button)
            time.sleep(1.5)
            page+=1  
        else:
            print("daha fazla sayfa yok")
            break
        return datas  
                     
def open_page(driver, datas):
    result = []
    page_count=0
    for link in datas:
        time.sleep(3)
        driver.get(link)
        # Sayfa gerçekten yüklenene kadar bekle
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.x-item-title__mainTitle')))
        title = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"h1.x-item-title__mainTitle span.ux-textspans--BOLD")))
        title = title.text.strip()
        price_el = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
            "div[data-testid='x-price-primary'] span.ux-textspans")))
        price = price_el.text.strip()
        #price=re.sub(r"[^\d\.]", "",price)

        see_details=driver.find_element(By.CSS_SELECTOR,'button[data-clientpresentationmetadata*="SHIPPING_RETURNS_PAYMENTS_TAB_MODULE"]')
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", see_details)
        time.sleep(0.8)
        driver.execute_script("arguments[0].click();", see_details)
        time.sleep(1.5)
        delivery_start = driver.find_element(By.XPATH, "//span[contains(text(),'Estimated between')]/following::span[contains(@class,'ux-textspans--BOLD')][1]").text.strip()
        delivery_end = driver.find_element(By.XPATH, "//span[contains(text(),'Estimated between')]/following::span[contains(@class,'ux-textspans--BOLD')][2]").text.strip()
        shipping_price = driver.find_element(By.XPATH, "//span[contains(text(),'Shipping:')]/following::span[contains(@class,'ux-textspans')][1]").text.strip()
        #shipping_price = re.sub(r"[^\d\.]", "",shipping_price)
        result.append({
            "title": title,
            "price": price,
            "shipping price": shipping_price,
            "delivery start": delivery_start,
            "delivery end": delivery_end
        })
        #print("✅", result)
        page_count+=1
        print(f"ÇEKİLEN SAYFA SAYISI =================={page_count}")
    return result
datas=take_link(driver)
datas=list(dict.fromkeys(datas))
datas=datas[:35]
result=open_page(driver,datas)
print("EXTRACING DATAS =",len(result)) 
df=pd.DataFrame(result) 
df.to_excel("ebay.xlsx")
