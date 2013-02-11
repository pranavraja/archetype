
# Archetype

Create project boilerplate from template folders. This is a quick hack / work in progress, I don't expect it to be useful to anyone else.

# Setup

- Clone repo, run `pip install -r requirements.txt` (preferably from within a [virtualenv](http://www.virtualenv.org/en/latest/)). 

# Usage 

- Run `python create.py` to see usage. See the `example/` directory for an example of a template project setup for a flask WSGI application.

Expressions of the form `{{ variable }}`, in file/folder paths and file contents, will be replaced with the values of the variables in the environment (using Jinja2 templates).

# Environment

The following environment variables will be available by default:

- `APP_DIR` - the path to the parent directory in which the new app is created
- `APP_PATH` - the full path to the app folder
- `APP_NAME` - the name of the app (generated by stripping punctuation from the app folder name)

You can add other variables by referencing an `env` file with key-value pairs. An example of an env file:

```
TEST_PARAM=test_value
ANOTHER_PARAM=another_value
```