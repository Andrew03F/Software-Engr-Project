from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from quizapp.auth import login_required
from quizapp.db import get_db

bp = Blueprint('leaderboard', __name__)

@bp.route('/')
def index():
    db = get_db()
    scores = db.execute(
        'SELECT score, created, scorer_id, u.username'
        ' FROM score s JOIN user u ON s.scorer_id = u.id'
        ' ORDER BY score DESC'
    ).fetchall()

    # Sort the scores by score in descending order
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)

    # Ensure there are at least 10 entries
    scores.extend([None] * (10 - len(scores)))

    return render_template('leaderboard/index.html', scores=scores)
