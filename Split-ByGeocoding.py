import requests
import json


def get_url(url):
	response =requests.get(url)
	content=response.content.decode("utf8")
	return content
	
def get_json_from_url(url):
	content=get_url(url)
	js=json.loads(content)
	return js
error=0
complete=0
i=0

OutputFile='address_split.csv' 
InputFile= 'address_to_splitt.csv'
Gkey='' #Google api key

file=open(OutputFile, 'w') 
with open(InputFile, 'r') as f:
	indToSplit=[line.strip() for line in f]
for ind in indToSplit:
	URL="https://maps.googleapis.com/maps/api/geocode/json?key="+Gkey+"&address="+str.lower(ind)

	geo=get_json_from_url(URL)
	indirizzo=""
	civico=""
	provincia=""
	comune=""
	cap=""

	try:
		for ad in geo['results'][0]['address_components']:
			if ad['types'][0]=='street_number':
				civico=ad['short_name']
			if ad['types'][0]=='route':
				indirizzo=ad['short_name']	
			if ad['types'][0]=='administrative_area_level_2':
				provincia=ad['short_name']
			if ad['types'][0]=='administrative_area_level_3':
				comune=ad['short_name']
			if ad['types'][0]=='postal_code':
				cap=ad['short_name']
			if indirizzo!="" and civico!="" and provincia !="" and comune!="" and cap!="":
				print(str(i)+';'+indirizzo+';'+civico+';'+comune+';'+provincia+';'+cap)
				file.writelines(str(i)+';'+indirizzo+';'+civico+';'+comune+';'+provincia+';'+cap+'\r')
				complete=complete+1
	except:
		print ("Error on -> "+str.lower(ind))
		file.writelines(str(i)+';'+str.lower(ind)+';'+''+';'+''+';'+''+';'+''+'\r')
		error=error+1
		pass
	i=i+1
print ("Finish:\nError: "+str(error)+'  |  Completed: '+str(complete))