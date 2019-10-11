# Web-APIs-with-Python-and-Flask
Creating Web APIs with Python and Flask

#### Requirements
- Python3
- Flask `pip install flask`

#### Introducing API
Application Programming Interface (API) allows information to be manipulated by other programs via the internet.If you have data you wish to share with the world, an API is one way.

### API Terminology
- **HTTP(Hypertext Transfer Protocol)** : is the primary means of communicating data on the web. HTTP implements a number of "methods", which tells which direction the data is moving and what should happen to it. The two most common are GET, which pulls data from a server and POST, which pushes data to a server.
- **URL(Uniform Resource Locator)** : An address for a resource on the web. A URL consists of a **protocol**`(http://)`, **domain**`(naikshubham.com)` , and optional **path** `(/about)`. A URL describes the location of a specific resource, such as a web page.
- **JSON(JavaScript Object Notation)** is a text-based data storage format that is designed to be easy to read for both humans and machines. JSON is generally the most common format for returning data through an API, XML being the second most common.
- **REST(REpresentational State Transfer)** is a philosophy that describes some best practices for implementing APIs. APIs designed with some or all of these principles in mind are called **REST APIs**.

### Flask
We will use Flask web framework to write an API. Flask maps HTTP requests to Python functions.
- Run the flask application with the command `python api.py`
We see output similar to below:
```python
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
This message means that Flask is running the application locally(on your computer) at that address.Follow the above link, `http://127.0.0.1:5000/` using your web browser to see the running application

### What Flask does
- Flask maps HTTP requests to Python functions. In our case, we've mapped one URL path('/') to one function `home`. 
- When we connect to Flask server at `http://127.0.0.0:5000/`, Flask checks if there is a match between the path provided and a defined function. 
- The process of mapping URLs to functions is called **routing**. 

```python
@app.route('/', methods=['GET'])
```

- The **methods** list **(methods=['GET'])** is a keyword argument that lets Flask known what kind of HTTP requests are allowed. 

- **`app = Flask(__name__)`** - Creates the Flask application object, which contains data about the application and also methods(object functions) that tell the application to do certain actions. The last line, **`app.run()`** is one such method.

- **`app.run()`** - runs the application server

### Creating the API
- Let's add some data(entries on three science fiction novels) as a list of dictionaries. Each dictionary will contain ID number, title, author, first sentence and year of publication for each book. 
- Finally, we'll add a new function : a **route** that will allow a visitor to access our data.
- Run the code (navigate to **`api`** folder in the command line and enter **`python api.py`**. Once the server is running, visit the route URL to view the data in the catalog

```python
http://127.0.0.1:5000/api/v1/resources/books/all
```
- **Flask has a `jsonify` function that converts lists and dictionaries to JSON format**
- In the route we created, our book entries are converted from a list of Python dictionaries to JSON before being returned to a user.





















































