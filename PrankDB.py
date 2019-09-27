import pymongo
import datetime

prankclient = pymongo.MongoClient("mongodb://localhost:27017/")

prankdb = prankclient["prankdatabase"]
# print(prankclient.list_database_names())

dblist = prankclient.list_database_names()

prankcol = prankdb["pranks"]

inidict = [
    {"prank": "Prank One", "timeStamp": datetime.datetime.now(), "rank": 2, "tempField": "temp"},
    {"prank": "Prank Two", "timeStamp": datetime.datetime.now(), "rank": 5, "tempField": "temp"},
    {"prank": "Prank Three", "timeStamp": datetime.datetime.now(), "rank": 3, "tempField": "temp"},
    {"prank": "Prank Four", "timeStamp": datetime.datetime.now(), "rank": 1, "tempField": "temp"},
    {"prank": "Prank Five", "timeStamp": datetime.datetime.now(), "rank": 4, "tempField": "temp"},
    {"prank": "Prank Six", "timeStamp": datetime.datetime.now(), "rank": 2, "tempField": "temp"},
    {"prank": "Prank Seven", "timeStamp": datetime.datetime.now(), "rank": 4, "tempField": "temp"},
]

# @app.route("/")
def data_ret():
    ret_list = [];
    for x in prankcol.find():
        x.pop('_id');                #Keeps or removes the _id item from the dictionary
        # print(x)
        ret_list.append(x)
    return ret_list

# print(ret_list)
print(data_ret())