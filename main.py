import itertools
import pandas as pd

from dotenv import load_dotenv
from api.riot_api_client import RiotApiClient

# todo: try except raise assert api key there
load_dotenv()


def get_summoner_puuid(summoner_name: str) -> str:
    """returns player id"""
    base_url = "https://na1.api.riotgames.com"
    endpoint = f"lol/summoner/v4/summoners/by-name/{summoner_name}"
    api = RiotApiClient(base_url)
    return api.get(endpoint).json()["puuid"]




if __name__ == "__main__":
    # get a match
    results = []
    match_ids = [
        "NA1_4574135601",
    ]
    for match_id in match_ids:
        match_dto = get_match(match_id)
        
        match_id = match_dto["metadata"]["matchId"]
        participants = match_dto["metadata"]["participants"]
        win = [ i["win"] for i in match_dto["info"]["participants"] ]

        records = zip(itertools.repeat(match_id), participants, win)


        # append match id
        pd.DataFrame(records, columns=["match_id", "puuid", "win"])


        # results.append({
        #     "match_id": ,
        #     "participants": match_dto["metadata"]["participants"],
        #     "win":  [ i["win"] for i in match_dto["info"]["participants"] ]
        # })

    print()
