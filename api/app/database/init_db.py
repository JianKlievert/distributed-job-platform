from app.database.database import engine, Base
from app.models.user import User
from app.models.job import Job

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")
