import pandas as pd
import sqlite3
import os

def csv_to_sqlite(csv_file, db_name, table_name):
    if not os.path.exists(csv_file):
        print(f"File {csv_file} does not exist.")
        return

    df = pd.read_csv(csv_file)
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    print(f"Data from {csv_file} has been successfully written to {table_name} table in {db_name} database.")

if __name__ == "__main__":
    # List of CSV files and their corresponding table names
    csv_files = [
        ('csv_tables/fifa_world_cup_matches_modified.csv', 'matches'),
        ('csv_tables/fifa_world_cup_goalscorers.csv', 'goalscorers'),
        ('csv_tables/world_cup_penalties.csv', 'penalties')
    ]
    db_name = 'fifa.db'

    for csv_file, table_name in csv_files:
        csv_to_sqlite(csv_file, db_name, table_name)
