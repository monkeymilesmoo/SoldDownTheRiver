from Lib import Database

def get_transactions():
    
    # Connect to the database
    cursor, connection = Database.ConnectToDatabase()

    # Construct the SQL query
    query = "SELECT * FROM Transactions ORDER BY TransactionDate DESC"
    values = ()

    # Execute the query and get the results
    cursor.execute(query, values)
    result = cursor.fetchall()
    if not result:
        result = []

    # Close the database connection
    connection.close()

    # Return the result as a list of dictionaries
    return result