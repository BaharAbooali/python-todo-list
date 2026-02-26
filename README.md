# python-todo-list
A simple command-line To-Do List application built with Python that stores tasks using JSON.

## Features

- View tasks in a numbered list
- Add new tasks
- Mark tasks as done
- Delete tasks
- Tasks are saved automatically using `tasks.json`
- Emoji indicators for task status

## Technologies Used

- Python
- JSON
- File handling
- Dictionaries and lists
- f-strings
- emoji library

## How It Works

Tasks are stored in a JSON file like this:


json
[
    {
        "title": "Go to gym",
        "done": true
    }
]
`

When the program starts, it loads tasks from the file.
Whenever a task is added, updated, or deleted, the file is updated automatically.

## What I Learned

* Working with JSON data in Python
* Reading and writing files
* Managing persistent data
* Building interactive CLI applications
* Structuring clean and readable code

## How to Run

Run the following commands:

pip install emoji (if you don't have this package yet)

python main.py
