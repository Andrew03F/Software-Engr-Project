import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from quizapp.auth import login_required

from quizapp.db import get_db

from random import randint
import time

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
    
    if request.method == 'GET':
        numOne = randint(0,10)
        numTwo = randint(0,10)
        
        numOneBin = bin(numOne)[2:]
        numTwoBin = bin(numTwo)[2:]
        
        result = (numOne * numTwo)
        
        return render_template('quiz/play.html', numOneBin = numOneBin, numTwoBin = numTwoBin)
    
    return render_template('quiz/play.html')

@bp.route('/results')
def results():
    global count

    score = count

    db = get_db()

    db.execute("INSERT INTO score (scorer_id, score) VALUES (?, ?)",
               (session['user_id'], score),
               )
    db.commit()
    
    return render_template('quiz/results.html', count = count)


@bp.route('/count_answer', methods = ["POST"])
def count_answer():
    global numOneBin
    global numTwoBin
    global result
    global count
    
    suffix = request.form['answer']
        
    prefix = "0b"
    string = prefix + suffix
    answer = int(string, 2)
    
    if answer == result:
        count = count + 1
    
    numOne = randint(0,10)
    numTwo = randint(0,10)
    
    numOneBin = bin(numOne)[2:]
    numTwoBin = bin(numTwo)[2:]
    
    result = numOne * numTwo
    
    return render_template('quiz/play.html', numOneBin = numOneBin, numTwoBin = numTwoBin)

