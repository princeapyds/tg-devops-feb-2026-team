import json

data = {
    "name": "EC2-Server",
    "status": "running",
    "region": "ap-south-1"
}

json_data = json.dumps(data, indent=4)
print(json_data)
