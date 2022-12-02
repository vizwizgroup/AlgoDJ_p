import uuid
import pandas as pd


def dict_to_df(Object)-> pd.DataFrame:
    return pd.DataFrame.from_dict(Object)


def generate_id()-> str:
    return str(uuid.uuid4())

def check_status(code) -> bool:
    status = False
    return status

def create_user(Object, status) -> pd.DataFrame:
    user_id = generate_id()
    playlist_id = generate_id()
    user_add = {"user_id":user_id, "playlist_id": playlist_id, "reg_status":check_status(user_id)}
    user_update = user_add.update(Object)
    user_row = {k:[v] for k,v in user_add.items()}
    df = pd.DataFrame.from_dict(user_row)
    return df





def update_df(df1, df2) -> pd.DataFrame:
    if isinstance(df1, pd.DataFrame) and isinstance(df2, pd.DataFrame):
        updated_df = pd.concat(df1, df2)
        return updated_df
    raise TypeError("update_df takes only 2 arguments of type: pd.DataFrame")



if __name__ == '__main__':
    a = {'playlist_size': '6', 'yr_from': '1957', 'yr_to': '1963', 'genre': 'Metal', 'title': 'Anti-Hero', 'song_sample': None, 'age': '15', 'gender': 2}
    print(create_user(a, False))
    print("Hello")