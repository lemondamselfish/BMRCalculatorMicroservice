# BMRCalculatorMicroservice

Microservice Communication Contract

This README provides clear instructions on how to programmatically REQUEST data from and RECEIVE data from the Flask Microservice implemented as part of the project.

Communication Contract

REQUEST Data
To request data from the microservice, you need to make an HTTP POST request to the appropriate endpoint. The microservice expects a JSON payload with the following parameters:

Endpoint: /calculate_bmr

HTTP Method: POST

Content-Type: application/json

Request Payload:

    weight (float): The weight of the person in kilograms (kg).
    
    height (float): The height of the person in centimeters (cm).
    
    age (integer): The age of the person in years.
    
    sex (string): The sex of the person, either "male" or "female". 
    
    (From my limited research, BMR Calculations regrettably do not account for intersex individuals. It is also 
    unclear to what extent these calculations should depend on a person's AGAB or current hormonal makeup)
    
Example Request:

POST http://127.0.0.1:5000/calculate_bmr
Content-Type: application/json

{
  "weight": 70,
  "height": 180,
  "age": 30,
  "sex": "male"
}


RECEIVE Data
The microservice will respond to the request with a JSON object containing the calculated Basal Metabolic Rate (BMR) for the provided parameters. The response will include the following data:

bmr (float): The calculated Basal Metabolic Rate for the given person.

Example Response:

{
  "bmr": 1656.5
}

Usage Example (Python)

To programmatically interact with the microservice in Python, you can use the requests library. Below is an example of how to make a request and receive data:

import requests

url = "http://127.0.0.1:5000/calculate_bmr" (port dependent on deployment)
payload = {
    "weight": 70,
    "height": 180,
    "age": 30,
    "sex": "male"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Received BMR:", data["bmr"])
else:
    print("Error:", response.status_code, "-", response.reason)

UML Diagram: 

<img width="583" alt="Screenshot 2023-07-31 at 14 14 07" src="https://github.com/lemondamselfish/BMRCalculatorMicroservice/assets/100961185/d4bdc572-3dac-4271-b169-76736dc224b5">


    

