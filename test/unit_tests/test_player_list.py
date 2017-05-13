from unittest.mock import patch

import player_list_data

from scraper.player_list import get_player_list

""" All text from real requests. Simply mocked here for speed, it's important unit tests run quickly. """
class MockResponse:
    text = player_list_data.player_list_request_response


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
