import functools
from flask import Blueprint, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from quizapp.auth import login_required
from quizapp.db import get_db
from random import randint

bp = Blueprint('quiz', __name__, url_prefix='/quiz')

result = 0
count = 0
numOneBin = ""
numTwoBin = ""

@bp.route('/play', methods=['GET', 'POST'])
@login_required
def play():
    global numOneBin
    global numTwoBin
    global result
    global count

    count = 0

    session.pop('numOneBin', None)
    session.pop('numTwoBin', None)
    session.pop('result', None)
    session.pop('quiz_details', None)

    if request.method == 'GET':
        numOne = randint(0, 10)
        numTwo = randint(0, 10)

        numOneBin = bin(numOne)[2:]
        numTwoBin = bin(numTwo)[2:]

        result = numOne * numTwo

        session['numOneBin'] = numOneBin
        session['numTwoBin'] = numTwoBin
        session['result'] = result

        return render_template('quiz/play.html', numOneBin=numOneBin, numTwoBin=numTwoBin)

    return render_template('quiz/play.html')


@bp.route('/results')
def results():
    global count

    score = count
    quiz_details = session.get('quiz_details', [])

    db = get_db()

    db.execute("INSERT INTO score (scorer_id, score) VALUES (?, ?)", (session['user_id'], score))
    db.commit()

    return render_template('quiz/results.html', count=count, quiz_details=quiz_details)

@bp.route('/count_answer', methods=["POST"])
def count_answer():
    global count

    suffix = request.form['answer']

    prefix = "0b"
    string = prefix + suffix
    answer = int(string, 2)

    if 'numOneBin' not in session:
        session['numOne'] = randint(0, 10)
        session['numTwo'] = randint(0, 10)
        session['numOneBin'] = bin(session['numOne'])[2:]
        session['numTwoBin'] = bin(session['numTwo'])[2:]
        session['result'] = session['numOne'] * session['numTwo']

    question_text = f"What is the product of these two binary numbers: {session['numOneBin']} * {session['numTwoBin']}"
    is_correct = answer == session['result']
    session.setdefault('quiz_details', []).append({'text': question_text, 'user_answer': suffix, 'correct': is_correct})

    if is_correct:
        count = count + 1

    session['numOne'] = randint(0, 10)
    session['numTwo'] = randint(0, 10)

    session['numOneBin'] = bin(session['numOne'])[2:]
    session['numTwoBin'] = bin(session['numTwo'])[2:]

    session['result'] = session['numOne'] * session['numTwo']

    return render_template('quiz/play.html', numOneBin=session['numOneBin'], numTwoBin=session['numTwoBin'])
