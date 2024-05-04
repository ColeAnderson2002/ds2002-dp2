from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

# specify a database
db = client.kbv4nd

dp2collection = db['dp2collection']

path = "/workspace/ds2002-dp2/data"

def read_from_mongo(path, filename):
        filename = os.path.join(path, filename)
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    if isinstance(data, list):
                        try:
                            dp2collection.insert_many(data)
                        except Exception as e:
                            print(f'Mongo Error {e}')
                    else:
                        try:
                            dp2collection.insert_one(data)
                        except Exception as e:
                            print(f'Mongo Error {e}')
                except Exception as e:
                    print(f'Json Error: {e}')
        except Exception as e:
            print(e)
        finally:
            if 'file' in locals():  # Check if 'file' variable exists (was opened)
                file.close()  # Close the file if it was opened

if __name__ == "__main__":
    for file in os.listdir(path):
        read_from_mongo(path, file)
