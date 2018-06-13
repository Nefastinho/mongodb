import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
students = db.students

# find the lowest homework in code and then update the scores array with the low homework pruned.
def remove_lowest_homework():        
    
    try:        
        query = {"scores.type":"homework"}        
        docs = students.find(query).sort("_id",pymongo.ASCENDING)

        for doc in docs:
            id = doc["_id"]            
            scores = drop_lowest_homework(doc)
            students.update_one({"_id":id},{"$set": {"scores":scores}}) 
            print "Updated student with id:",id           

    except Exception:
        raise

def drop_lowest_homework(student):
    scores = student["scores"]
    # sort list by score
    sorted_scores = sorted(scores, key=lambda x: x["score"])
    for score in sorted_scores:
        if score["type"]=="homework":
            # the first homework is the lowest
            sorted_scores.remove(score) 
            break

    return sorted_scores

remove_lowest_homework()