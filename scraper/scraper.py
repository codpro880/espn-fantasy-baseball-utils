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
    def filter_by_attribute(tags, attribute, attribute_value):
        for tag in tags:
            try:
                if attribute_value in tag[attribute]:
                    yield tag
            except KeyError:
                pass

    def get_soup_for_tag(data, tag):
        soup = BeautifulSoup(data, "lxml")
        return soup.find_all(tag)

    all_tds = get_soup_for_tag(page_data, 'td')
    relevant_tds = filter_by_attribute(all_tds, 'class', 'playertablePlayerName')

    all_a_in_td = get_soup_for_tag("".join([str(td) for td in relevant_tds]), 'a')
    player_tags = filter_by_attribute(all_a_in_td, 'playerid', '')

    players = [player_tag.string for player_tag in player_tags if player_tag.string]

    return players