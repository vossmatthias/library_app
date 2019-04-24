import functools
import sqlite3
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from library_app.db import get_db


bp = Blueprint('input', __name__, url_prefix='/input')

@bp.route('/book', methods=('GET', 'POST'))


def input_book():

	db_connection = get_db()
	db_cursor = db_connection.cursor()
	#db.get_db()
	if request.method == "POST":
		title = request.form['title']

	#db.get_db()
	if request.method == "POST":
		title = request.form['title']
		db = get_db()
		error = None

		if not title:
			error = 'Title of Book is required.'
		# elif db_cursor.execute('SELECT title FROM book' ):
		elif db_cursor.execute('SELECT title FROM book WHERE title = ?', (book,)).fetchone() is not None:
			error = 'Book {} is already in the library.'.format(title)

		if error is None:
			db_cursor.execute(
				'INSERT INTO book (title) VALUES (?); ', (title,)
			)
			db_connection.commit()
		return redirect(url_for('input.input_book'))

		flash(error)

	return render_template('input/book.html')
