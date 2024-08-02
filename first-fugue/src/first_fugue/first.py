import pandas
import fugue

import pandas as pd
from typing import Dict

input_df = pd.DataFrame({"id":[0,1,2], "value": (["A", "B", "C"])})
map_dict = {"A": "Apple", "B": "Banana", "C": "Carrot"}

def map_letter_to_food(df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
    df["value"] = df["value"].map(mapping)
    return df
  
print(map_letter_to_food(input_df,map_dict))


import pandas as pd
from fugue import transform
from fugue_spark import SparkExecutionEngine

data = pd.DataFrame({'numbers':[1,2,3,4], 'words':['hello','world','apple','banana']})

# schema: *, reversed:str
def reverse_word(df: pd.DataFrame) -> pd.DataFrame:
    df['reversed'] = df['words'].apply(lambda x: x[::-1])
    return df

spark_df = transform(data, reverse_word, engine=SparkExecutionEngine())