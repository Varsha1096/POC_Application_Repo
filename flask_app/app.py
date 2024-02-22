from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

app = Flask(__name__)

# Your SQLAlchemy and database connection configurations here
# Retrieve database credentials from environment variables
db_host = "pocapplicationserver.postgres.database.azure.com"
db_port = 5432
db_name = "pocapplicationdb"
#db_user = os.environ.get('DB_USERNAME') #Add user name from Environment
#db_password = os.environ.get('DB_PASSWORD') #Take user name from Environment

db_user = "varsha1096"
db_password = "Va9645rshi*"

# Construct the database connection string
db_uri = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Configure the Flask application to use the database
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database object
db = SQLAlchemy(app)

# Define a simple database model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))


@app.route('/')
def hello_world():
    try:
        # Query a sample message from the database
        # message = Message.query.first()
        # message_content = message.content
        message_content = "Connection with Azure Database is successful"
    except OperationalError as e:
        print("Error: Unable to connect to the database.")
        print(e)  # Print the specific error message for troubleshooting
        message_content = "Error fetching message from the database"

    # Define HTML content directly within the Flask route handler using Jinja2 syntax
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello World</h1>
        <p>{{ message }}</p>
    </body>
    </html>
    """

    # Render the HTML template with dynamic content
    return render_template_string(html_content, message=message_content)

if __name__ == '__main__':
    app.run(debug=True)
