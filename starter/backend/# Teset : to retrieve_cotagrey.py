 
# Teset : to retrieve_cotagrey   
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
        self.assertTrue(data['question'])
        self.assertTrue (len(data['question']))


  def test_404_sent_retrieve_questions_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'resource not found')


         def test_delete_question(self):
       res = self.client().delete('/questions/25')
       data = json.loads(res.data)
       self.assertEqual(res.status_code, 200)
       self.assertEqual(data['success'], True)
       self.assertEqual(data['deleted'], 25)
       #self.assertTrue(data['total_question'])
       #self.assertEqual(question, None)

    def test_404_if_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
    def test_create_question(self):
        res = self.client().post('/questions',   json=self.new_question)
        data = json.loads(res.data)
        pass
    
    def test_422_if_question_creation_fails(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        pass

     def test_get_questions_by_categories(self):
        res = self.client().get('/categories/5/questions')
        data = json.loads(res.data)
        question= Question.query.filter(Question.category==5)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        self.assertTrue(data['total_question'])
        self.assertTrue(data['categories'])

    def test_404_if_questions_by_categories_does_not_exist(self):
        res = self.client().get('/categories/10/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found') 
    
   def test_search_questions(self):
        request_data= {'searchTeram':'HOW'}
        res = self.client().post('/search/questions',data=json.dumps(request_data),content_type='application/json')                      
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    def test_422_if_notfind_search_questions(self):
        request_data= {'searchTeram':'Where'}
        res = self.client().post('/search/questions',data=json.dumps(request_data),content_type='application/json')                      
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

     
    def test_quizzes(self):
        request_data= {'previous_questions': [1, 2],
            'quiz_category': {'id': 2, 'type': 'Art'}}
        res = self.client().post('/quizzes',data=json.dumps(request_data),content_type='application/json')                      
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)