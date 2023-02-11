from abc import ABC, abstractmethod
import os


class TokenProvider(ABC):
    """Base token provider class"""
    def __init__(self) -> None:
        self.token = None
        self.auth_method = None

    def get_token(self) -> str:
        """request a newtoken if cached token is timed out.
        Otherwise, returns cached token
        """
        if self.is_token_expired():
            self.token = self.request_new_token()
        return self.token
    
    @abstractmethod
    def request_new_token(self) -> str:
        pass

    def is_token_expired(self) -> bool:
        """Defaults to True"""
        return True


class RiotTokenProvider(TokenProvider):
    """Reads token from API key"""
    def request_new_token(self) -> None:
        return os.environ["API_KEY"]
    