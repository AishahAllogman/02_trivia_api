import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path =  "postgres://{}/{}".format("localhost:5432",self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question={
            'question':"what is the captial city in Saudi Arabia?",
             'answer':"Riyadh",
             'catogray':3,
             'difficulty':4
        }

        # binds the app to \the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_reteirve_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    def test_404_if_categories_does_not_exist(self):
        res = self.client().get('/categories/100')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')  
    # Teset : to retrieve_questions      
    def test_etrieve_questions(self):
        res = self.client().get('/questions')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['questions'])
        self.assertTrue (len(data['questions']))


    def test_404_sent_retrieve_questions_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'resource not found')
    #to deleete question
    def test_delete_question(self):
       res = self.client().delete('/questions/15')
       data = json.loads(res.data)
       self.assertEqual(res.status_code, 200)
       self.assertEqual(data['success'], True)
       self.assertEqual(data['deleted'], 15)
       #self.assertTrue(data['total_question'])
       #self.assertEqual(question, None)

    def test_404_if_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
    # test : to create new Question
    def test_create_question(self):
        res = self.client().post('/questions',   json=self.new_question)
        data = json.loads(res.data)
        pass
    
    def test_422_if_question_creation_fails(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        pass
    #Test: questions_by_categories
    def test_get_questions_by_categories(self):
        res = self.client().get('/categories/5/questions')
        data = json.loads(res.data)
        question= Question.query.filter(Question.category==5)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])

    def test_404_if_questions_by_categories_does_not_exist(self):
        res = self.client().get('/categories/10/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found') 
    #Test : search Quizz
    def test_search_questions(self):
        request_data= {'searchTerm':'HOW'}
        res = self.client().post('/search/questions',data=json.dumps(request_data),content_type='application/json')                      
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    def test_422_if_notfind_search_questions(self):
        request_data= {'searchTerm':'Where'}
        res = self.client().post('/search/questions',data=json.dumps(request_data),content_type='application/json')                      
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
    # Teset : Quizz
    def test_quizzes(self):
        request_data= {'previous_questions': [1, 2],
            'quiz_category': {'id': 2, 'type': 'Art'}}
        res = self.client().post('/quizzes',data=json.dumps(request_data),content_type='application/json')                      
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    # Teset : Quizz
    def test_quizzes(self):
        request_data= {'previous_questions': [1, 2],
            'quiz_category': {'id': 2, 'type': 'Art'}}
        res = self.client().post('/quizzes',data=json.dumps(request_data),content_type='application/json')                      
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_if_test_quizzes(self):
        request_data= {}
        res = self.client().post('/quizzes') 
        print (res.status_code)        
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
        
    
          


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()