from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

driver= webdriver.Chrome()

import re
driver.get('https://web.whatsapp.com/')

time.sleep(60)

file = pd.read_excel('C:\\Users\\hp 840\\Desktop\\البرنامج\\الاول\\The sample of xlsx file of whatsapp Groups.xlsx')

file = file.dropna(subset=['Group link'])

file = file[file['Group link'].astype(str).str.startswith('https://chat.whatsapp.com')]
file = file.loc[file['Joined=1 \ Otherwis=0']!=1]

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



    ut_what = driver.find_element_by_link_text("utilisez WhatsApp Web")

    ut_what.click()


    time.sleep(10)

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


file.to_csv('C:\\Users\\hp 840\\Desktop\\البرنامج\\الاول\\names_and_nb_mbr_pych.csv')
file=pd.read_csv('C:\\Users\\hp 840\\Desktop\\البرنامج\\الاول\\names_and_nb_mbr_pych.csv')

file.to_excel('C:\\Users\\hp 840\\Desktop\\البرنامج\\الاول\\names_and_nb_mbr_pych.xlsx')