import requests

def get_page_data(team_url):
    html_data = requests.get(team_url).text
    return html_data