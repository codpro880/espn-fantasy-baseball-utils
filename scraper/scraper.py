import requests
from bs4 import BeautifulSoup

def get_player_list(team_url):
    page_data = _get_page_data(team_url)
    player_list = _parse_page_data(page_data)
    return player_list

def _get_page_data(team_url):
    html_data = requests.get(team_url).text
    return html_data

def _parse_page_data(page_data):
    soup = BeautifulSoup(page_data, "lxml")
    all_tds = soup.find_all('td')
    def filter_by_attribute(tags, attribute, attribute_value):
        for tag in tags:
            try:
                if attribute_value in tag[attribute]:
                    yield tag
            except KeyError:
                pass

    relevant_tds = list(filter_by_attribute(all_tds, 'class', 'playertablePlayerName'))
    print("tds: ", list(relevant_tds))

    td_soup = BeautifulSoup("".join(str(relevant_tds)))
    all_a_in_td = td_soup.find_all('a')
    players = []
    for a in all_a_in_td:
        try:
            if a['playerid']:
                players.append(a.string)
        except KeyError:
            pass

    return players