data_file = open("fatal-police-shootings-data.csv", 'r') #opening the CSV file 
data_lines = data_file.readlines()

database = {}       #assigning accumulator 
for row in range(1, len(data_lines)):  #parsing the CSV file
    line = data_lines[row]
    
    entries = line.split(',')
    db_entry = {}   #creating anotther dictionary to use as a value to ID
    db_entry["name"] = entries[1]
    db_entry["date"] = entries[2]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[5]
    db_entry["gender"] = entries[6]
    db_entry["race"] = entries[7]
    db_entry["state"] = entries[9]
    entry_id = int(entries[0]) 
    database[entry_id] = db_entry #assigning the ID as a key to the database 

print(database[1694]["name"]) #printing the name of the person with 1694 as an ID

for keys in database: #iterating through database dictionary to print out the name of victims from Minnisota
    if database[keys]["state"]=="MN":
        print(database[keys]["name"])

count_race={}  #assigning an accumulator dictionary
for keys in database: #iterating through database to count
    if database[keys]["race"] in count_race: #accumulating through the dictionary for keys that already have values
       count_race[database[keys]["race"]]+=1
    else:
       count_race[database[keys]["race"]]=0   #creating the keys
print(count_race)

print("fraction of black victims to black people on general", count_race["B"]/len(database))

unarmed_selection={}
for key in database:
    if database[key]["armed"]=="unarmed":
        unarmed_selection[key]=database[key]

unarmed_race_count={}
for key in unarmed_selection:
    if unarmed_selection[key]["race"] in unarmed_race_count: #accumulating through the dictionary for keys that already have values
        unarmed_race_count[unarmed_selection[key]["race"]]+=1
    else:
        unarmed_race_count[unarmed_selection[key]["race"]]=1  #creating the keys 
print(unarmed_race_count)
print("The fraction of unarmed black men",unarmed_race_count["B"]/len(unarmed_selection)) 

                           



       
           

        


