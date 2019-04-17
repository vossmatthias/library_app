DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS author; 
DROP TABLE IF EXISTS publisher;
DROP TABLE IF EXISTS rel_book_author;


CREATE TABLE publisher (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);


CREATE TABLE author (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
);


CREATE TABLE book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn TEXT,
    title TEXT NOT NULL,
    year NUMERIC,
    pages NUMERIC,
    language TEXT,
    publisher_id INTEGER,
    FOREIGN KEY (publisher_id) REFERENCES publisher (id)
);


CREATE TABLE rel_book_author (
    book_id INTEGER,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES author (id),
    FOREIGN KEY (book_id)  REFERENCES book (id)
);