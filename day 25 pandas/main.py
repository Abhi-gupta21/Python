#file = open("day 25 pandas/weather_data.csv")
#content = file.readlines()
#print(content)

#import csv

#with open("day 25 pandas/weather_data.csv") as file:
#    data = csv.reader(file)
#   temp = []
#    for row in data:
#        print(row)
#        if row[1]!='temp':
#            temp.append(int(row[1]))
#    print(temp)



# Pandas - super powerful

import pandas

data = pandas.read_csv("day 25 pandas/weather_data.csv")
#print(type(data))
print(data)
#print(type(data['temp']))
#print(data['temp'])
data_dict = data.to_dict()
print(data_dict)
temp_list = data['temp'].to_list()
avg = sum(temp_list)/len(temp_list)
print(avg)
print(temp_list)
print(data['temp'].mean())
print(data['temp'].max())

print(data[data['day']=="Monday"])
print(data[data['temp']==data['temp'].max()])
print(data[data['temp']==data['temp'].max()]["temp"])

# ceate a datafra,e from scratch

data_diction = {
    "students": ["amy","Abhi","hesaree"],
    "marks": [50,100,100]
}

Data = pandas.DataFrame(data_diction)
Data.to_csv("day 25 pandas/new_data.csv")