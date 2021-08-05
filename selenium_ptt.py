import time
from selenium import webdriver

PATH = "C:/Users/JieDa/Desktop/selenium test/chromedriver.exe"
driver = webdriver.Chrome(PATH)
'''年齡確認頁面'''
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
over18_but = driver.find_element_by_name("yes")
over18_but.click()

'''文章列表'''
'''
titles = driver.find_elements_by_class_name("r-ent")
url=titles[0].find_element_by_css_selector('a').get_attribute('href')
print(titles[0].find_element_by_css_selector("div.title").text)
print(url)
'''
for i in range(50): #爬取頁數
    print("Page", i)
    titles = driver.find_elements_by_class_name("title")
    for title in titles:
        if "疫苗" not in title.text:
            #print(title.text)
            continue
        url=title.find_element_by_css_selector('a').get_attribute('href')
        print(title.text, url)
    pre_page = driver.find_element_by_partial_link_text("上頁")
    url = pre_page.get_attribute('href')
    driver.get(url)
#titles = driver.find_elements_by_partial_link_text("奧運")
'''
for title in titles:
    print(title.text)
'''
time.sleep(10)