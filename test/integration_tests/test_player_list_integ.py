from scraper.player_list import get_player_list


def test_get_player_list(*args, **kwargs):
    player_list = get_player_list(team_url="http://games.espn.com/flb/clubhouse?leagueId=13127&teamId=11&seasonId=2017")

    # Undroppables, should always be in the list
    assert "Miguel Cabrera" in player_list
    assert "Madison Bumgarner" in player_list
