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

### Finding specific resources
- Add a feature to filter or find specific resources.
- We have added **`api_id()`** to **`api.py`**
- `api_id()`, with the `@app.route` syntax that maps the function to the path `/api/v1/resources/books`
- Run the code as before **`python api.py`** from **`api`** directory and visit below URLs to test the new filtering capability:

```python
127.0.0.1:5000/api/v1/resources/books?id=0
127.0.0.1:5000/api/v1/resources/books?id=1
127.0.0.1:5000/api/v1/resources/books?id=2
127.0.0.1:5000/api/v1/resources/books?id=3
```

- Inside the function, we do two things : First examine the provided URL for an id and select the books that match that id. The id must be provided like this: **`?id=0`**.
- Data passed through URLs like this **`(after the ?)`** are called **query parameters**. They are a feature of HTTP used for filtering for specific kinds of data.

### API Design Principles
- Our next version of our API will pull in data from a database before providing it to a user. It will also take additional query parameters, allowing users to filter by fields other than ID.

### Designing Requests
- The prevailing design philosophy of modern APIs is called **REST**. The most important thing about REST is that it's based on the four methods defined by the HTTP protocol : **`POST, GET, PUT and DELETE`**.
- Here we will be dealing with the **`GET requests`** which corresponds to reading from a database.

### Connecting our API to a Database
- This last example of our API pulls in data from a database, implements error handling and can filter books by publication.
- The database used is SQLite, a light weight database engine that is supported by python by default.
- SQLite files typically end with the **`.db`** file extension.
- try out the filtering functionality with these HTTP requests:

```python
http://127.0.0.1:5000/api/v1/resources/books/all
http://127.0.0.1:5000/api/v1/resources/books?author=Connie+Willis
http://127.0.0.1:5000/api/v1/resources/books?author=Connie+Willis&published=1999
http://127.0.0.1:5000/api/v1/resources/books?published=2010
```

- The first request returns all entries in the database, similar to the `/all` request we implemented for the last version of our API.
- The second request returns all books by the author `Connie Willis` **`(?author=Connie+Willis)`** .Note that, within a query parameter, spaces between words are denoted with a **+** sign, hence **Connie+Willis**.
- The third request filters by two fields-author and year of publication

### Understanding our Database-Powered API
- First, we connect to the database using our **sqlite3** library.
- **conn** variable represents connection to the database.
- The **conn.row_factory = dict_factory** line lets the connection object know to use the **dict_factory function**, which returns items from the database as dictionaries rather than lists-these work better when we output them to JSON.
- We then create a cursor object **(cur = conn.cursor() )**, which is the object that actually moves through the database to pull our data.
- Finally, we execute an SQL query with the **`cur.execute`** method to pull our data from the **books** table of our database.
- In HTML responses the code **200** means **"OK"** (the expected data transferred), while the code **404** means **"Not Found"**


## Acknowledgement

- https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#creating-the-api


































































