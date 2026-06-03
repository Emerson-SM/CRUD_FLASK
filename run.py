from app import create_app
from app.database.db import db
from app.database.db import db 
from app.database.models.users_model import User

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)