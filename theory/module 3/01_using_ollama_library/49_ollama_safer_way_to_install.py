'''
Q1. Why is "python -m pip install ollama" considered safer?

A.
Because it ensures that pip runs from the exact Python interpreter you are using.
This avoids installing the package into the wrong Python environment.
'''
# Example:
# If you have Python 3.10 and 3.12 installed,
# python3.12 -m pip install ollama
# ensures installation into Python 3.12



'''
Q2. What problem can happen with just "pip install ollama"?

A.
It may install the package into a different Python version
than the one running your script.
'''
# Example:
# pip installs into Python 3.10
# But you run script with Python 3.12
# → ModuleNotFoundError



'''
Q3. What does the "-m" flag mean in this command?

A.
"-m" tells Python to run a module as a script.
Here, it runs the pip module using that Python interpreter.
'''
# Example:
# python -m pip
# means "use this Python to execute pip"



'''
Q4. When is this especially important?

A.
It is important when:
- Multiple Python versions exist
- Virtual environments are used
- System Python and user Python differ
'''
# Example:
# Inside venv:
# python -m pip install ollama
# ensures installation inside that virtual environment



'''
Q5. What is the safest mental model for installing packages?

A.
Always tie pip to the Python interpreter you plan to use.
Use:
python -m pip install <package>
'''
# Example:
# python -m pip install ollama
# Then run:
# python app.py
