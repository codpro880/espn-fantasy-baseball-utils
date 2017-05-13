from scraper.soup_utils import get_page_data


def get_matchups(team_url):
    page_data = get_page_data(team_url)
    opposing_pitchers = _parse_data_for_opp_pitch(page_data)
    return opposing_pitchers

def _parse_data_for_opp_pitch(page_data):
    # Cheated quite a bit here (i.e. no BeautifulSoup parsing), but this seemed fastest/clearest.
    filtered = [data for data in page_data.split("(") if '<a href=""' in data and "</a>)" in data]
    filtered_splits = [f.split("</a>)") for f in filtered]
    opp_pitchers = [li[0].split('cache="true">')[-1] for li in filtered_splits]

    return opp_pitchers