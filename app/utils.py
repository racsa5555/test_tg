from models import Tasks
from typing import List

def pretty_tasks(tasks:List[Tasks]):
    pretty_res = ''
    k = 1
    for task in tasks:
        pretty_res += f'{k}.{task.description}\n'
        k+=1
    return pretty_res
