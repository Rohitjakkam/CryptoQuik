# Mock Kraken API
from .trade import Trade
from datetime import datetime
from time import sleep
from typing import List

class KrakenMockAPI:
    def __init__(self,pair: str):
        self.pair = pair

    def get_trades(self) -> List[Trade]:
        """
        Returns a list of mock trades.
        """
        mock_trades = [
            Trade(pair=self.pair, price=0.5117, volume=40.0, timestamp=datetime(2023, 9, 25, 7, 49, 37, 708706), timestamp_ms=172728957708706),
            Trade(pair=self.pair, price=0.4217, volume=40.0, timestamp=datetime(2023, 9, 25, 7, 49, 37, 708706), timestamp_ms=172728957708706),
            Trade(pair=self.pair, price=0.6717, volume=40.0, timestamp=datetime(2023, 9, 25, 7, 49, 37, 708706), timestamp_ms=172728957708706),
        ]
        sleep(1)
        return mock_trades
