# -*- coding: utf-8 -*-
import scrapy
#import items
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time



class MedSpider(scrapy.Spider):
    name = 'Med'
    allowed_domains = ['www.med.tn']

driver = webdriver.Chrome()
for v in range(1620,162):
    time.sleep(5)
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,'referer':'https://www.google.com/'}

    driver.get("https://www.med.tn/question-medicale/"+str(v))
   
    classpath=driver.find_elements_by_class_name('card-doctor-block')
    

    datatabibi=[]
    x=1
    for i in classpath:
        print("#################begn################")
        #print(i.find_element_by_xpath('//*[@id="pflistgridviewshowHoKCNmXjqUJc-form"]/div/div[1]/div['+str( x)+']/div[1]/div/div/div/a/h2').text)#maladie
        #print(i.find_element_by_xpath('//*[@id="pflistgridviewshowHoKCNmXjqUJc-form"]/div/div[1]/div['+str( x)+']/div[2]/div[1]/a/div/div[2]/div[1]').text)#nom doc
        #print(i.find_element_by_xpath('//*[@id="pflistgridviewshowHoKCNmXjqUJc-form"]/div/div[1]/div['+str( x)+']/div[1]/div/div').text)#question
        #print(i.find_element_by_xpath('//*[@id="pflistgridviewshowHoKCNmXjqUJc-form"]/div/div[1]/div['+str( x)+']/div[2]/div[1]/a/div/div[2]/div[2]').text)#specialite
        

        Maladie=(i.find_element_by_xpath('//*[@id="pflistgridviewshowHoKCNmXjqUJc-form"]/div/div[1]/div['+str( x)+']/div[1]/div/div/div/a/h2').text)#maladie
        Nom_doc=(i.find_element_by_xpath('//*[@id="pflistgridviewshowHoKCNmXjqUJc-form"]/div/div[1]/div['+str( x)+']/div[2]/div[1]/a/div/div[2]/div[1]').text)#nom doc
        Question=(i.find_element_by_xpath('//*[@id="pflistgridviewshowHoKCNmXjqUJc-form"]/div/div[1]/div['+str( x)+']/div[1]/div/div').text)#question
        spécialiste=(i.find_element_by_xpath('//*[@id="pflistgridviewshowHoKCNmXjqUJc-form"]/div/div[1]/div['+str( x)+']/div[2]/div[1]/a/div/div[2]/div[2]').text)#specialite
        
        x+=1

        tabibi_item={
            'Maladie':Maladie,
            'Nom_doc':Nom_doc,
            'Question':Question,
            'spécialiste':spécialiste
        }

        datatabibi.append(tabibi_item)
        print("#################end################")
df=pd.DataFrame(datatabibi)
print(df)
driver.quit()
    
        
