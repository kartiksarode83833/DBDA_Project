from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route("/")
def root():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Input Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
        <h1>User Input Form</h1>
        <form action="/predict" method="post">
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required>

            <label for="workclass">Workclass:</label>
            <input type="text" id="workclass" name="workclass" required>

            <label for="finalWeight">Final Weight:</label>
            <input type="number" id="finalWeight" name="finalWeight" required>

            <label for="education">Education:</label>
            <input type="text" id="education" name="education" required>

            <label for="educationNum">Education Number:</label>
            <input type="number" id="educationNum" name="educationNum" required>

            <label for="martialStatus">Martial Status:</label>
            <input type="text" id="martialStatus" name="martialStatus" required>

            <label for="occupation">Occupation:</label>
            <input type="text" id="occupation" name="occupation" required>

            <label for="relationship">Relationship:</label>
            <input type="text" id="relationship" name="relationship" required>

            <label for="race">Race:</label>
            <input type="text" id="race" name="race" required>

            <label for="gender">Gender:</label>
            <select id="gender" name="gender" required>
                <option value="" disabled selected>Select your gender</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="non-binary">Non-binary</option>
                <option value="other">Other</option>
            </select>

            <label for="capitalGain">Capital Gain:</label>
            <input type="number" id="capitalGain" name="capitalGain" required>

            <label for="capitalLoss">Capital Loss:</label>
            <input type="number" id="capitalLoss" name="capitalLoss" required>

            <label for="hoursPerWeek">Hours per Week:</label>
            <input type="number" id="hoursPerWeek" name="hoursPerWeek" required>

            <label for="nativeCountry">Native Country:</label>
            <input type="text" id="nativeCountry" name="nativeCountry" required>

            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
    """

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract form data
        Age = int(request.form["age"])
        Workclass = request.form["workclass"]
        FinalWeight = int(request.form["finalWeight"])
        Education = request.form["education"]
        EducationNum = int(request.form["educationNum"])
        MartialStatus = request.form["martialStatus"]
        Occupation = request.form["occupation"]
        Relationship = request.form["relationship"]
        Race = request.form["race"]
        Gender = request.form["gender"]
        Capital_Gain = int(request.form["capitalGain"])
        Capital_loss = int(request.form["capitalLoss"])
        Hours_per_week = int(request.form["hoursPerWeek"])
        Native_Country = request.form["nativeCountry"]

        # Load the model
        with open('model_picke', 'rb') as file:
            model = pickle.load(file)

        # Prepare the feature list
        x = [Age, Workclass, FinalWeight, Education, EducationNum, MartialStatus, Occupation, Relationship, Race,
             Gender, Capital_Gain, Capital_loss, Hours_per_week, Native_Country]

        # Preprocess features if needed (e.g., encode categorical variables)
        # Example preprocessing step (you need to adjust this based on your model requirements):
        # x_processed = preprocess_features(x)

        # Get prediction
        prediction = model.predict([x])

        if prediction[0] == 1:
            result = "Pass"
        else:
            result = "Fail"

        return f"""
        <html>
            <body>
                <h1>Prediction Result</h1>
                <p>Based on your input, we have predicted your result as: {result}</p>
            </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html>
            <body>
                <h1>Error</h1>
                <p>An error occurred: {e}</p>
            </body>
        </html>
        """

# Start the Flask application

app.run(host="0.0.0.0", port=4000, debug=True)
