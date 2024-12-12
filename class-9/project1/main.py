import requests
import csv

url = 'https://fake-json-api.mock.beeceptor.com/users'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("project1/info.csv", "w", newline="") as csvFile:
        fieldNames = ["Id", "Name", "Company", "Email"]
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

        writer.writeheader()

        for i in data:
            writer.writerow({"Id":i["id"], "Name":i["name"], "Company":i["company"], "Email":i["email"]})