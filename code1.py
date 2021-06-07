from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from tkinter import filedialog
import tkinter as tk
from tkinter import Menu,filedialog,Canvas
import time

file_path = ''
def get_file():
    global file_path
    file_path = filedialog.askopenfilename()
    print(file_path)

    window.destroy()

    work()

def work():
    options = webdriver.ChromeOptions()
    options.add_argument('lang=en')
    # options.add_argument('--lang=en') <- Tried this option as well
    driver = webdriver.Chrome(chrome_options=options)
    import time
    import re
    driver.get('https://web.whatsapp.com/')

    time.sleep(20)

    file = pd.read_excel(file_path)

    file = file.dropna(subset=['Group link'])

    file = file[file['Group link'].astype(str).str.startswith('https://chat.whatsapp.com')]

    links = list(file['Group link'])
    len(links)

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    i = 0

    nmb_users = []
    is_group = []
    names = []

    for j in range(len(links)):

        driver.get(links[j])
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

        txt1 = soup.findAll('div', {'class': '_2fuxX'})

        name_of_group = ''
        nb_prs = 0

        if (txt1[0].text != "You can't join this group because this invite link was reset.") and (
                txt1[0].txt != "Vous ne pouvez pas intégrer ce groupe car ce lien d'invitation a été réinitialisé.") and (
                txt1[0].txt != "Couldn't join this group. Please try again."):

            if (str(txt1[0].txt) == "None") and (len(soup.findAll('span', {'class': '_32Hpp _1VzZY'})) > 0):

                name_of_group = soup.findAll('span', {'class': '_32Hpp _1VzZY'})[0].text
                nb_prs = int(soup.findAll('span', {'class': '_1348Y'})[0].text.split(' ')[0])

                is_group.append(1)
            else:
                is_group.append(0)

        else:
            txt = soup.findAll('div', {'class': '_2fuxX'})[0].text

            is_group.append(0)

        nmb_users.append(nb_prs)
        names.append(name_of_group)



    file["Work=1 \ DON'T Work=0"] = is_group
    file["Group Name"] = names
    file["The number of members"] = nmb_users


    file.to_csv('tmp.csv',index=False)
    file=pd.read_csv('tmp.csv')

    file.to_excel('output_code1.xlsx',index=False)
    driver.close()



window = tk.Tk()


window.title('Welcome')


button_select = Menu(window)
button_selecter = Menu(button_select,tearoff=0)


button_selecter.add_command(label="ouvrir",command=get_file)
button_selecter.add_command(label="quit",command=button_select.quit())
button_select.add_cascade(label='file',menu=button_selecter)

window.config(menu=button_select)
window.mainloop()