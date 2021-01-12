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
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    CORS(app, rsources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/categories')
    def reteirve_categories():
        categories = Category.query.order_by(Category.id).all()
        category = {}
        for Categories in categories:
            category[Categories.id] = Categories.type
        if len(category) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'categories': category})

    @app.route('/questions')
    def retrieve_questions():
        selection = Question.query.all()
        current_question = paginate_question(request, selection)
        categories = Category.query.order_by(Category.id).all()
        category = {}
        for Categories in categories:
            category[Categories.id] = Categories.type
        if len(category) == 0:
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

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)
            if question is None:
                abort(404)

            question.delete()
            return jsonify({
                'success': True,
                'deleted': question_id,
                'total_question': len(Question.query.all())
            })

        except BaseException:
            print(sys.exc_info())
            abort(422)

    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)
        try:
            question = Question(
                question=new_question,
                answer=new_answer,
                category=new_category,
                difficulty=new_difficulty)
            question.insert()
            selection = Question.query.order_by(Question.id).all()
            current_question = paginate_question(request, selection)

            return jsonify({
                'success': True,
                'created': question.id,
                'question': current_question,
                'total_books': len(Question.query.all())
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/search/questions', methods=['POST'])
    def search_question():
        body = request.get_json()
        searchTerm = body.get('searchTerm', None)
        questions = []
        try:
            question = Question.query.filter(
                Question.question.ilike(
                    '%' + searchTerm + '%')).all()
            if len(question) == 0:
                abort(422)
            for q in question:
                questions.append({
                    'id': q.id,
                    'question': q.question,
                    'answer': q.answer,
                    'difficulty': q.difficulty,
                    'category': q.category
                })
            print(questions)
            return jsonify({
                'success': True,
                'questions': questions,
                'total_questions': len(questions)
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/categories/<int:category_id>/questions')
    def get_questions_by_categories(category_id):
        selection = Question.query.filter(Question.category == category_id)
        current_question = paginate_question(request, selection)
        Questions = []
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
        if body is None:
            abort(422)
        quiz_category = body.get('quiz_category', None)
        previous_questions = body.get('previous_questions', None)
        if quiz_category['id'] == 0:
            question = Question.query.all()
        else:
            question = Question.query.filter(
                Question.category == quiz_category['id']).all()
        questions = []
        for q in question:
            if q.id not in previous_questions:
                questions.append({
                    'id': q.id,
                    'question': q.question,
                    'answer': q.answer,
                    'difficulty': q.difficulty,
                    'category': q.category
                })
        return jsonify({
            'success': True,
            'question': random.choice(questions),
            'categories': quiz_category
        })

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
