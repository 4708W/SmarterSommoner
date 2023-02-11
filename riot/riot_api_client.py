from api.api_client import ApiClient


class RiotApiClient(ApiClient):
    """Api client for querying riot api"""
    def build_headers(self):
        return {
            # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            # "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": self.token_provider.get_token()
        }