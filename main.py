import requests
import bs4


def insert_icao():
    icao = input('Digite o código ICAO de um aeroporto: ')
    return icao


def get_request(icao):
    response = requests.get("https://aisweb.decea.mil.br/?i=aerodromos&codigo=" + icao)
    return response


def beautifoul_request(response):
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return soup


def get_show_sunrise_sunset(soup):
    sunrise = soup.find_all('sunrise')[0].string
    sunset = soup.find_all('sunset')[0].string
    print('nascer do sol : ', sunrise)
    print('por do sol : ', sunset)


def get_show_cartas(soup):
    cartas = soup.find_all('a', {'title': 'Uso Ostensivo'})
    print('Cartas encontradas :  Links para downloads')
    for carta in cartas:
        print(carta.string, ': ', carta['href'])


def get_show_metar_taf(soup):
    metar_taf = soup.find_all('h5', {'class': 'mb-0 heading-primary'})
    print(metar_taf[0].text)
    print(metar_taf[0].findNext('p').text)
    print(metar_taf[1].text)
    print(metar_taf[1].findNext('p').text)


cod = insert_icao()
request_cod = get_request(cod)
soup_response = beautifoul_request(request_cod)
get_show_cartas(soup_response)
get_show_sunrise_sunset(soup_response)
get_show_metar_taf(soup_response)