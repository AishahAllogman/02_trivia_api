## Full Stack Trivia API project

trivia app  is  project  with  question answering game from Udacity  to improve ability to structure plan, implement, and test an API – 
this project implementing the following functionality 
1.	Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2.	Delete questions.
3.	Add questions and require that they include question and answer text.
4.	Search for questions based on a text query string.
5.	Play the quiz game, randomizing either all questions or within a specific catego
## Project Frontend 
Installing Dependencies
Installing Node and NPM
This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from https://nodejs.com/en/download.
Installing project dependencies
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the frontend directory of this repository. After cloning, open your terminal and run:
npm install
tip: npm i is shorthand for npm install
Required Tasks
Running Your Frontend in Dev Mode
The frontend app was built using create-react-app. In order to run the app in development mode use npm start. You can change the script in the package.json file.
Open http://localhost:3000 to view it in the browser. The page will reload if you make edits.
npm start

## Project  Backend
Installing Dependencies
Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs
# Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found  in the python docs
# PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:
```
pip install -r requirements.txt
```
This will install all of the required packages we selected within the requirements.txt file.
# Key Dependencies
-	Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.
-	SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.
- Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.
## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```
psql trivia < trivia.psql
```
## Running the server
From within the backend directory first ensure you are working using your created virtual environment.
To run the server, execute:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

### API Reference 

##	Getting Started
-	Base URL: Currently this application is only hosted locally. The backend is hosted at http://127.0.0.1:5000/
-	Authentication: This version does not require authentication or API keys.
# Errors
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
•	400: Bad Request
•	404: Resource Not Found
•	422: Not Processable

## GET /categories
# General:
- Returns a list of category objects, success value
-	Sample: curl http://127.0.0.1:5000/ categories 
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```
## GET /questions
#	General:
-	Returns a list of question objects, success value, and total number of question, general categroy
-	Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
-	Sample: $ curl  http://127.0.0.1:5000/questions
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 21
}
```
## DELETE /questions/{question_id}
#	General:
-	Deletes the question of the given  ID if it exists. Returns the json object ( id of the deleted question, success value, total question )
-	Sample : $ curl -X DELETE  http://127.0.0.1:5000/questions/26
```
{
  "deleted": 26, 
  "success": true, 
  "total_question": 20
}
```
## POST /questions
# General:
- Creates a new question using the submitted json parameter ( question, answer,category, and difficulty)
- Returns the json object (id of the created question , success value, total question , and questions  list based on current page number to update the frontend.)
- Sample : $ curl http://127.0.0.1:5000/questions -X POST -H "Content-Type:application/json" -d '{"question":"what is national fruit in Saudi Arabia?", "answer":"date","categroy":3,"difficulty":1}'
```
{
  "created": 35, 
  "question": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
```  

## POST /search/questions
#	General:
- Search question with term word as json request parameter 

-	Returns the json object with (questions ,success value, total number for question in search.)

-	Sample: curl  http://127.0.0.1:5000/search/questions -X POST -H "Content-Type:application/json" -d '
```
{"searchTerm":"what"}'

{
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "aisha", 
      "category": 3, 
      "difficulty": 4, 
      "id": 24, 
      "question": "what is your name?"
    }, 
    {
      "answer": "aisha", 
      "category": 3, 
      "difficulty": 4, 
      "id": 25, 
      "question": "what is your name?"
    }, 
    {
      "answer": "latifha", 
      "category": 2, 
      "difficulty": 4, 
      "id": 33, 
      "question": "what is your mama's name "
    }
  ], 
  "success": true, 
  "total_questions": 9
}
```
## Get  /categories/{category_id}/questions

-	General : 
   Get question by category  request parameter  (  category_id)
   Return json object with category id, success values ,question , number of question 

-	Sample :  curl  http://127.0.0.1:5000/categories/2/questions
```
"categories": 2, 
  "questions": [
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "latifha", 
      "category": 2, 
      "difficulty": 4, 
      "id": 33, 
      "question": "what is your mama's name "
    }
  ], 
  "success": true, 
  "total_questions": 5
}
```
## Post/quizzes
Allow user to play games  with random question on selected category 
 -	Request parameter is : previous_questions, quiz_category
 -	Returns JSON object with random question
Sample : curl  http://127.0.0.1:5000/quizzes -X POST -H "Content-Type:application/json" -d '{"previous_questions": [],"quiz_category": {"type": "History", "id": 4}}'
```
{
  "categories": {
    "id": 4, 
    "type": "History"
  }, 
  "question": {
    "answer": "George Washington Carver", 
    "category": 4, 
    "difficulty": 2, 
    "id": 12, 
    "question": "Who invented Peanut Butter?"
  }, 
  "success": true
}
```
#### Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```