from PIL import Image as im
import csv 
import numpy as np
import pandas as pd

def crop(filename,coords,save_location):
	image = im.open(filename)
	cropped = image.crop(coords)
	cropped.save(save_location+filename)
	
filelist = ["Image locations for Users/user_3_loc.csv","Image locations for Users/user_4_loc.csv","Image locations for Users/user_5_loc.csv","Image locations for Users/user_6_loc.csv","Image locations for Users/user_7_loc.csv","Image locations for Users/user_9_loc.csv","Image locations for Users/user_10_loc.csv"]
 
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
for filename in filelist:
	with open(filename, 'r') as csvfile:
    # creating a csv reader object
		csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
		fields = csvreader.next()
 
    # extracting each data row one by one
		for row in csvreader:
			rows.append(row)
	
		for row in rows:
			loc = "Dataset/"+row[0]
			save_loc = "Modified_Dataset/"
			crop(loc,map(float,row[1:5]),save_loc)
 