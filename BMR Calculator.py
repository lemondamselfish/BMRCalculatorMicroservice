from flask import Flask, request, jsonify

bmr_calculator_app = Flask(__name__)


def calculate_bmr(weight, height, age, sex):
    if sex.lower() == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    return bmr


@bmr_calculator_app.route('/calculate_bmr', methods=['POST'])
def get_bmr():
    data = request.get_json()
    weight = data.get('weight')
    height = data.get('height')
    age = data.get('age')
    sex = data.get('sex')

    if None in (weight, height, age, sex):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        weight = float(weight)
        height = float(height)
        age = int(age)
    except ValueError:
        return jsonify({'error': 'Invalid input format'}), 400

    bmr = calculate_bmr(weight, height, age, sex)
    return jsonify({'bmr': bmr}), 200


if __name__ == '__main__':
    bmr_calculator_app.run(host='0.0.0.0', port=8000)
