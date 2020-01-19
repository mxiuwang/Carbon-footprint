import csv       #import csv module
import boto3      # import AWS module to use rekognition funcionallity SOURCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import nltk
nltk.download('wordnet') # source wordNet!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from nltk.corpus import wordnet as wn

with open('credentials.csv', 'r') as input:   #iterate over the csv containing our API
	next(input)  #skip first row, move onto next
	objRead = csv.reader(input) #read the csv file
	for i in objRead:    #find the access key
		accKeyID = i[2] # the 3rd item in the file is the access Key ID
		secAccKey = i[3] #the 4th item in the file is the secret access key

UserInput = ['popcan.png','aluminium.JPG','battery.JPG','cardboard.JPG','chair.JPG','fruit.JPG','laptop.JPG','meat.JPG','milkjug.JPG','orangepeel.JPG','paper.JPG','pen.JPG','soupcan.JPG','tire.JPG'] #Load the image to be tested

itemList = []
#create a client , pass in secret access key and access key id
for pic in UserInput:

	client = boto3.client('rekognition',region_name = 'us-west-2',aws_access_key_id = accKeyID,aws_secret_access_key = secAccKey) 

#convert image into base-64 bytes
	with open(pic, 'rb') as original:
		originalBytes = original.read()  # the bytes are what will be passed into the rekognition detect labels method
		#originalBytes = 

	estimate = client.detect_labels(Image={'Bytes': originalBytes},MaxLabels = 10)	#get the image

	itemList.append(estimate['Labels'][0]['Name'])
print(itemList)

def itemCheck(item):
	oragnicList=['Fruit','Peel','Plant','Food','Vegtable','Apple','Burger','Flower','Leaf', 'Meat','Meal','Lunch','Breakfast','Supper','Dinner']
	for org in oragnicList:
		synOrg = wn.synsets(org)
	for i in synOrg:
		str(i)
		oragnicList.append(wordSplit(i))
	print(oragnicList)
	recyclingList =['Milk','Soda','Can','Tin','Paper','Steel','Cardboard','Box','Soup','Spoupcan','Plastic','Wrap']

	garbageOrElectronics = ['Pen','Chair','Pc','Fuse','TV','Microwave','Garbage']
	#recycleRefundList = ['Milk','Soda','Can']
	#recycleNonRefund = ['Tin','Paper','Steel','Cardboard']
	#electronics = ['PC','Fuse','TV','Microwave']
	

	if item in oragnicList:
		#print('This is a '+ item + ', pleaase place it in your organics bin or compost.')
		return 0
	if item in recyclingList:
		#print('This is a '+ item + ', please return for a refund.')
		return 0
	#if item in recycleNonRefund:
		#print('This is a '+ item + ', please place in your recycling bin.')
		#return 0
	#if item in electronics:
		#print('This is a '+ item + ', please return your unwanted electronics to the nearest pickup location.')
		#return 0
	if item in garbageOrElectronics:
		#print('This is a '+ item + ', please place all garbage in your gaerbage bin, or take to your local landfill.Please return your unwanted electronics to the nearest pickup location.')
		return 0
	else:
		#print('Unkown item, please consult with your local jusrtistictions webpage.')
		return 0

def wordSplit(word):
	word = str(word)
	word2=''
	for i in range(8,len(word)):
		if word[i] != '.':
			word2+=word[i]
		if word[i]=='.':
			return word2



#itemCheck(item)
synonymList = []
for item in itemList:
	synonym = wn.synsets(item)
	#itemCheck(item)

	for i in synonym:
		str(i)
		synonymList.append(wordSplit(i))
	#print(synonym)
print(synonymList)
print(len(synonymList))