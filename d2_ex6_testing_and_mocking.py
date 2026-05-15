import requests
import json

URL = "https://jsonplaceholder.typicode.com/todos"


# a function that fetches a lists of todos
# and by default filters for those not completed
def get_todos(url, completed=False):
    # don't forget to pip install requests
    response = requests.get(url)

    # we never crash, and return an empty list
    if response.status_code != 200:
        return []
    
    # also if the endpoint sent malformed response
    try:
        todos = json.loads(response.text)
    except json.JSONDecodeError:
        return []
    
    if completed is None:
        return todos
    
    return [
        todo
        for todo in todos
        if todo['completed'] == completed
    ]

# write tests that do not hit the remote API,
# that:
# - simulate an http response different from 200
# - simulate a json.JSONDecodeError

