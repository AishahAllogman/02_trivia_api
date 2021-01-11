import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def paginate_question(request, selection):
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions= [question.format() for question in selection]
    current_questions= questions[start:end]

    return current_questions
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app,rsources={r"/api/*": {"origins": "*"}})
  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def reteirve_categories():
    categories=Category.query.order_by(Category.id).all()
    category={}
    for Categories in categories:
       category[Categories.id]=Categories.type
    if len(category)==0:
       abort(404)
    return jsonify({
      'success':True,
      'categories': category})

  '''
    @TODO: 
    Create an endpoint to handle GET requests for questions, 
    including pagination (every 10 questions). 
    This endpoint should return a list of questions, 
    number of total questions, current category, categories. 

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def retrieve_questions():
        selection = Question.query.all()
        current_question = paginate_question(request, selection)
        categories=Category.query.order_by(Category.id).all()
        category={}
        for Categories in categories:
            category[Categories.id]=Categories.type
        if len(category)==0:
            abort(404)

        if len(current_question) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_question,
            'total_questions': len(selection),
            'categories': category,
            'current_category': None
        })
  '''
    @TODO: 
    Create an endpoint to DELETE question using a question ID. 

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
        try:
          question= Question.query.get(question_id)
          if question is None:
                abort(404)

          question.delete()
          return jsonify({
                'success': True,
                'deleted': question_id,
                'total_question': len(Question.query.all())
          })
        
        except:
            print(sys.exc_info())
            abort(422)
  '''  
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
  '''  
  @app.route('/questions', methods=['POST'])
  def create_question():
      body = request.get_json()
      new_question = body.get('question', None)
      new_answer = body.get('answer', None)
      new_category = body.get('category', None)
      new_difficulty = body.get('difficulty', None)
      try:
            question = Question(question=new_question, answer=new_answer,category=new_category,difficulty=new_difficulty)
            question.insert()
            selection = Question.query.order_by(Question.id).all()
            current_question = paginate_question(request, selection)
          
            return jsonify({
                'success': True,
                'created': question.id,
                'question': current_question,
                'total_books': len(Question.query.all())
            })
      except:
            print(sys.exc_info())
            abort(422)
  '''  
    @TODO: 
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 

    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start.   
  '''
  @app.route('/search/questions', methods=['POST'])
  def search_question():
      body = request.get_json()
      searchTerm= body.get('searchTerm', None)
      questions=[]
      try:
          question=Question.query.filter(Question.question.ilike('%'+ searchTerm+'%')).all()
          if len(question)==0:
            abort (422)
          for q in question:
            questions.append({
              'id':q.id,
              'question':q.question,
              'answer':q.answer,
              'difficulty':q.difficulty,
              'category':q.category
            })  
          print(questions)
          return jsonify({
                'success': True,
                'questions': questions,
                'total_questions': len(questions)
          })
      except:
            print(sys.exc_info())
            abort(422)
                        
                        
  
  @app.route('/categories/<int:category_id>/questions')
  def get_questions_by_categories(category_id):
        selection = Question.query.filter(Question.category==category_id)
        current_question = paginate_question(request, selection)
        Questions=[]
        for question in selection:
            Questions.append(question.format())

        if len(current_question) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': Questions,
            'total_questions': len(Questions),
            'categories': category_id
        })
      
 
  @app.route('/quizzes', methods=['POST'])
  def quizzes():
      body = request.get_json()
      quiz_category = body.get('quiz_category', None)
      previous_questions = body.get('previous_questions', None)
      if quiz_category['id']==0:
        question= Question.query.all()
      else:
        question= Question.query.filter(Question.category==quiz_category['id']).all()
      questions=[]
      for q in question: 
        if q.id not in previous_questions:
          questions.append({
            'id':q.id,
            'question':q.question,
            'answer':q.answer,
            'difficulty':q.difficulty,
            'category':q.category
          })   
      return jsonify({
                    'success': True,
                    'question': random.choice(questions),
                    'categories': quiz_category
                })
  '''
      @TODO: 
      Create error handlers for all expected errors 
      including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
        return jsonify({
                "success": False, 
                "error": 404,
                "message": "resource not found"
        }), 404

  @app.errorhandler(422)
  def unprocessable(error):
          return jsonify({
                "success": False, 
                "error": 422,
                "message": "unprocessable"
          }), 422

  @app.errorhandler(400)
  def bad_request(error):
          return jsonify({
                "success": False, 
                "error": 400,
                "message": "bad request"
            }), 400
      
  return app

    