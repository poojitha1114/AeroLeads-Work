# How to Build a Simple Web App with Flask

---
title: How to Build a Simple Web App with Flask: Your Beginner-Friendly Guide
description: Learn how to build your first web application using Flask, the lightweight Python web framework. This step-by-step tutorial covers setup, templates, static files, and handling user input.
keywords: Flask web app, build web app Flask, Flask tutorial, Python web development, simple Flask app, Flask for beginners, Flask templates, Flask forms, create web app Python
---

## Introduction: Embark on Your Web Development Journey with Flask

Ever wondered how websites and web applications are built? If you're familiar with Python and curious about web development, Flask is an excellent place to start! Flask is a lightweight and flexible web framework that allows you to build powerful web applications with minimal fuss. Its simplicity makes it ideal for beginners, while its extensibility offers enough power for complex projects.

In this detailed, step-by-step guide, we'll walk you through building a simple web application using Flask. We'll cover everything from setting up your environment to handling user input, providing you with a solid foundation to create your own Flask projects.

**What We'll Build:** A very basic "To-Do List" application that allows you to add and display tasks. This will introduce you to core Flask concepts like routing, templates, and forms.

## Section 1: Prerequisites & Environment Setup

Before we dive into coding, let's make sure you have the necessary tools and set up a clean development environment.

### 1.1 What You'll Need:

*   **Python 3:** Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
*   **Text Editor/IDE:** A good text editor like [VS Code](https://code.visualstudio.com/), Sublime Text, or PyCharm will make coding much easier.

### 1.2 Setting Up Your Virtual Environment

A virtual environment is crucial for Python projects. It isolates your project's dependencies from other Python projects, preventing conflicts.

1.  **Create a Project Folder:**
    Let's start by creating a new directory for our project.
    ```bash
    mkdir flask_todo_app
    cd flask_todo_app
    ```

2.  **Create a Virtual Environment:**
    Inside your `flask_todo_app` directory, run the following command:
    ```bash
    python3 -m venv venv
    ```
    (On some systems, `python` might suffice instead of `python3`).

3.  **Activate the Virtual Environment:**
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    *   **Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    *   **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    You'll know it's active when you see `(venv)` preceding your terminal prompt.

4.  **Install Flask:**
    With your virtual environment activated, install Flask using `pip`:
    ```bash
    pip install Flask
    ```
    This will install Flask and its dependencies.

## Section 2: Your First Flask App – "Hello, Flask!"

Let's write the simplest possible Flask application to get things rolling.

1.  **Create `app.py`:**
    Inside your `flask_todo_app` directory, create a new file named `app.py`.

2.  **Add the Basic Flask Code:**
    Open `app.py` and add the following code:

    ```python
    # app.py

    from flask import Flask

    # Create a Flask application instance
    # The __name__ argument helps Flask determine the root path for resources
    app = Flask(__name__)

    # Define a route for the home page ('/')
    # This decorator tells Flask which URL should trigger our function
    @app.route('/')
    def hello_flask():
        """This function will be called when someone visits the home page."""
        return "<h1>Hello, Flask! Welcome to your first web app.</h1>"

    # This block ensures the server runs only when the script is executed directly
    if __name__ == '__main__':
        # Run the Flask development server
        # debug=True enables debug mode, which provides helpful error messages
        # and automatically reloads the server on code changes.
        app.run(debug=True)
    ```

3.  **Run Your App:**
    Make sure your virtual environment is active, then run your app from the terminal:
    ```bash
    python app.py
    ```

    You should see output similar to this:
    ```
     * Serving Flask app 'app'
     * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: ...
    ```

4.  **View in Browser:**
    Open your web browser and navigate to `http://127.0.0.1:5000/`. You should see "Hello, Flask! Welcome to your first web app." displayed. Congratulations, you've built your first Flask web app!

## Section 3: Introducing HTML Templates with Jinja2

Returning HTML directly from Python strings works for simple cases, but it quickly becomes unmanageable for complex web pages. Flask uses Jinja2 as its templating engine, allowing you to separate your Python logic from your HTML presentation.

1.  **Create a `templates` Folder:**
    Flask expects your HTML templates to be in a folder named `templates` in your project root.
    ```bash
    mkdir templates
    ```

2.  **Create `index.html`:**
    Inside the `templates` folder, create a new file named `index.html`.

3.  **Add Basic HTML to `index.html`:**
    ```html
    <!-- templates/index.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask To-Do App</title>
    </head>
    <body>
        <h1>Welcome to Your To-Do List!</h1>
        <p>This page is rendered from an HTML template.</p>
        <p>Hello, {{ user_name }}!</p>
    </body>
    </html>
    ```
    Notice `{{ user_name }}`. This is Jinja2 syntax for displaying a variable passed from your Flask application.

4.  **Update `app.py` to Render the Template:**
    Modify your `app.py` to import `render_template` and use it:

    ```python
    # app.py

    from flask import Flask, render_template # Import render_template

    app = Flask(__name__)

    @app.route('/')
    def index(): # Renamed the function to 'index' for clarity
        """Renders the home page using an HTML template."""
        # Pass data to the template using keyword arguments
        return render_template('index.html', user_name="Awesome Developer")

    if __name__ == '__main__':
        app.run(debug=True)
    ```

5.  **Restart and View:**
    If your server is still running, it should auto-reload (thanks to `debug=True`). If not, stop it (`CTRL+C`) and run `python app.py` again. Refresh your browser at `http://127.0.0.1:5000/`. You should now see the content from `index.html`, with "Awesome Developer" displayed.

## Section 4: Adding Static Files (CSS & JavaScript)

Web applications often need CSS for styling and JavaScript for interactivity. Flask serves these "static" files from a special `static` folder.

1.  **Create a `static` Folder:**
    In your project root (`flask_todo_app`), create a folder named `static`.
    ```bash
    mkdir static
    ```

2.  **Create `style.css`:**
    Inside the `static` folder, create a file named `style.css`.

3.  **Add Some CSS to `style.css`:**
    ```css
    /* static/style.css */
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        color: #333;
        margin: 20px;
        line-height: 1.6;
    }
    h1 {
        color: #0056b3;
        border-bottom: 2px solid #0056b3;
        padding-bottom: 10px;
    }
    .container {
        max-width: 800px;
        margin: auto;
        background: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    ```

4.  **Link CSS in `index.html`:**
    Update your `templates/index.html` file to link to the stylesheet. Flask provides `url_for()` to generate URLs for static files.

    ```html
    <!-- templates/index.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask To-Do App</title>
        <!-- Link to our static CSS file -->
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Your To-Do List!</h1>
            <p>This page is rendered from an HTML template.</p>
            <p>Hello, {{ user_name }}!</p>
        </div>
    </body>
    </html>
    ```
    The `url_for('static', filename='style.css')` call dynamically generates the correct path to your `style.css` file.

5.  **Restart and View:**
    Refresh your browser. You should now see your page with the new styling applied!

## Section 5: Handling User Input with Forms (Building the To-Do App)

Now, let's make our To-Do app functional by allowing users to add tasks. This involves HTML forms and handling `POST` requests in Flask.

**Important Note:** For simplicity, we'll store tasks in a global Python list. In a real application, you would use a database (like SQLite with SQLAlchemy) to persist data.

1.  **Update `app.py`:**
    We need to import `request` and `redirect`, and we'll have a global list to store our tasks. We'll also modify our `index` route to handle both `GET` (displaying the page) and `POST` (submitting a new task).

    ```python
    # app.py

    from flask import Flask, render_template, request, redirect, url_for # Import request, redirect, url_for

    app = Flask(__name__)

    # A simple list to store our tasks (for demonstration purposes only)
    tasks = []

    @app.route('/', methods=['GET', 'POST']) # Allow both GET and POST requests
    def index():
        if request.method == 'POST':
            task_content = request.form.get('task_content') # Get data from the form
            if task_content: # Check if the task content is not empty
                tasks.append(task_content)
            return redirect(url_for('index')) # Redirect back to the home page after adding
        
        # For GET requests, render the template and pass the tasks
        return render_template('index.html', user_name="Awesome Developer", tasks=tasks)

    if __name__ == '__main__':
        app.run(debug=True)
    ```

2.  **Update `index.html`:**
    We need to add a form for input and a loop to display the tasks.

    ```html
    <!-- templates/index.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask To-Do App</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
        <style>
            /* Add some specific styles for our To-Do list */
            form {
                margin-bottom: 20px;
            }
            form input[type="text"] {
                width: 70%;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            form input[type="submit"] {
                padding: 8px 15px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            form input[type="submit"]:hover {
                background-color: #0056b3;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                background-color: #e9ecef;
                padding: 10px;
                margin-bottom: 8px;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>My To-Do List</h1>
            <p>Hello, {{ user_name }}!</p>

            <!-- Form to add new tasks -->
            <form method="POST" action="{{ url_for('index') }}">
                <input type="text" name="task_content" placeholder="Add a new task..." required>
                <input type="submit" value="Add Task">
            </form>

            <h2>Current Tasks:</h2>
            <ul>
                <!-- Loop through the tasks list and display each one -->
                {% if tasks %}
                    {% for task in tasks %}
                        <li>{{ task }}</li>
                    {% endfor %}
                {% else %}
                    <li>No tasks yet! Add one above.</li>
                {% endif %}
            </ul>
        </div>
    </body>
    </html>
    ```
    Key points in `index.html`:
    *   `<form method="POST" action="{{ url_for('index') }}">`: This form will send a `POST` request to the `/` route.
    *   `<input type="text" name="task_content">`: The `name="task_content"` attribute is crucial, as Flask's `request.form.get('task_content')` uses it to retrieve the input value.
    *   `{% if tasks %}` / `{% for task in tasks %}`: These are Jinja2 control structures that allow you to add logic (like loops and conditionals) directly in your templates.

3.  **Restart and Test:**
    Restart your Flask app. Now, when you visit `http://127.0.0.1:5000/`, you'll see an input field. Type a task and click "Add Task". The page will refresh, and your task will appear in the list!

## Section 6: Next Steps & Beyond

You've built a functional (albeit simple) web application with Flask! This is just the beginning. Here are some ideas for where to go next:

*   **Database Integration:** Replace the global `tasks` list with a proper database (e.g., SQLite, PostgreSQL) using an ORM like **SQLAlchemy**. This is essential for persistent data.
*   **Update and Delete Functionality:** Extend your To-Do app to allow editing and deleting tasks.
*   **User Authentication:** Learn how to implement user login, registration, and sessions (e.g., using Flask-Login).
*   **Form Validation:** Ensure user input meets specific criteria (e.g., a task cannot be empty) using libraries like **Flask-WTF**.
*   **REST APIs:** Learn how to build APIs with Flask to serve data to other applications (e.g., mobile apps, single-page applications).
*   **Blueprints:** As your application grows, organize it into modular components using Flask Blueprints.
*   **Deployment:** Learn how to deploy your Flask app to production servers using services like Heroku, Vercel, AWS, or DigitalOcean.

## Conclusion: Your Journey as a Flask Developer Begins!

Congratulations! You've successfully built a simple web application using Flask. You've learned how to:

*   Set up a Python virtual environment.
*   Create a basic Flask application with routes.
*   Use Jinja2 templating to render dynamic HTML.
*   Serve static files like CSS.
*   Handle user input from HTML forms using `GET` and `POST` requests.

Flask's elegant design and Pythonic nature make it a joy to work with. Keep experimenting, keep building, and don't hesitate to consult the official [Flask documentation](https://flask.palletsprojects.com/en/latest/) for deeper dives into specific topics. The world of web development is vast, and you've taken a fantastic first step with Flask!

---
