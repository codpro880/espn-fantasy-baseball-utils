from unittest.mock import patch

import response_data

from scraper.opposing_pitcher_list import get_matchups


class MockOppPitchResponse:
    text = response_data.opp_pitch_request_response


@patch('requests.get', autospec=True, return_value=MockOppPitchResponse())
def test_opp_pitcher_list(*args, **kwargs):
    matchups = get_matchups(team_url="http://games.espn.com/flb/clubhouse?leagueId=13127&teamId=11&seasonId=2017")

    # Looked at my ESPN page on 5/13/2017 to assert these a priori
    assert matchups[0] == "Teheran"
    assert matchups[-1] == "Bonilla"