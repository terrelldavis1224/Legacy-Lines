import flask
import back_end
import os
from flask import Flask, render_template, request, session
from datetime import datetime, timedelta

app = Flask(__name__)


#app.secret_key = os.getenv('FLASK_SECRET_KEY', 'fallback_secret_key_if_not_set')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess_player')
def guess_player():
  


    return render_template('guess.html', main_player_info=back_end.main_player_info,
                           main_career_info=back_end.main_career_info,
                           player_info_list=back_end.nba_player_info_list,
                           career_info_list=back_end.career_info_list)

@app.route('/submit_guesses', methods=['POST'])
def submit_guesses():
    user_answers = request.form.to_dict()
    results = back_end.process_user_answers(user_answers)
    correct=0
    for key in user_answers:
        if user_answers[key] == "T":
            correct+=1
    return render_template('submit_guesses.html', main_player_info=back_end.main_player_info,
                           main_career_info=back_end.main_career_info,
                           player_info_list=back_end.nba_player_info_list,
                           career_info_list=back_end.career_info_list,
                           results=results, correct=correct)

if __name__ == '__main__':
    app.run(debug=True)

