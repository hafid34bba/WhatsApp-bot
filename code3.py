import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import tkinter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os



from tkinter import Menu,filedialog,Canvas
window = tk.Tk()
file_path = ''
def get_file():
    global file_path
    file_path = filedialog.askopenfilename()
    print(file_path)
file_path1 = ''
def get_file1():
    global file_path1
    file_path1 = filedialog.askopenfilename()
    print(file_path1)

max_nb = 0
nb_sec = 0
def close_window():
    global max_nb
    global nb_sec
    nb_sec = int(entry1.get())
    max_nb = int(entry.get())
    window.destroy()


    work()
from selenium.webdriver.common.action_chains import ActionChains
def work():
    def paste_keys( xpath, text):

        el = driver.find_element_by_xpath(xpath)
        command = 'echo | set /p nul=' + text.strip() + '| clip'
        os.system(command)
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    options = webdriver.ChromeOptions()
    options.add_argument('lang=en')
    # options.add_argument('--lang=en') <- Tried this option as well
    driver = webdriver.Chrome(chrome_options=options)
    import time
    import re
    driver.get('https://web.whatsapp.com/')
    time.sleep(20)
    print('here1')
    file = pd.read_excel(file_path)
    print('no')
    file1 = file[file["Work=1 \ DON'T Work=0"] == 1]
    file1
    file2 = file1[file1['The number of members'] < 257]

    file2 = file2.loc[file2['Joined=1 \ Otherwis=0'] == 1]

    file2 = file2.loc[file2['message_sent']==0]

    file2 = file2.sample(frac=1)

    links = list(file2['Group link'])
    j = 0
    i = 0
    string = ""
    print('here')
    fl = open(file_path1,'r',encoding='utf-8')
    l = fl.readlines()
    for k in range(len(l)):
        string += l[k]

    while ((j < max_nb) and (i < len(links))):
        print(i)
        driver.get(links[i])
        time.sleep(10)
        act = driver.find_element_by_id("action-button")
        while (act.is_displayed() and act.is_enabled()):
            act.click()
            time.sleep(4)

        ut_what = driver.find_element_by_link_text("use WhatsApp Web")

        ut_what.click()

        time.sleep(15)

        content = driver.page_source
        soup = bs(content)

        count = soup.findAll('div', attrs={'class': '_1awRl copyable-text selectable-text'})
        if len(count) > 1:
            print('you can send messages')


            inp_xpath = '//div[@class="_1awRl copyable-text selectable-text"][@dir="ltr"][@data-tab="6"]'

            input_box = driver.find_element_by_xpath(inp_xpath)
            for m in range(1):
                input_box.send_keys(string.strip() + Keys.ENTER)

                time.sleep(nb_sec+1)
            time.sleep(5)
            file.loc[(file['Group link'] == links[j]), 'message_sent'] = 1

        else:
            time.sleep(4)
            bt = driver.find_elements_by_xpath('//div[@class="_2Gdma _2amHe"]')

            bt[0].click()
            time.sleep(20)
            bt1 = driver.find_elements_by_xpath('//span[@class="_3Tk1z _1WmI4 _27rts"]')
            bt1[0].click()
            time.sleep(5)
            bt2 = driver.find_elements_by_xpath('//div[@role="button"][@tabindex="0"][@class="_30EVj gMRg5"]')
            bt2[0].click()

            file = file.loc[file["Group link"] != links[j]]

        i = i + 1
        j = j + 1

    file.to_csv('tmp.csv', index=False)
    file = pd.read_csv('tmp.csv')
    file.to_excel('output_code3.xlsx', index=False)











window.title('Welcome')


button_select = Menu(window)
button_selecter = Menu(button_select,tearoff=0)


button_selecter.add_command(label="xsl_file",command=get_file)
button_selecter.add_command(label="txt_file",command=get_file1)
button_select.add_cascade(label='file',menu=button_selecter)

window.config(menu=button_select)



label = tk.Label(text="nmber of groupe to send msg")
entry = tk.Entry()
label1 = tk.Label(text="nb_sec between messages")
entry1 = tk.Entry()

B = tk.Button( text ="submit", command = close_window)

B.pack()

label.pack()
entry.pack()
label1.pack()
entry1.pack()


window.mainloop()