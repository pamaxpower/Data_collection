from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

db = client.steam

def find():
    # Игра с более 500000 положительных отзывов
    #query = {"positive" : {"$gt" : 500000, "$lte" : 600000}}
    # название игр она A,B,C
    #query = {"name" : {"$gte" : "A", "$lt" : "D"}}
    # игры с возрастом неравным 0
    #query = {"required_age" : {"$ne" : 0}}
    # 
    #query = {"tags" : {"$exists" : 1}}
    # все игры со словом Puzzle (и puzzle)
    #query = {"name" : {"$regex" : "[Pp]uzzle"}}
    # все игры со словом Puzzle/puzze и Game/game
    #query = {"name" : {"$regex" : "[Pp]uzzle | [Gg]ame"}}
    # Поиск по категориям
    #query = {"categories" : "Co-op"}
    # поиск по нескольким значениям в категории (или то или то)
    #query = {"categories" : {"$in" : ["Co-op", "Online PvP"]}}
    # поиск сразу по всем значениям
    query = {"categories" : {"$all" : ["Co-op", "Remote Play on Tablet", "Steam Achievements"]}}
    # 
    #query = {"categories" : {"$all" : ["Steam Trading Cards", "Co-op", "Remote Play on Tablet", "Steam Achievements"]}}
    # 
    #query = {"type" : {"$ne" : "game"}}


    projection = {"_id" : 0, "name" : 1}

    games = db.games.find(query, projection)
    
    num_games = 0
    for i in games:
        print(i)
        num_games += 1
        
    print('Число игр: %d' % num_games)

    for a in games:
        print(a)
        
if __name__ == '__main__':
    find()