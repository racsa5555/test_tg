from config import session
from models import Tasks

def create_task(description:str):
    with session() as db:
        try:
            task = Tasks(description=description)
            db.add(task)
            db.commit()
            return True
        except:
            return False
        

def get_tasks():
    with session() as db:
        try:
            tasks = db.query(Tasks).all()
            return tasks
        except:
            return False