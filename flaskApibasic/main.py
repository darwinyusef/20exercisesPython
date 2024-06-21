from sqlalchemy import create_engine, Column, Integer, String, delete, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection string (modify for your file path)
DATABASE_URL = 'sqlite:///crud.db'

# Create engine for connecting to the SQLite database
engine = create_engine(DATABASE_URL)

# Create a declarative base for our models
Base = declarative_base()

# Define the model class for our data (replace 'Task' and attributes as needed)


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)


# Create all tables in the database (if they don't exist)
Base.metadata.create_all(engine)

# Create a session factory for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Function to create a new task
def create_task(db, title, description=None):
    new_task = Task(title=title, description=description)
    db.add(new_task)
    db.commit()
    return new_task


# Function to read all tasks
def read_tasks(db):
    return db.query(Task).all()


# Function to read a single task by ID
def read_task(db, task_id):
    return db.query(Task).filter(Task.id == task_id).first()


# Function to update a task
def update_task(db, task_id, title=None, description=None):
    task = read_task(db, task_id)
    if task:
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        db.commit()
        return task
    else:
        return None


# Function to delete a task
def delete_task(db, task_id):
    task = read_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
        return task
    else:
        return None


# Example usage
if __name__ == '__main__':
    with get_db() as db:
        # Create some tasks
        create_task(db, title="Learn SQLAlchemy")
        create_task(db, title="Build a CRUD application",
                    description="Using SQLAlchemy and SQLite")

        # # Read all tasks
        # tasks = read_tasks(db)
        # for task in tasks:
        #     print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}")

        # # Update a task
        # updated_task = update_task(
        #     db, task_id=1, title="Master CRUD operations")
        # print(f"Updated task: {updated_task.title}")

        # # Delete a task
        # deleted_task = delete_task(db, task_id=2)
        # print(f"Deleted task (ID: {deleted_task.id})")
