# First we are gonna install virtual environment here in web_server folder.
# By typing python -m venv venv
# Now we are gonna activate virtual environment by typing venv/Scripts/activate
# Now, we finally install Flask, by typing pip install Flask.

from flask import Flask, render_template  # This render_template is used to send HTML files.

app = Flask(__name__)

@app.route("/")  # This / means we are on homepage.
def hello_world():
    return "<p>Hello, My name is John Cena! YOU CAN'T SEE ME...</p>"

# Upper code copied from Flask documentation.

@app.route("/blog")  # This /blog means blog page
def blog():
    return "<p>These are my thoughts on Blogs...</p>"

@app.route("/blog/2021/dog")  # This /blog means blog page
def blog2():
    return "<p>This is my Dog!!!!!!!!!!!!</p>"

# To use an HTML file, REMEMBER, put your html files in a folder called templates, bc flask automatically,
# looks for a folder named templates, for HTML files.

@app.route("/html")  # This /blog means blog page
def html():
    return render_template('index.html')

# Now to add css and JavaScript files to our html, we have to create a static named folder and 
# move them to static folder. Static means those files aren't gonna change.

# To add fevicons (choti si photu jo uprr tabs me aati hai.)
# Visit icon-icons.com (for fevicons)
# Put a link for fevicon in HTML, REMEMBER fevicon image must be in static folder.

# URL parameters
# Flask has a feature called url parameters, in which we pass something in url which is pasted in
# our website.

@app.route("/<username>/<int:post_id>")
def variables(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)  # we have to type this, name
    # and post_id in HTML in 2 curly brackets as well, as we are calling from HTML here, 
    # Username is for string or name, and post id is int So, it is for any number.

# We have to type (export FLASK_APP=server.py), name should be same as of our python file.
# Then with typing (flask run) in command line our server starts.
# Initially the debugging mode is off, it means if we make any change in our website, it won't be
# Initiated even after refreshing the page, unless we run the server again by typing flask run.
# So, to turn on debugging mode we have to type (export FLASK_ENV=development) in command line.
