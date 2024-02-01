# Python Code Checker

This is a simple web app that allows you to check the syntax of your python code. You can enter any python code in the form and get instant feedback on whether it is valid or not. If it is invalid, you will also see the error message.

## How it works

The app uses the built-in `ast` module to parse the code as an abstract syntax tree. If the parsing succeeds, the code is syntactically valid. If the parsing fails, a `SyntaxError` exception is raised and caught by the app. The app then returns the error message to the user.

The app is built with the `Flask` framework and uses `render_template` to display the HTML pages. The app has two routes: `/` for the home page and `/result` for the result page. The home page contains a form where the user can enter the code. The result page shows the feedback on the code.

## How to run it

To run the app, you need to have `python` and `Flask` installed on your system. You can install `Flask` with the command:

```bash
pip install Flask
```

Then, you can run the app with the command:

```bash
python app.py
```

The app will run on `http://localhost:5000/` by default. You can change the port number by passing it as an argument to the `app.run` function.

## Example

Here is an example of how the app looks like:

app.py; <br> [![initial-app-run.png](https://i.postimg.cc/ncBKVRyw/initial-app-run.png)](https://postimg.cc/BXZPMgQx) <br>
<br>
Browser first opens; <br> [![initial-browser-open.png](https://i.postimg.cc/DwcqLWyr/initial-browser-open.png)](https://postimg.cc/yDkgz8Rx) <br>
<br>
Input Python code i know is correct; <br> [![input-python-code-i-know-works.png](https://i.postimg.cc/mrXCp09h/input-python-code-i-know-works.png)](https://postimg.cc/3yGkdfnH) <br>
<br>
Get results from correct code; <br> [![output-code-i-know-is-correct.png](https://i.postimg.cc/W1VGdmjp/output-code-i-know-is-correct.png)](https://postimg.cc/6yH2SvyF) <br>
<br>
Input Python code i know is incorrect; <br> [![output-code-i-know-is-correct.png](https://i.postimg.cc/W1VGdmjp/output-code-i-know-is-correct.png)](https://postimg.cc/6yH2SvyF) <br>
<br>
Get error results; <br> [![error-results.png](https://i.postimg.cc/L4qBw6NS/error-results.png)](https://postimg.cc/nMJDQxyS)<br>
<br>

## Licence

MIT <br>
Created by Stuart Elliott <br>
Free to use!!