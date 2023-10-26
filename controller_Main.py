import json
import pyodbc

# DatabaseConnection class for managing database connections
class DatabaseConnection:
    # Singleton instance variable
    _instance = None

    # Create a new instance if one doesn't exist
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = cls._create_connection()
        return cls._instance

    # Private method to create a database connection
    @staticmethod
    def _create_connection():
        # Read database connection configuration from a JSON file
        with open('config.json') as config_file:
            config = json.load(config_file)
        connection_string = config['connection_string']
        # Establish a connection using PyODBC
        return pyodbc.connect(connection_string)

    # Execute a query on the database
    def execute_query(self, query):
        # Create a cursor to interact with the database
        cursor = self.connection.cursor()
        cursor.execute(query)
        # Fetch the query results
        result = cursor.fetchall()
        # Close the cursor
        cursor.close()
        # Return the query results
        return result
