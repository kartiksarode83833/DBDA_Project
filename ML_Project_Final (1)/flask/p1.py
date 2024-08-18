# get the Flask class imported
from flask import Flask, request
import pickle

# create an application of Flask
app = Flask(__name__)


@app.route("/")
def root():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> User Input Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: url('/static/images_bg.jpeg') no-repeat center center fixed;
            background-size: cover;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            position: relative; /* To ensure that z-index works if needed */
            top: 50px; /* Pushes the form down slightly from the top */
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            display: grid;
            gap: 15px;
        }
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        input[type="text"], input[type="number"], select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Income Prediction Based On Census Data-(UIF)</h1>
        <form action="/predict" method="post">
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" min="19" max="65" required>

            <label for="education">Education:</label>
            <select id="education" name="education" required>
                <option value="" disabled selected>Select your education level</option>
                <option value="0">Preschool</option>
                <option value="1">1st-4th grade</option>
                <option value="2">5th-6th grade</option>
                <option value="3">7th-8th grade</option>
                <option value="4">9th grade</option>
                <option value="5">10th grade</option>
                <option value="6">11th grade</option>
                <option value="7">12th grade</option>
                <option value="8">HS-grad</option>
                <option value="9">Some-college</option>
                <option value="10">Assoc-acdm</option>
                <option value="11">Assoc-voc</option>
                <option value="12">Bachelors</option>
                <option value="13">Masters</option>
                <option value="14">Doctorate</option>
                <option value="15">Prof-school</option>
            </select>

            <label for="educationNum">Education Number:</label>
            <input type="number" id="educationNum" name="educationNum" required>

            <label for="martialStatus">Marital Status:</label>
            <select id="martialStatus" name="martialStatus" required>
                <option value="" disabled selected>Select your marital status</option>
                <option value="0">Never-married</option>
                <option value="1">Married-civ-spouse</option>
                <option value="2">Divorced</option>
                <option value="3">Married-spouse-absent</option>
                <option value="4">Separated</option>
                <option value="5">Married-AF-spouse</option>
                <option value="6">Widowed</option>
            </select>

            <label for="occupation">Occupation:</label>
            <select id="occupation" name="occupation" required>
                <option value="" disabled selected>Select your occupation</option>
                <option value="0">Adm-clerical</option>
                <option value="1">Exec-managerial</option>
                <option value="2">Handlers-cleaners</option>
                <option value="3">Prof-specialty</option>
                <option value="4">Other-service</option>
                <option value="5">Sales</option>
                <option value="6">Craft-repair</option>
                <option value="7">Transport-moving</option>
                <option value="8">Farming-fishing</option>
                <option value="9">Machine-op-inspct</option>
                <option value="10">Tech-support</option>
                <option value="11">Protective-serv</option>
                <option value="12">Armed-Forces</option>
                <option value="13">Priv-house-serv</option>
                <option value="14">Other</option>
            </select>

            <label for="relationship">Relationship:</label>
            <select id="relationship" name="relationship" required>
                <option value="" disabled selected>Select your relationship status</option>
                <option value="0">Husband</option>
                <option value="1">Not-in-family</option>
                <option value="2">Other-relative</option>
                <option value="3">Own-child</option>
                <option value="4">Unmarried</option>
                <option value="5">Wife</option>
            </select>

            <label for="gender">Gender:</label>
            <select id="gender" name="gender" required>
                <option value="" disabled selected>Select your gender</option>
                <option value="0">Male</option>
                <option value="1">Female</option>
            </select>

            <label for="capitalGain">Capital Gain:</label>
            <input type="number" id="capitalGain" name="capitalGain" required>

            <label for="capitalLoss">Capital Loss:</label>
            <input type="number" id="capitalLoss" name="capitalLoss" required>

            <label for="hoursPerWeek">Hours per Week:</label>
            <input type="number" id="hoursPerWeek" name="hoursPerWeek" required>

            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
    """
@app.route("/predict", methods=["POST"])
def predict():
    Age = int(request.form["age"])

    Education = int(request.form["education"])
    Gender = int(request.form["gender"])
    EducationNum = int(request.form["educationNum"])
    MartialStatus = int(request.form["martialStatus"])
    Occupation = int(request.form["occupation"])
    Relationship = int(request.form["relationship"])
    Capital_Gain = int(request.form["capitalGain"])
    Capital_loss = int(request.form["capitalLoss"])
    Hours_per_week = int(request.form["hoursPerWeek"])

    with open('model_lr', 'rb') as file:
        model = pickle.load(file)

    # get the prediction using model
    x = [Age, Education, EducationNum, MartialStatus, Occupation, Relationship, Gender,
         Capital_Gain, Capital_loss, Hours_per_week]
    prediction = model.predict([x])
    print(f"prediction = {prediction}")

    if prediction[0] == 1:
        result = "Greater than 50K"
    else:
        result = "Less than 50K"

    print("Received data:")
    print(f"Age: {Age}")

    print(f"Education: {Education}")
    print(f"EducationNum: {EducationNum}")
    print(f"MartialStatus: {MartialStatus}")
    print(f"Occupation: {Occupation}")
    print(f"Relationship: {Relationship}")
    print(f"Gender: {Gender}")
    print(f"Capital_Gain: {Capital_Gain}")
    print(f"Capital_loss: {Capital_loss}")
    print(f"Hours_per_week: {Hours_per_week}")

    return f"""
    <html>
        <body>
            <h1>Prediction Result</h1>
            <p>Based on your age and physical score, we have predicted
            your hearing test result as = {result}:</p>
        </body>
    </html> 
    """
# start the application
app.run(host="0.0.0.0", port=4000, debug=True)
