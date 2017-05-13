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
    def get_tags_for_data(data, tag):
        soup = BeautifulSoup(data, "lxml")
        return soup.find_all(tag)

    def filter_soup_by_attribute(data, tag_type, attribute, attribute_value):
        tags = get_tags_for_data(data, tag_type)
        for tag in tags:
            try:
                if attribute_value in tag[attribute]:
                    yield tag
            except KeyError:
                pass

    relevant_td_tags = filter_soup_by_attribute(page_data, 'td', 'class', 'playertablePlayerName')
    player_tags = filter_soup_by_attribute("".join(str(td) for td in relevant_td_tags), 'a', 'playerid', '')

    return [player_tag.string for player_tag in player_tags if player_tag.string]