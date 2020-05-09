import json

def extract_Value(json_Object, key):
	try:
		json_Load = json.loads(json_Object) #loads the json Object
		value = json_Load[key] #extracts the value
		print(key+" = "+str(value)) 
	except:
	#in case json object is not valid or key is not found in the json object
		print("Please check again json object and key provided.") 
		