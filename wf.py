#!/usr/local/bin/python3
# coding: utf-8 

from requests import get
from fuzzywuzzy import fuzz
from googlesearch import search
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init

# colorama
init(autoreset=True)

# Logo
print(Fore.YELLOW + '''
┌──────────────────────────────────────────────────────────────────┐
│ _       _____    _   ___   _____       ___________   ______  ___ │
│| |     / /   |  / | / / | / /   |     / ____/  _/ | / / __ \/__ \│
│| | /| / / /| | /  |/ /  |/ / /| |    / /_   / //  |/ / / / / / _/│
│| |/ |/ / ___ |/ /|  / /|  / ___ |   / __/ _/ // /|  / /_/ / /_/  │
│|__/|__/_/  |_/_/ |_/_/ |_/_/  |_|  /_/   /___/_/ |_/_____/ (_)   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
                                   Created by 
''' )

query   = input(Back.BLACK + Fore.YELLOW + 'Найти > ' + Back.RESET + Fore.WHITE)
results = 100

print(Fore.GREEN + '[~] Поиск... ' + query)
for url in search(query, stop = results):
	print('\n' + Fore.CYAN + '[+] URL найден: ' + url)
	try:
		text = get(url, timeout = 1).text
	except:
		continue
	soup = BeautifulSoup(text, "html.parser")
	links_detected = []
	try:
		print(Fore.MAGENTA + '[?] Оглавление: ' + soup.title.text.replace('\n', ''))
	except:
		print(Fore.RED + '[?] Оглавление: отсутствует')
	# Find by <a> tags
	try:
		for link in soup.findAll('a'):
			href = link['href']
			if not href in links_detected:
				if href.startswith('http'):
					# Filter
					if url.split('/')[2] in href:
						links_detected.append(href)
					# If requested data found in url
					elif query.lower() in href.lower():
						print(Fore.GREEN + '--- Запрошенные данные найдены по ссылке: ' + href)
						links_detected.append(href)
					# If text in link and link location is similar
					elif fuzz.ratio(link.text, href) >= 60:
						print(Fore.GREEN + '--- Текст и ссылка похожи: ' + href)
						links_detected.append(href)
	except:
		continue
	if links_detected == []:
		print(Fore.RED + '--- Не найдено')



	
#for s in links_detected: print(s)

	
