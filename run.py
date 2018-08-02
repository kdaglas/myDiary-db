import os
from app import app
from app.database import dbController


if __name__ == "__main__":
    dbUtils = dbController.DatabaseConnection()
    dbUtils.create_tables()
    app.run(debug=True)
