from flask import Flask, request, jsonify

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


@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction nvels.</p>"

@app.route('/api/v1/resources/books', methods=['GET'])
def api_all():
	return jsonify(books)

app.run()