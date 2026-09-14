from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

# Create the FastAPI application
app = FastAPI()

# Define the SQLite database location
DATABASE_URL = "sqlite:///./test.db"

# Create the database engine used to connect with SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required for SQLite with FastAPI
)

# Create a factory that generates database sessions
sessionLocal = sessionmaker(bind=engine)

# Create a base class that database models will inherit from
Base = declarative_base()


# Create the Todo model that represents the "todos" table
class Todo(Base):
    __tablename__ = "todos"  # Define the database table name

    id = Column(Integer, primary_key=True, index=True)  # Unique ID for each todo
    title = Column(String)  # Store the todo title
    completed = Column(String)  # Store the todo completion status


# Create the Todo table in the database if it does not already exist
Base.metadata.create_all(bind=engine)


# Create a database session for each request
def get_db():
    db = sessionLocal()
    try:
        yield db  # Provide the database session to the API endpoint
    finally:
        db.close()  # Close the database session after the request is completed


# Inject the database session into this API endpoint
@app.get("/")
def home(db: Session = Depends(get_db)):
    return {
        "message": "DB connected successfully"
    }


# Create API
@app.post("/todos")
def create_todo(title: str, db: Session = Depends(get_db)):
    todo = Todo(title=title, completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo created successfully",
        "data": todo
    }

# Read all data
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()

    return {
        "Total": len(todos),
        "data": todos
    }

# Get single data
@app.get("/todos/{todo_id}")
def get_todo(todo_id=int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# Update data
@app.put("/todos/{todo_id}")
def update_todo(todo_id=int, title=str, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = title

    db.commit()

    return {
        "message": "Todo updated successfully",
        "data": todo
    }

# Delete data
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)

    db.commit()

    return {
        "message": "Todo deleted successfully"
    }