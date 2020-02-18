import requests
import pandas as pd
from bs4 import BeautifulSoup


def imprimir_lineup(lineup):
    print('Lineup', end=': ')

    for jogador in lineup:
        print(f'-{jogador}', end=' ')


class Main:

    url = 'https://www.hltv.org/ranking/teams/2020/february/17'

    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')

    times = soup.find_all(
        'span', attrs={'class': 'name'})

    posicoes = soup.find_all(
        'span', attrs={'class': 'position'})

    jogadores = soup.find_all(
        'table', attrs={'class': 'lineup'})

    pontos = soup.find_all(
        'span', attrs={'class': 'points'})

    print("\n< TOP#30 CSGO RANKING >")

    for x in range(0, len(times)):
        print('\n')

        print(f'{posicoes[x].text} - {times[x].text} {pontos[x].text}')

        dataframe_time = pd.read_html(str(jogadores))[x]
        imprimir_lineup(dataframe_time.values[0])


if __name__ == '__main__':
    Main()
