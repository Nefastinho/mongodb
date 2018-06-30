db.zips.aggregate([
    {$project:{
    	first_char: {$substr : ["$city",0,1]},
    	pop:1 }},

	{"$match":{
		"first_char":{"$in":["B","D","O","G","N","M"]}}},

	{"$group":{
		"_id":null,
		"population":{"$sum":"$pop"}
	}}
   
])