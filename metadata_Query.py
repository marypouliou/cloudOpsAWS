import requests
import json

#code should run within AWS EC2 instance

def metadata_Query(metadata_Name):
	try:
		url = "http://169.254.169.254/latest/meta-data/"+metadata_Name #extract metadata value
		response = requests.post(url)
		json_Response= json.dumps({metadata_Name: response.text}) #parse response to JSON format
		print(json_Response)
	except:
		print("Please check again metadata key provided") #in case metadata key is not valid
		
		
		
		
		
		
		
		
		
		
		
		
		
		