from api.riot_api_client import RiotApiClient


def get_match_id_by_player(puuid: str) -> str:
    """returns match ids"""
    base_url = "https://americas.api.riotgames.com"
    endpoint = f"/lol/match/v5/matches/by-puuid/{puuid}/ids"
    api = RiotApiClient(base_url)
    params = { "start": 0, "count": 100  }
    return api.get(endpoint, params).json()


if __name__ == "__main__":
    # start date should be one day after the latest date from idx table
    start_date = "2023-01-01"
    
    # end date should be yesterday
    end_date = "2023-02-10"

    # create date series

    # loop the data series

    # for each day, download the match id for each player, and save them in sqlite

    # (date, puuid, mid)
