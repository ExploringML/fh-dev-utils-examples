from fasthtml.common import *
from fh_dev_utils.serve import *

DEV_MODE=True

app,rt,todos,ToDo = fast_app('data/todos.db', id=int, title=str, pk='id', pico=True, live=True)

if not todos(): # Seed database if empty
    todos.insert_all([
        {"title": "Buy groceries"},
        {"title": "Finish blog post"},
        {"title": "Reply to emails"},
        {"title": "Plan weekend trip"},
        {"title": "Read AI research paper"}
    ]
)

def TodoRow(todo): return Li(todo.title, href=f'/todos/{todo.id}', id=f'todo-{todo.id}')

def home():
    add = Form(
            Group(
                Input(name="title", placeholder="New Todo"),
                Button("Add")
            ), action="/", method='post'
        )
    card = Card(
                Ul(*map(TodoRow, todos()), id='todo-list', style="padding:20px;"),
                header=add,
                footer=Div(id='current-todo')
            )
    return Titled('Todo list', card)

@rt("/")
def get(): return home()

@rt("/")
def post(todo:ToDo):
    todos.insert(todo)
    return home()

if DEV_MODE: serve_dev(db=True, db_path='data/todos.db')
else: serve()