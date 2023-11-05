import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from quizapp.auth import login_required

from quizapp.db import get_db

bp = Blueprint('quiz', __name__, url_prefix='/quiz')

@bp.route('/play', methods=('GET', 'POST'))
@login_required
def play():
    if request.method == 'POST':
        score = request.form['score']

        db = get_db()
        error = None

        if not score:
            error = 'example score required'
        
        if error is None:
            try:
                db.execute(
                    "INSERT INTO score (scorer_id, score) VALUES (?, ?)",
                    (session['user_id'], score),
                )
                db.commit()
            except:
                error = 'error saving score';
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('quiz/play.html')