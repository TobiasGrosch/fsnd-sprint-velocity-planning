import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from random import random

from app import create_app
from models import setup_db, Developer, Sprint, Vacation


class SprintVelTestCase(unittest.TestCase):
    """This class represents the SprintVel test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "velocity_test"
        self.database_path = "postgresql://postgres:postgres@localhost:5432/{}".format(self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.random_number = str(random())

        self.new_developer = {
            'name': 'Tobias ' + self.random_number,
            'proj_participation': 0.5,
            'id': 1
        }

        self.new_wrong_developer = {
            'name': 'Tobias ' + self.random_number,
            'proj_participation': 'wrong data type',
            'id': 2
        }

        self.new_sprint = {
            "name": "Sprint " + self.random_number,
            "sp_planned": 127,
            "sp_finished": 99,
            "velocity_factor": 0.89,
            "sp_prediction_next_sprint": 105,
            "sprint_fte_sum": 90,
            "date_start": "2021-04-16",
            "date_end": "2021-05-06"
        }

        self.new_wrong_sprint = {
            "name": "Sprint " + self.random_number,
            "sp_planned": "wrong data type",
            "sp_finished": 99,
            "velocity_factor": 0.89,
            "sp_prediction_next_sprint": 105,
            "sprint_fte_sum": 90,
            "date_start": "2021-04-16",
            "date_end": "2021-05-06"
        }

        self.developer_header = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1wSjduRi0xQXZsT3JSbjctT2FRNCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3Jvc2NodC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA2YzUwMjJjY2YwNDMwMDY5MjRlNzkwIiwiYXVkIjoic3ByaW50X3ZlbCIsImlhdCI6MTYxOTI0ODQ5NCwiZXhwIjoxNjE5MzM0ODk0LCJhenAiOiJIMFpUTThPOVhnNmZkVHUxV3U5T3BmMjlVemxMMkJmbCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRldmVsb3BlcnMiLCJnZXQ6c3ByaW50cyIsInBvc3Q6ZGV2ZWxvcGVycyJdfQ.VavaiLBHJQBkP4xWhJfakkTKEgi8on4F2KMwYvrN17Nw5yCOG0b3odIu_npsWDwx-y_Vy4pQSkTHKQj5P21EBswvgDSnfg7kgrGqQ67hsWwfGk1rFaRJPYy_t3RUhje5rBiNULoUJgUihEh1t6NitrlDUIZFO0yzL7XXjZ5QIZXol6-zfHib3_nkj80cqk2Z3iZbMmGDXEw6XkjDPvp3Yqaf0fRdwAYTpFpg1xBrH79tC5lrkp_gt0wa7VnOGhImXdy3M00JLb_jJnh0Q9CYVASFqcAHgaVDiUS1PsTt86jtOliXWt1CaK5EKlpg7q8e8Br7DFjRsM4ALqJV2IRgNA"
        self.scrum_master_header = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1wSjduRi0xQXZsT3JSbjctT2FRNCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3Jvc2NodC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA2NmM1MDkxODNhMmUwMDY5NGU2ZTBjIiwiYXVkIjoic3ByaW50X3ZlbCIsImlhdCI6MTYxOTI0ODU5MSwiZXhwIjoxNjE5MzM0OTkxLCJhenAiOiJIMFpUTThPOVhnNmZkVHUxV3U5T3BmMjlVemxMMkJmbCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRldmVsb3BlcnMiLCJkZWxldGU6c3ByaW50cyIsImdldDpkZXZlbG9wZXJzIiwiZ2V0OnNwcmludHMiLCJwb3N0OmRldmVsb3BlcnMiLCJwb3N0OnNwcmludHMiXX0.BDCJtw729z9lUggunoa3iESr_FH3ssIldSHY90sLrqOqdV3AkORtiqM42JEaD2eUhPm29AyF4fFZsycD8KSyLoDYQwsrKazn6yl5n8ux76_S8RG2Ws__tMB8bTd3b1yxTFOzETRduMJZKZdhalMkDyfu2vNdEirmx8jzHvbouw2e6JTZZf6d0YqHzOVZs9BadlztlTkiqZt4yXmAz6rDN-DpI5GDX-9tzienjXGRNHfpN9rX2SJ60kAbdwEnBtAHjwFLneO2fg_mKuiJxfCQhzbAi7IEXA89N93KE-ZoE3pg5TZrEqGmjdfy-upMCZBx-dEc1-INWzz-aND2eGWrxA"

    
    def test_get_landingpage(self):
         res = self.client().get('/', headers={'Authorization': self.developer_header})

         self.assertEqual(res.status_code, 200)

    def test_get_wrong_page(self):
        res = self.client().get('/abc', headers={'Authorization': self.developer_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found, Client error')
        

    def test_get_developers(self):
        res = self.client().get('/developers', headers={'Authorization': self.developer_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_sprints(self):
        res = self.client().get('/sprints', headers={'Authorization': self.scrum_master_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_developers(self):
        res = self.client().post('/developers', json=self.new_developer, headers={'Authorization': self.scrum_master_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['name'])
        self.assertEqual(data['proj_participation'], 0.5)

    def test_post_developers_error(self):
        res = self.client().post('/developers', json=self.new_wrong_developer, headers={'Authorization': self.developer_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request, Client Error')

    def test_post_sprints(self):
        res = self.client().post('/sprints', json=self.new_sprint, headers={'Authorization': self.scrum_master_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["name"])
        self.assertEqual(data["sp_planned"], 127)
        self.assertEqual(data["sp_finished"], 99)
        self.assertEqual(data["velocity_factor"], 0.89)
        self.assertEqual(data["sp_prediction_next_sprint"], 105)
        self.assertEqual(data["sprint_fte_sum"], 90)
        self.assertEqual(data["date_start"], "2021-04-16")
        self.assertEqual(data["date_end"], "2021-05-06")

    def test_post_sprints_error(self):
        res = self.client().post('/sprints', json=self.new_wrong_sprint, headers={'Authorization': self.scrum_master_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request, Client Error')


    def test_patch_developers(self):
        res = self.client().patch('/developers/1', json={'name': "Tobias_changed", "proj_participation": 0.505}, headers={'Authorization': self.scrum_master_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['name'], 'Tobias_changed')
        self.assertEqual(data['proj_participation'], 0.505)

    def test_patch_wrongly_developer(self):
        res = self.client().patch('/developers/xy', json={'name': "Tobias_changed", "proj_participation": 0.505}, headers={'Authorization': self.scrum_master_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found, Client error')


    def test_delete_developer(self):
        selected = Developer.query.order_by(self.db.desc(Developer.id)).limit(1)
        selected_id = [id.json_representation() for id in selected]
        dict = selected_id[0]
        delete_id = dict['id'] 
        param = {'id': delete_id}
        
        res = self.client().delete('/developers/{id}'.format(**param), headers={'Authorization': self.scrum_master_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], delete_id)


    def test_404_delete_developer_above_limit(self):
        res = self.client().delete('/developer/10000', headers={'Authorization': self.scrum_master_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found, Client error')

    def test_wrong_role_posting_sprint(self):
        res = self.client().post('/sprints', json=self.new_sprint, headers={'Authorization': self.developer_header})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        
    def tearDown(self):
        """Executed after every test run"""
        #developer = Developer.query.all()
        #sprint = Sprint.query.all()
        #developer.delete()
        #sprint.delete()
        pass

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()