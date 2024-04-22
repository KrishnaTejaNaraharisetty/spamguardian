from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the Naive Bayes model
pipe = pickle.load(open("Naive_model.pkl", "rb"))

# Load the dataset
data = pd.read_csv("emails.csv")

# Separate features and target variable
X = data['text'].values
y = data['spam'].values


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the CountVectorizer
cv = CountVectorizer()
X_train_cv = cv.fit_transform(X_train)

# Train the SVM model
svm = SVC()
svm.fit(X_train_cv, y_train)

@app.route('/', methods=["GET","POST"])
def main_function():

    if request.method == "POST":
        text = request.form
        emails = text['email']
        model_choice = text['model']

        list_email = [emails]
        if model_choice == 'naive_bayes':
            output = pipe.predict(list_email)[0]
        elif model_choice == 'svm':
            output = svm.predict(cv.transform(list_email))[0]

        return render_template("show.html", prediction=output)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
