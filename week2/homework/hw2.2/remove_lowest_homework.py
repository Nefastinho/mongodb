import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades

def remove_lowest_homework():        
    
    try:
        query = {"type":"homework"}
        projection = {"student_id":True,"score":True}
        homeworks = grades.find(query,projection).sort([("student_id",pymongo.ASCENDING),("score",pymongo.ASCENDING)])
        
        last_id = -1
        # Si cambia el id, al estar ordenados de forma ascendente significa que
        # el primer documento con ese id es el de menor nota. Se borra
        for doc in homeworks:
            student_id = doc["student_id"]
            if (student_id!=last_id):
                last_id = student_id
                id = doc["_id"]
                remove_student(id)

    except Exception:
        raise


def remove_student(id):
    query = {'_id':id}
    try:
        grades.delete_one(query)
        print "removed student with id: ", id
    
    except Exception:
        raise

remove_lowest_homework()