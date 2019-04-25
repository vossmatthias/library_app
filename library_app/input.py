import functools
import sqlite3

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from library_app.db import get_db


bp = Blueprint('input', __name__, url_prefix='/input')

@bp.route('/book', methods=('GET', 'POST'))


def input_book():

	db_connection = get_db()
	db_cursor = db_connection.cursor()

	if request.method == "POST":
		title = request.form['title']
		isbn = request.form['isbn']
		year = request.form['year']
		pages = request.form['pages']
		language = request.form ['language'] 
		db = get_db()
		error = None

		if not title or not isbn or not year or not pages or not language:
			error = 'Basic Information of Book is required.'
		elif db_cursor.execute('SELECT isbn FROM book WHERE isbn = ?', (isbn,)).fetchone() is not None:
			error = 'Book {} is already in the library.'.format(title)

		if error is None:
			db_cursor.execute(
				'INSERT INTO book (title, isbn, year, pages, language) VALUES (?,?,?,?,?); ', (title, isbn, year, pages, language,)
			)
			db_connection.commit()

	if request.method == "POST":
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		db = get_db()
		error = None

		if not first_name or not last_name:
			error = 'Basic Information of the Author is required.'

		elif db_cursor.execute('SELECT first_name FROM author WHERE first_name = ?', (first_name,)).fetchone() is not None:
			error = 'Author {} is already in the library.'.format(first_name)

		if error is None:
			db_cursor.execute(
				'INSERT INTO author (first_name, last_name) VALUES (?,?); ', (first_name, last_name,)
			)
			db_connection.commit()

	if request.method == "POST":
		name = request.form['name']
		db = get_db()
		error = None

		if not name:
			error = 'Basic Information of the Publisher is required.'

		elif db_cursor.execute('SELECT name FROM publisher WHERE name = ?', (name,)).fetchone() is not None:
			error = 'Publisher {} is already in the library.'.format(name)

		if error is None:
			db_cursor.execute(
				'INSERT INTO publisher (name) VALUES (?); ', (name,)
			)
			db_connection.commit()
		return redirect(url_for('input.input_book'))

		flash(error)

	return render_template('input/book.html')
