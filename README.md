# Full Stack Number to English Translator

### Overview

This project was built using React.js on the frontend and Django on the backend.

### Instructions to Run the Code

1. Start up a virtual environment using "python -m venv venv"
2. Activate the virtual environment using "source venv/bin/activate"
3. Navigate to the directory where the requirements.txt is located.
4. Run the command "pip install -r requirements.txt"
5. Navigate into the frontend folder, and run the command "npm run dev"
6. In another terminal navigate to the directory where manage.py is located.
7. Run "python manage.py runserver"
8. Visit http://localhost:8000/num_translator in your browser to view the landing page or try hitting the API endpoints (see below).

### views.py

There are two API endpoints:
GET = /num_to_english?number=12345678
POST = /num_to_english
{
"number": "12345678"
}

You can use curl to send a post request to the backend:
curl -X POST http://localhost:8000/api/num_to_english -H "Content-Type: application/json" -d '{"number": "12345678"}'

These API endpoints take in a string or an int of a number and return an english translation of the number in the form of a string.

### utilities.py

The algorithm is built in a class called TranslateNumber that resides in the utilities.py folder. The algorithm is my 100% original work. It translates numbers 0 <= n <= 1,000,000,000,000

### tests.py

The algorithm passes substantial testing when takes place in the api/tests.py file. To run these tests navigate to the directory containing the manage.py file, and then run the command "python manage.py test".

Notice that the algorithm passes all of the tests.

### frontend

The frontend was built using React.js
All inputs on the main input form have both frontend and backend validation.

GET requests are instantaneous and appear above the input field.
POST requests are asycnhronous and appear below the input field in 5 seconds. A spinner is displayed during the loading time.

visit http://localhost:8000/num_translator in your browser to view the landing page.

### Thanks!

Thank you for checking out my project.
