"""
=====================================================
Extract Data from Bronze or Silver Layer
=====================================================
Script Purpose:
    This script extracts data from a specific table stored in the 'bronze'
    or 'silver' schema and loads it into a pandas DataFrame.

    The extracted DataFrame is returned inside a dictionary, where the key
    represents the table name and the value contains its corresponding
    DataFrame.

Notes:
    - Uses SQLAlchemy to connect to the database.
    - Receives the schema and table name as parameters.
    - Retrieves all rows from the specified table.
    - Converts the query result into a pandas DataFrame.
    - Returns a dictionary containing the extracted table, allowing
      subsequent pipeline steps to process the data.
"""

from sqlalchemy import text
import pandas as pd

def execute(engine, schema: str, table_name: str) -> dict:

    # data dictionary that contains:
    # key:table_name value:dataframe of that table
    data_dict = {}

    with engine.connect() as conn:

        # retrieve all the data from the table of table in the database
        result = conn.execute(text(f'SELECT * FROM {schema}.{table_name}')).fetchall()

        # converts the data into a dataframe
        result = pd.DataFrame(result)

        # create a new key in the dictionary and assign the dataframe correspondent to that table
        data_dict[f'{table_name}'] = result
            
    return data_dict