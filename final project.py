
import json

with open("rows.json", 'r') as file:
    Json_file_name = json.load(file)
#print(Json_file_name)
    result= []
for item in Json_file_name['data']:
    if item[8] == "Wellness visit" and item [9] == "18-34 years":
        #print(item)
        result.append(float(item[10]))
        #print(item[10])
average_result = ((result[0] + result[1]) / 2)
#print(int(average_result))
print("The percentage of adults in the 18–34-year age range who saw a doctor for a Wellness Visit")
print("in 2019 and 2020 is " + str(average_result) + " %")
#print(int(average_result))

# this section is trying to figure out which category of obesity is the highest.

for item in Json_file_name['data']:
    if item[8] == "Obesity" and item [9] == "18-34 years":
        print(item)
        result.append(float(item[10]))
        print(item[10])
average_result = ((result[0] + result[1]) / 2)
print(int(average_result))

for item in Json_file_name['data']:
    if item[8] == "Wellness visit" and item [9] == "Total":
        print(item)
        result.append(float(item[10]))
        print(item[10])
average_result = ((result[0] + result[1]) / 2)
print(int(average_result))