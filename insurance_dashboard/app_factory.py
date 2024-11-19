from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask app
def create_app():
    app = Flask(__name__)
    
    # Configure Flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Replace with your DB URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions (e.g., SQLAlchemy)
    db = SQLAlchemy(app)

    # Register Blueprints if any (optional)
    # from your_blueprint import your_blueprint
    # app.register_blueprint(your_blueprint)

    # Add routes (for testing)
    @app.route("/")
    def home():
        return "Insurance Dashboard API"

    return app
