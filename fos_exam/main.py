from flask import Flask, render_template, request, redirect, url_for

# imports for database
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# route for books
@app.route('/books')
def index():
    context = {
        'title': 'Books LIst',
        'heading': 'Welcome to my Flask App!'
    }
    return render_template('books.html', context=context)


# model for database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    publication_year = db.Column(db.Integer)

    def __repr__(self):
        return '<Customer %r>' % self.name

# create db    
def create_db():
    with app.app_context():
        db.create_all()

@app.route('/books', methods=['GET'])
def show_books():

    context = {
        'title': 'Data',
        'heading': 'Data',
        'books': Book.query.all()
    }
    return render_template('books.html', context=context)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        publication_year = request.form.get('publication_year')

        new_book = Book(title=title, author=author, publication_year=publication_year)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('add_book'))

    return render_template('add_book.html')



if __name__ == '__main__':
    create_db()
    app.run(debug=True)