def get_mongodb():
    try:
        f = open("mongoDBServer.txt", "r")
        apikey = f.read()
        f.close()
        return apikey
    except:
        print("error no mongoDb server specified try running comand \'python .\getMongoBD.py\'")
        exit(1)

if __name__ == "__main__":
    mongoDB = input("Please enter your local mongoDB server url or a cluster url from https://www.mongodb.com/. The name of the database in the cluster's url can be anythign: \n")
    f = open("ApiKey.txt", "w")
    f.write(mongoDB)
    f.close()