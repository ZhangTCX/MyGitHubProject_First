from selenium import webdriver
import random
import time


AA='/html/body/form/div[5]/div[3]/fieldset/div[1]/div[2]/div[%s]/span/a'
BB='/html/body/form/div[5]/div[3]/fieldset/div[2]/div[2]/div[%s]/span/a'
CC='/html/body/form/div[5]/div[3]/fieldset/div[3]/div[2]/div[%s]/span/a'
DD='/html/body/form/div[5]/div[3]/fieldset/div[4]/div[2]/div[%s]/span/a'
EE='/html/body/form/div[5]/div[3]/fieldset/div[5]/div[2]/div[%s]/span/a'
FF='/html/body/form/div[5]/div[3]/fieldset/div[6]/div[2]/div[%s]/span/a'
GG='/html/body/form/div[5]/div[3]/fieldset/div[7]/div[2]/div[%s]/span/a'
HH='/html/body/form/div[5]/div[3]/fieldset/div[8]/div[2]/div[%s]/span/a'
II='/html/body/form/div[5]/div[3]/fieldset/div[9]/div[2]/div[%s]/span/a'
JJ='/html/body/form/div[5]/div[3]/fieldset/div[10]/div[2]/div[%s]/span/a'
KK='/html/body/form/div[5]/div[3]/fieldset/div[11]/div[2]/div[%s]/span/a'
LL='/html/body/form/div[5]/div[3]/fieldset/div[12]/div[2]/div[%s]/span/a'
MM='/html/body/form/div[5]/div[3]/fieldset/div[13]/div[2]/div[%s]/span/a'
NN='/html/body/form/div[5]/div[3]/fieldset/div[14]/div[2]/div[%s]/span/a'
OO='/html/body/form/div[5]/div[3]/fieldset/div[15]/div[2]/div[%s]/span/a'
PP='/html/body/form/div[5]/div[3]/fieldset/div[16]/div[2]/div[%s]/span/a'
QQ='/html/body/form/div[5]/div[3]/fieldset/div[17]/div[2]/div[%s]/span/a'
RR='/html/body/form/div[5]/div[3]/fieldset/div[18]/div[2]/div[%s]/span/a'

def Click(url):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('user-agent="Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"')
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver',options=option)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)  # 最多等待时间 页面加载时间
    # 1
    Justone(driver, 2, AA)
    # 2
    Justone(driver, 1, BB)
    # 3
    # Nornoal(driver, 2, 3, CC)
    # 4
    Nornoal(driver,1,2,DD)
    # 5
    Nornoal(driver,2,3,EE)
    # 6、
    Choose(driver,[1,3],FF)
    # 7
    Nornoal(driver,1,2,GG)
    # 8
    Manychoice(driver,3,HH)
    # 9
    Cmanychoice(driver,[2,4],II)
    # 10
    Cmanychoice(driver,[3,4,9,10],JJ)
    # 11
    Nornoal(driver,3,4,KK)
    # 12
    Nornoal(driver,1,5,LL)
    # 13
    Nornoal(driver,1,2,MM)
    # 14
    Manychoice(driver, 5, NN)
    # 15
    Nornoal(driver,1,2,OO)
    # 16
    Nornoal(driver,1,2,PP)
    # 17
    Manychoice(driver, 5, QQ)
    # 18
    Justone(driver, 2, RR)
    # 19
    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))
    driver.quit()

#只适合单选题：当你只想固定选择一个选项的时候
def Justone(driver,num,listnum):
    driver.find_element_by_xpath(listnum % num).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

#只适合单选题：当你想在几个选项里面随机选择
def Nornoal(driver,numone,numtwo,listnum):
    thenum = str(random.randint(numone,numtwo))
    driver.find_element_by_xpath(listnum%thenum).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

#只适合单选题：选择哪个几个
def Choose(driver,islist,listnum):
    randomnum = int(random.randint(0, len(islist)-1))
    num = islist[randomnum]
    driver.find_element_by_xpath(listnum % num).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

def Manychoice(driver,i,listnum):
    randomnum = int(random.randint(1, i))
    randomlist = range(1, i+1)
    wantnum = random.sample(randomlist, randomnum)  # randomnum是你想随机想选出的个数
    for temp in wantnum:
        num = str(temp)
        driver.find_element_by_xpath(listnum % num).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))

def Cmanychoice(driver,islist,listnum):
    randomnum = int(random.randint(1, len(islist)))
    randomlist = range(1, len(islist)+1)
    wantnum = random.sample(randomlist, randomnum)  # randomnum是你想随机想选出的个数
    for temp in wantnum:
        num = str(temp)
        driver.find_element_by_xpath(listnum % num).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))

if __name__ == '__main__':
    url = "https://www.wjx.cn/m/69786397.aspx?from=timeline"
    for i in range(20):#输入数字
        try:
            t1 = time.time()
            Click(url)
            t2 = time.time()
            t3 = str(t2 - t1)
            print("第%s次填写,耗时：%s" % (str(i), t3))
        except Exception as e:
            print(e)
            continue