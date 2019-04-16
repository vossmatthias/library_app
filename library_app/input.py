

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import db



bp = Blueprint('input', __name__, url_prefix='/input')

@bp.route('/book', methods=('GET', 'POST'))


def input_book():

	#db.get_db()
	if request.method == "POST":
		title = request.form['title']
		db = get_db()
		error = None

		if not title:
			error = 'Title of Book is required.'
		elif db.execute(
			'SELECT isbn FROM book WHERE title = ?', (book,)
		).fetchone() is not None:
			error = 'Book {} is already in the library.'.format(title)

		if error is None:
			db.execute(
				'INSERT INTO book (title) VALUES (?, ?)',
				(title)
			)
			db.commit()
		return redirect(url_for('input'))

		flash(error)

	return render_template('input/book.html')
