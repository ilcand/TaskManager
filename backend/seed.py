
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Task, Base
from datetime import datetime, timezone

DATABASE_URL = "postgresql://postgres:postgres@db:5432/tasks_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create tables if not exist (redundant safety)
Base.metadata.create_all(bind=engine)

def seed_data():
    session = SessionLocal()
    # Clear existing tasks
    session.query(Task).delete()
    # Add dummy tasks
    tasks = [
        Task(title="Buy groceries", description="Milk, Bread, Cheese"),
        Task(title="Finish FastAPI app", description="Add seed script"),
        Task(title="Read a book", description="At least 20 pages"),
    ]
    session.add_all(tasks)
    session.commit()
    for task in tasks:
        print(f"Task '{task.title}' inserted with ID: {task.id}")
    
    session.close()
    print("Seeded DB with dummy tasks.")

if __name__ == "__main__":
    seed_data()