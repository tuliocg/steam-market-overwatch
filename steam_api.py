
import re
import os
from bs4 import BeautifulSoup
 
def get_weapon_list():
    id_terraz = []
    browser = webdriver.Firefox()
    num_aps = 0

    for bairro in bairros_terraz:


        print('URL: {}'.format(url))

        browser.get(url)
        delay = 10
        for i in range(20):
            step = i * 400
            browser.execute_script("window.scrollTo(0, "+str(step)+");")

        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'styles__footer___28vDB')))

        soup = BeautifulSoup(browser.page_source, "html.parser")

        try:
            num_aps = int(re.findall(r"\d+", str(soup.find_all("span", {'class': "styles__underline___3_JPa"})))[1]) + num_aps

            for link in soup.find_all("div", {'class': "styles__title___k97NL"}):
                id_terraz.append(int(re.findall(r"\d+", link.get_text())[0]))
        except:
            print('Bairro {} não encontraod'.format(bairro))
