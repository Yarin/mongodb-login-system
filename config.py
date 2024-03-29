import json

class Config:
    def __init__(self):
        with open("config.json", 'r') as f:
            self.data = json.load(f)
    
    def get_mongodb_link(self):
        """get_mongodb_link get the MongoDB connection link to connect to DB with pymongo

        Returns:
            str: connection link
        """
        return self.data["mongodb-link"]
    
    def get_db_name(self):
        """get_db_name get the database name from MongoDB cluster

        Returns:
            str: database name
        """
        return self.data["db-name"]
    
    def get_collection(self):
        """get_collection get collection name from cluster.database

        Returns:
            str: collection name
        """
        return self.data["collection"]
        