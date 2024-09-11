import time
import requests
from bs4 import BeautifulSoup

from .urlHelper import getUrl
from .excel import saveToExcel


def main(params):
    # start fetching
    print('fetching data...')

    profiles = []
    i = int(params['start'])
    stop = False
    while not stop:
        # get url
        params['start'] = str(i)
        url = getUrl(params)
        print(url)
        
        # send GET request
        time.sleep(2)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # get all profiles
        data = soup.find_all('div', class_='Gx5Zad xpd EtOod pkphOe')[1:]
        for element in data:
            # find data
            name = element.find('div', class_='BNeawe vvjwJb AP7Wnd').getText()
            infos = element.find('div', class_='BNeawe vvjwJb AP7Wnd').getText()
            link = 'https' + str(element.find('a', href=True)['href'].split('https', 1)[1].split('&', 1)[0])
            
            # add to list
            profil = {
                'name': name,
                'infos': infos,
                'link': link,
            }
            profiles.append(profil)
            
            # suivant
            i += 1
            
            # found all required
            if i == params['nb']:
                stop = True
                break
        
        # print end of get page
        print(f"{i}/{params['nb']}")


    # end of getting data
    print('End of fetch !')

    # save
    saveToExcel(profiles, params)