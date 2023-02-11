from api.token_provider import RiotTokenProvider
from dotenv import load_dotenv

from riot.riot_api_client import RiotApiClient

if __name__ == "__main__":
    load_dotenv()

    api = RiotApiClient(base_url="https://na1.api.riotgames.com/lol/", token_provider=RiotTokenProvider())
    
    # here is my uuid
    results = api.get("summoner/v4/summoners/by-name/SchroDog2")
    print()

    # get match history
    
