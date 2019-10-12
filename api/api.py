from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

# create some test data for our catlog in the form of a list of dictionaries.
books = [
{
	'id':0,
	'title':'A Fire upon the deep',
	'author':'Vernor Vinge',
	'first_sentence':'The coldsleep itself was dreamless',
	'year_published':'1992'
},
{
	'id':1,
	'title': 'The Ones Who Walk Away From Omelas',
    'author': 'Ursula K. Le Guin',
    'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
    'published': '1973'
},
{	'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'
}
]


def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d


@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archives</h1><p>This site is a prototype API for distant reading of science fiction nvels.</p>"


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
	conn = sqlite3.connect('books.db')
	conn.row_factory = dict_factory
	cur = conn.cursor()
	all_books = cur.execute('SELECT * FROM books;').fetchall()

	return jsonify(all_books)


# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_id():
# 	# check if an ID was provided as a part of the URL
# 	# If ID is provided, assign it to a variable
# 	# If no ID is provided, display an error in the browser
# 	if 'id' in request.args:
# 		id = int(request.args['id'])
# 	else:
# 		return "Error: No id field provided. Please specify an id."

# 	# create an empty list for our results
# 	results = []

# 	# loop through the data and match results that fit the requested ID
# 	# IDs are unique, but other fields might return many results
# 	for book in books:
# 		if book['id'] == id:
# 			results.append(book)

# 	# use the jsonify function from Flask to convert our list of Python dictionaries to the JSON format
# 	return jsonify(results)


@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
	query_parameters = request.args
	id = query_parameters.get('id')
	published = query_parameters.get('published')
	author = query_parameters.get('author')

	query = "SELECT * FROM books"
	to_filter = []
	filters = []

	if id:
		# query += ' id=? AND'
		filters.append(' id=? ')
		to_filter.append(id)
	if published:
		# query += ' id=? AND'
		filters.append(' published=? ')
		to_filter.append(published)
	if author:
		# query += ' author=? AND'
		filters.append(' author=? ')
		to_filter.append(author)
	if not (id or published or author):
		return page_not_found(404)

	print('filters->', filters)
	print('to_filter->', to_filter)
	if len(filters) > 1:
		conditions = " and ".join(filters)
	else:
		conditions = filters[0]
	print('conditions ->', conditions)
	# query = query[:-4] + ';'
	final_q = " WHERE ".join([query, conditions])
	print('final query ->', final_q)

	conn = sqlite3.connect('books.db')
	conn.row_factory = dict_factory
	cur = conn.cursor()

	results = cur.execute(final_q, to_filter).fetchall()

	return jsonify(results)


app.run()