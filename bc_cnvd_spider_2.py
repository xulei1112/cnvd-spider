from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.common.keys import Keys
import time
import csv

if __name__ == '__main__':
    a= open("e:/test.csv",'r')
    reader=csv.reader(a)
    rows=[row for row in reader]
    #从csv文件中取出url链接，然后使用爬虫进行访问获取
    for j in rows:
        print(j[0])
        web = Firefox()
        web.get(j[0])
        #下面的element是爬取wp内容的
        element=web.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/div/p[1] ')
        descrition=web.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/div/div[4]')
        weihai=web.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/p[1]/span[2]')
        with open('e:/test3.csv','a+',newline='',encoding='gb18030') as result:
            writer=csv.writer(result)
            writer.writerow([j[0],element.text,descrition.text,weihai.text])
        web.close()
