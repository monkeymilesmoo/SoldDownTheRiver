from Lib import Database

def get_human(HumanId):
	if not HumanId:
		HumanId="-1"
	
	# Connect to the database
	cursor, connection = Database.ConnectToDatabase()

	# Construct the SQL query
	query = "SELECT * , (select max(dateAdded) from History where History.KeyValue=Humans.HumanId and History.TableName='Humans' and History.KeyName='HumanId') LastModified"
	query +=" FROM Humans left join HumanRoles on Humans.HumanId=HumanRoles.HumanId WHERE Humans.HumanId = %s"
	values = (HumanId,)
	print(query % values)
	# Execute the query and get the results
	cursor.execute(query, values)
	result = cursor.fetchone()
	if not result:
		result={}
		
	# Close the database connection
	connection.close()
	
	# Return the result as a dictionary
	return result
