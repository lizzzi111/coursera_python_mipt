import json
import functools

def to_json(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = json.dumps(function(*args, **kwargs))
        return result
    return wrapper


@to_json
def get_data():
  return {
    'data': 42
  }

get_data()
