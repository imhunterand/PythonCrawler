import pandas as pd

def save_to_csv(data, filename='output.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def save_to_database(data, db_name='crawler.db'):
    import sqlite3
    conn = sqlite3.connect(db_name)
    df = pd.DataFrame(data)
    df.to_sql('web_data', conn, if_exists='replace', index=False)
    conn.close()
