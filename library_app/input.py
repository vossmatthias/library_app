<<<<<<< HEAD
import functools
import sqlite3


=======


import functools

>>>>>>> 219ce5e91842e5541ff05245ec88b2691af3a3e6
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import db



bp = Blueprint('input', __name__, url_prefix='/input')

@bp.route('/book', methods=('GET', 'POST'))


def input_book():
<<<<<<< HEAD
	db_connection = db.get_db()
	db_cursor = db_connection.cursor()
	#db.get_db()
	if request.method == "POST":
		title = request.form['title']
=======

	#db.get_db()
	if request.method == "POST":
		title = request.form['title']
		db = get_db()
>>>>>>> 219ce5e91842e5541ff05245ec88b2691af3a3e6
		error = None

		if not title:
			error = 'Title of Book is required.'
<<<<<<< HEAD
		elif db_cursor.execute(
			'SELECT title FROM book', 
=======
		elif db.execute(
			'SELECT isbn FROM book WHERE title = ?', (book,)
>>>>>>> 219ce5e91842e5541ff05245ec88b2691af3a3e6
		).fetchone() is not None:
			error = 'Book {} is already in the library.'.format(title)

		if error is None:
<<<<<<< HEAD
			db_cursor.execute(
				'INSERT INTO book (title) VALUES (?); ', (title,)
			)
			db_connection.commit()
		return redirect(url_for('input.input_book'))

		flash(error)

	return render_template('input/book.html')
=======
			db.execute(
				'INSERT INTO book (title) VALUES (?, ?)',
				(title)
			)
			db.commit()
		return redirect(url_for('input'))

		flash(error)

	return render_template('input/book.html')
>>>>>>> 219ce5e91842e5541ff05245ec88b2691af3a3e6
