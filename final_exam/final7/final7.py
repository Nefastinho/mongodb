import pymongo

con = pymongo.MongoClient("mongodb://localhost")

db = con.final7
images = db.images
albums = db.albums

cursor = images.find({},{'_id':1})

for image in cursor:
    image_id = image['_id']
    image_in_albums = albums.find_one({'images': image_id})    

    if image_in_albums is None:
        print 'removed image with id: ' + str(image_id)
        images.remove({'_id':image_id})

print 'completed'