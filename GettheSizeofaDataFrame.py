"""
DataFrame players:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
Write a solution to calculate and display the number of rows and columns of players.


"""

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    size = list(players.shape)
    
    return size
    
