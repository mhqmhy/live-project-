#url=https://fz.meituan.com/
#http://www.dianping.com/ 大众点评
import requests
import common
import json
import os
import time
from selenium import webdriver
path="./chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(executable_path=path)

def down(keyword,txtpath=''):
    browser.get('https://fz.meituan.com/')
    time.sleep(2)
    text=browser.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[1]/input')
    text.send_keys(keyword)
    btn=browser.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[1]/button')
    btn.click()
    time.sleep(3)
    array = []
    if os.path.exists(txtpath):
        os.remove(txtpath)
    try:
        for i in range(30):
            print("第{0}页".format(i), end=' ')
            renqi=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]/a')
            renqi.click()
            time.sleep(3)
            try:
                # '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]'
                # '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]'
                lists = browser.find_elements_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div')
            except Exception as e:
                print('4',e)
            print(len(lists))
            time.sleep(2)
            try:
                for j in lists:
                    try:
                        dic = {}
                        try:
                            href = j.find_element_by_xpath('./div/div/div/div/a')
                        except Exception as e:
                            print('href',e)
                        dic["href"] = href.get_attribute('href')
                        # print(dic["href"],href.text)
                        dic["name"] = href.text
                        dic["data-id"] = json.loads(href.get_attribute("data-lab"))
                        try:
                            level = j.find_elements_by_xpath('./div/div/div/div/div[@class="item-eval-info clearfix"]/span')
                        except Exception as e:# print(len(level))
                            print('level')
                        dic["level"] = []
                        dic["price"]=''

                        try:
                            dic["price"]=j.find_element_by_xpath('./div/div/div/div/div[3]/div/span[@class="avg-price"]').text
                            print(dic["price"])
                        except:
                            pass
                        for k in level:
                            dic["level"].append(k.text)
                        dic["address"] = j.find_element_by_xpath(
                            './div/div/div/div/div[@class="item-site-info clearfix"]/div/span[@class="address ellipsis"]').text
                        # print(dic["address"])
                    except Exception as e:
                        print('2',e)
                    array.append(dic)
            except Exception as e:
                print('1', e)
            nextPage = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/nav/ul/li[7]')
            time.sleep(3)
            nextPage.click()
            time.sleep(3)
    except Exception as e:
        print('2', e)
    print(array)
    with open(txtpath, 'a+', encoding="gbk", errors='ignore') as f:
        f.write(json.dumps(array, ensure_ascii=False, indent=4))
if __name__=="__main__":
    # lists=["五四北泰禾广场服饰","仓山万达服饰","东二环泰禾广场服饰","东街口服饰","宝龙万象城服饰","金融街万达服饰","五一广场服饰"]
    lists = ["五四北泰禾广场美食", "仓山万达美食", "东二环泰禾广场美食", "东街口美食", "宝龙万象城美食", "金融街万达美食", "五一广场美食"]
    for i in lists:
        down(i,"./人气排序_"+i+'.txt')

