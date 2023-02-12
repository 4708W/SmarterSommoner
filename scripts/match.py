import time
import itertools
import sqlite3
import pandas as pd

from api.riot_api_client import RiotApiClient


# todo: store all information. do not lose info
def get_match_by_id( match_id: str ) -> tuple[str, str, str]:
    base_url = "https://americas.api.riotgames.com"
    api = RiotApiClient(base_url)
    endpoint = f"/lol/match/v5/matches/{match_id}"
    match_dto = api.get(endpoint).json()  
    match_id = match_dto["metadata"]["matchId"]
    participants = match_dto["metadata"]["participants"]
    win = [ i["win"] for i in match_dto["info"]["participants"] ]
    return list(zip(itertools.repeat(match_id), participants, win))


if __name__ == "__main__":
    # todo: read from db the matchids that haven't been fetched yet
    with open("db/20230210_match_ids.txt", "r") as f:
        mids = f.readlines()
    
    records = []
    for mid in mids:
        records.extend(get_match_by_id(mid))
        time.sleep(1)

    data = pd.DataFrame(records, columns=["mid", "puuid", "win"])

    with sqlite3.connect("db/match.db") as con:
        data.to_sql("match", con, if_exists="replace")
