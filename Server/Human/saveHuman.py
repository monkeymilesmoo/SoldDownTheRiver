import uuid
from Lib import Database

def save_human(HumanId, FirstName, MiddleName, LastName):
    # Connect to the database
    cursor, connection = Database.ConnectToDatabase()

    # Check if the HumanId is present
    if HumanId:
        # If the HumanId is present, update the existing human
        query = "UPDATE Humans SET FirstName = %s, MiddleName = %s, LastName = %s WHERE HumanId = %s"
        values = (FirstName, MiddleName, LastName, HumanId)
    else:
        # If the HumanId is not present, create a new human
        HumanId = str(uuid.uuid4())
        query = "INSERT INTO Humans (HumanId, FirstName, MiddleName, LastName) VALUES (%s, %s, %s, %s)"
        values = (HumanId, FirstName, MiddleName, LastName)

    # Execute the query and commit the changes
    cursor.execute(query, values)
    connection.commit()

    # Close the database connection
    connection.close()

    # Return the HumanId as a JSON response
    return {'success': True, 'HumanId': HumanId}
