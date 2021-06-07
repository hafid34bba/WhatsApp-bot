import tkinter as tk
from tkinter import filedialog

import tkinter as tk
from tkinter import filedialog
import tkinter
from tkinter import Menu,filedialog,Canvas
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd

window = tk.Tk()
file_path = ''
def get_file():
    global file_path
    file_path = filedialog.askopenfilename()
    print(file_path)

max_nb = 0
def close_window():
    global max_nb
    max_nb = int(entry.get())
    window.destroy()

    work()

def work():
    import time
    options = webdriver.ChromeOptions()
    options.add_argument('lang=en')
    # options.add_argument('--lang=en') <- Tried this option as well
    driver = webdriver.Chrome(chrome_options=options)

    import re
    driver.get('https://web.whatsapp.com/')

    time.sleep(20)

    file = pd.read_excel(file_path)

    file1 = file[file["Work=1 \ DON'T Work=0"] == 1]
    file1
    file2 = file1[file1['The number of members'] < 257]

    file2 = file2.loc[file2['Joined=1 \ Otherwis=0'] != 1]

    file2 = file2.sample(frac=1)

    links = list(file2['Group link'])
    from selenium.webdriver.common.by import By
    from selenium.webdriver.remote import webelement
    j = 0
    i = 0
    while((j<max_nb) and (i<len(links))):
        i = i+1
        j = j+1
        driver.get(links[j])
        time.sleep(10)
        act = driver.find_element_by_id("action-button")
        while (act.is_displayed() and act.is_enabled()):
            act.click()
            time.sleep(4)

        ut_what = driver.find_element_by_link_text("use WhatsApp Web")

        ut_what.click()

        time.sleep(10)

        element = driver.find_element_by_xpath("//div[@class = '_30EVj gMRg5']")
        element.click()
        time.sleep(10)
        file.loc[(file['Group link'] == links[j]), 'Joined=1 \ Otherwis=0'] = 1
    l = []
    for j in range(file.shape[0]):
        l.append(0)

    file['message_sent'] = l
    file.to_csv('tmp.csv',index=False)
    file = pd.read_csv('tmp.csv')
    file.to_excel('output_code2.xlsx',index=False)

    driver.close()




window.title('Welcome')


button_select = Menu(window)
button_selecter = Menu(button_select,tearoff=0)


button_selecter.add_command(label="ouvrir",command=get_file)
button_selecter.add_command(label="quit",command=button_select.quit())
button_select.add_cascade(label='file',menu=button_selecter)

window.config(menu=button_select)

label = tk.Label(text="nmber of groupe to add")
entry = tk.Entry()


B = tk.Button( text ="submit", command = close_window)

B.pack()

label.pack()
entry.pack()

window.mainloop()