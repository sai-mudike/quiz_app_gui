import requests
parameter={
    "amount":10,
    "type":"boolean"
}
respose=requests.get("https://opentdb.com/api.php",params=parameter)
question_data=respose.json()["results"]


