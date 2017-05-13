from unittest.mock import patch

from scraper.player_list import get_player_list, get_matchups
import player_list_data

""" All text from real requests. Simply mocked here for speed, it's important unit tests run quickly. """
class MockResponse:
    text = player_list_data.player_list_request_response

class MockOppPitchResponse:
    text = player_list_data.opp_pitch_request_response

@patch('requests.get', autospec=True, return_value=MockResponse())
def test_get_player_list(*args, **kwargs):
    player_list = get_player_list(team_url="http://games.espn.com/flb/clubhouse?leagueId=13127&teamId=11&seasonId=2017")

    # Undroppables, should always be in the list
    assert "Miguel Cabrera" in player_list
    assert "Madison Bumgarner" in player_list

@patch('requests.get', autospec=True, return_value=MockResponse())
def test_player_list_behaves_like_list(*args, **kwargs):
    player_list = get_player_list(team_url="http://games.espn.com/flb/clubhouse?leagueId=13127&teamId=11&seasonId=2017")
    assert player_list[player_list.index("Miguel Cabrera")] == "Miguel Cabrera"

@patch('requests.get', autospec=True, return_value=MockResponse())
def test_player_list_doesnt_contain_nones(*args, **kwargs):
    player_list = get_player_list(team_url="http://games.espn.com/flb/clubhouse?leagueId=13127&teamId=11&seasonId=2017")
    assert None not in player_list

@patch('requests.get', autospec=True, return_value=MockOppPitchResponse())
def test_opp_pitcher_list(*args, **kwargs):
    matchups = get_matchups(team_url="http://games.espn.com/flb/clubhouse?leagueId=13127&teamId=11&seasonId=2017")

    # Looked at my ESPN page on 5/13/2017 to assert these a priori
    assert matchups[0] == "Teheran"
    assert matchups[-1] == "Bonilla"
