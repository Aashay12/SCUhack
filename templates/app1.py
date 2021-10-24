from logging import debug
from flask import Flask, render_template, request, redirect, session
from flask_cors import CORS
import json
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'any'
CORS(app)

# sender_email = os.getenv('SENDER_EMAIL')
# password = os.getenv('PASSWORD')
# receiver_email = os.getenv('RECEIVER_EMAIL')

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = sender_email
# app.config['MAIL_PASSWORD'] = password
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

expungement_penal_code = {
    '1203.4': "Positive: Expungement under § 1203.4, More info DACA: For updates on DACA, go to www.ilrc.org/daca. For information on DACA and crimes go to https: // www.ilrc.org/sites/default/files/resources/crimes_and_daca_renewals.pdf"}

vacatur_penal_code = {
    '1203.43': "Positive Outcome: Vacatur under California Penal code §1203.43",
    '1018': "Positive Outcome: Vacatur under California Penal code §1018",
    '1016.5': "Positive Outcome: Vacatur under California Penal code §1016.5",
    '1473.7': "Positive Outcome: Vacatur under California Penal code §1473.7, For more information about 1473.7 see https://www.ilrc.org/sites/default/files/resources/ammends_ca_penal_code_1473.7-20180928.pdf and https://www.ilrc.org/sites/default/files/resources/using_and_defending_california_penal_code_1473.7_vacaturs_in_immigration_proceedings_sample_memorandum_of_law_and_table_of_bia_cases.pdf",
    '236.14': "Positive Outcome: Vacatur under California Penal code §236.14",
    'corpus': "Positive Outcome: Vacatur under Writ of Habeas Corpus"
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        print('hcjhjhfghjk')
        # rule engine
        data = request.get_json()
        print(data)
        # Question 1
        if data['drug_offense'] == True:
            # positive
            text_result_1 = expungement_penal_code["1203.4"]
        else:
            text_result_1 = "Negative"

        # Question 2
        if data['daca'] == True:
            # positive
            text_result_2 = expungement_penal_code["1203.4"]
        else:
            text_result_2 = "Negative"

        # Question 3
        if data['drug_counselling'] == True:
            text_result_3 = vacatur_penal_code["1203.43"]
            # subquestion_3
            if data['3.1'] == True:
                print(data['3.1'])
                text_result_3_1 = "Negative"
            else:
                text_result_3_1 = vacatur_penal_code["1473.7"]
        else:
            text_result_3 = "Negative"

        # Question 4
        if data['drug_diverse'] == True:
            text_result_4 = "No Conviction under §1000"
        else:
            text_result_4 = "Negative"

        # Question 5
        if data['probation'] == True:
            # subquestion
            if data['5.1'] == True:
                # print(data['5.1'])
                text_result_5 = vacatur_penal_code["1018"]
            else:
                text_result_5 = "Negative"
        else:
            text_result_5 = "Negative"

        # Question 6
        if data['nolo-immigrant'] == True:
            # subquestion 6_1
            if data['6.1'] == True:
                text_result_6 = vacatur_penal_code['1016.5']
            else:
                text_result_6 = "Negative"
        else:
            text_result_6 = "Negative"

        # Question 7
        if data['parole'] == True:
            text_result_7 = vacatur_penal_code['corpus']
            # sub question 7_1
            if data['records_destroyed'] == True:
                text_result_7_1 = vacatur_penal_code['1016.5']
            else:
                text_result_7_1 = "Negative"
        else:
            text_result_7 = "Negative"

        # Question 8
        if data['nolo-probation'] == True:
            text_result_8 = "Negative"
        else:
            text_result_8 = vacatur_penal_code['1473.7']

        # Question 9
        if data['evidence'] == True:

            # Subquestion 9
            if data['question2'] == True:
                text_result_9 = "Negative"
            else:
                text_result_9 = vacatur_penal_code['1473.7']
        else:
            text_result_9 = "Negative"

        # Question 10
        if data['human-traffic'] == True:
            if data['offense_nonviolent'] == True:
                text_result_10 = vacatur_penal_code['236.14']
            else:
                text_result_10 = "Negative"
        else:
            text_result_10 = "Negative"

        # Question 11
        if data['marijuana'] == True:
            text_result_11 = ""
            if data['sentence_completed'] == True:
                print(data['sentence_completed'])
                text_result_11_1 = "Positive Output-- Either Expungement or Vacatur under Health & Safety"
            else:
                text_result_11_1 = "Negative"
            print(text_result_11_1)
            if data['criminal_custody'] == True:
                text_result_11_2 = "Negative"
            else:
                text_result_11_2 = vacatur_penal_code['1473.7']
        else:
            text_result_11 = "Negative"

        # Question 12
        if data['jail'] == True:
            text_result_12 = "You may be eligible for a pardon: https://www.ilrc.org/sites/default/files/resources/gubernatorial_pardons_in_california_ilrc_cdc_2019.pdf "
        else:
            text_result_12 = "Negative"

        print(text_result_1,
              text_result_3_1,
              text_result_7_1,
              text_result_2,
              text_result_3,
              text_result_4,
              text_result_5,
              text_result_6,
              text_result_7,
              text_result_8,
              text_result_9,

              text_result_10,
              text_result_11,
              text_result_11_1,
              text_result_11_2,
              text_result_12)


@app.route('/form', methods=['GET', 'POST'])
def processForm():
    if request.method == 'GET':
        # return render_template('form.html')
        pass
    else:
        # rule engine
        pass


@app.route('/result')
def result():
    pass


if __name__ == "__main__":
    app.run(debug=True)
