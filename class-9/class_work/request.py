import requests
import csv

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("user_info.csv", 'w', newline='') as csvFile:
        filedNames = ["Name", "Email", "City"] # Name of headers
        writer = csv.DictWriter(csvFile, fieldnames=filedNames)

        writer.writeheader()

        for d in data:
            writer.writerow({"Name": d['name'], "Email":d['email'], "City":d["address"]['city']})

else:
    print("Bad Request:", response.status_code)