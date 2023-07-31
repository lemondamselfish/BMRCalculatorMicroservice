import requests


def test_calculate_bmr():
    url = 'http://127.0.0.1:8000/calculate_bmr'

    # Example input data, replace with appropriate values for testing
    input_data = {
        'weight': 70,
        'height': 180,
        'age': 30,
        'sex': 'male'
    }

    # Send a POST request with JSON data
    response = requests.post(url, json=input_data)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print("BMR:", data.get('bmr'))
    else:
        print("Error:", response.json())


if __name__ == "__main__":
    test_calculate_bmr()