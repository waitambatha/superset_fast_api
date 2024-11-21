import sqlite3
import pandas as pd


# Function to create a database and table, then import data from CSV
def create_db_and_insert(csv_file, db_name='medicines.db'):
    # Connect to SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Read CSV file using pandas
    df = pd.read_csv(csv_file)

    # Check the columns in the CSV file
    print("CSV columns:", df.columns)

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS medicines")

    # Create table with column names from CSV
    columns = ', '.join([f'"{col}" TEXT' for col in df.columns])

    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS medicines (
        {columns}
    );
    '''
    print("Creating table with columns:", columns)
    cursor.execute(create_table_query)

    # Insert data into the table
    for index, row in df.iterrows():
        values = tuple(row)
        insert_query = f'''
        INSERT INTO medicines ({', '.join(df.columns)})
        VALUES ({', '.join(['?'] * len(values))});
        '''
        cursor.execute(insert_query, values)

    # Commit the transaction
    conn.commit()
    print(f"Data from {csv_file} has been inserted into the {db_name} database.")

    # Close the connection
    conn.close()


if __name__ == '__main__':
    # Specify the path to your CSV file here
    csv_file = 'med.csv'  # Update with your file path
    create_db_and_insert(csv_file)
