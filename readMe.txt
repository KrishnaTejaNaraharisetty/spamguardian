Email Spam Classifier

Introduction:

This project is an Email Spam Classifier, built to classify emails into spam or non-spam (ham) categories. It utilizes a machine learning model trained on email data to make predictions.

Project Structure:

The project consists of the following files:

1. index.html: This file contains the HTML code for the user interface of the application. It provides a form where users can input an email to check if it is spam or ham.

2. show.html: This file presents the result of the classification. It displays whether the input email is classified as spam or not, along with relevant images.

3. Email Spam_with_pipeline.ipynb: This Jupyter Notebook file contains the code for building and training the email spam classifier using a pipeline approach. It includes data preprocessing, model training, and model evaluation.

4. Email Spam.ipynb: This Jupyter Notebook file contains an alternative approach to building and training the email spam classifier. It directly uses the Multinomial Naive Bayes algorithm without a pipeline.

5. main.py: This Python script implements the Flask web application. It loads the trained model and provides the necessary routing to render the HTML templates and handle the classification requests.

Usage:

To run the application, make sure you have Python and Flask installed. Then, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the command `python main.py`.
4. Once the server is running, open a web browser and go to `http://127.0.0.1:5000/`.
5. You can now input an email into the provided form and submit it to see the classification result.

Contributors:

This project was developed by the following contributors:

- Krishna Teja Naraharisetty
- Harshitha Manne
- Yashwanth Chowdary Kanaparthi
- Velangini Sameeksha Reddy Khambam
- Satya Suhas Nune
- Sukhdev Kolli

Acknowledgments:
This project was created as part of the ITCS 6150 Intelligent Systems Term Project under the guidance of Professor Ali Sever.

