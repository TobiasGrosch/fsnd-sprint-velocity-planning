import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

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

        self.new_developer = {
            'name': 'Tobias',
            'proj_participation': 0.5,
            'id': 1
        }

        self.new_wrong_developer = {
            'name': 'Tobias',
            'proj_participation': 'wrong data type',
            'id': 2
        }

        self.new_sprint = {
            "name": "Sprint xy",
            "sp_planned": 127,
            "sp_finished": 99,
            "velocity_factor": 0.89,
            "sp_prediction_next_sprint": 105,
            "sprint_fte_sum": 90,
            "date_start": "2021-04-16",
            "date_end": "2021-05-06"
        }

        self.new_wrong_sprint = {
            "name": "Sprint xy",
            "sp_planned": "wrong data type",
            "sp_finished": 99,
            "velocity_factor": 0.89,
            "sp_prediction_next_sprint": 105,
            "sprint_fte_sum": 90,
            "date_start": "2021-04-16",
            "date_end": "2021-05-06"
        }

        self.developer_header = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1wSjduRi0xQXZsT3JSbjctT2FRNCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3Jvc2NodC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA2YzUwMjJjY2YwNDMwMDY5MjRlNzkwIiwiYXVkIjoic3ByaW50X3ZlbCIsImlhdCI6MTYxOTA5MjEzNywiZXhwIjoxNjE5MTc4NTM3LCJhenAiOiJIMFpUTThPOVhnNmZkVHUxV3U5T3BmMjlVemxMMkJmbCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRldmVsb3BlcnMiLCJnZXQ6c3ByaW50cyIsInBvc3Q6ZGV2ZWxvcGVycyJdfQ.DkrXbR02vfDdlDU0nOcHcgjU5qilbc-iD2JLX4Xy2DSh-QPmtz8sH0_vY-svKo_xEfWZdDmo1MvZuhrjADqqpyCuBih2sJGRA_ysSlf62aZNYxZMexnag0-nb1bvCeTo0ps9xKbL3sXg5r7Wa0Y7iwEyMZw3hG9_WJHlLEPAkCkC5Id-Z1e76V_aFXZ0RO8DKncaOblVTmB1xO0qqHzB75ePXA2sNhzM-cfr7_hVnphIIMkaiQveYlMCn0jzMUGuJYUcR7LeDqOIz9M7ir4K1MPS72cGwb1gvqRcPALDciN45x5AhkFqi3OelJxSwA_w589VbvFHF1oeDZoE1cSBYQ"
        self.scrum_master_header = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1wSjduRi0xQXZsT3JSbjctT2FRNCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZ3Jvc2NodC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA2NmM1MDkxODNhMmUwMDY5NGU2ZTBjIiwiYXVkIjoic3ByaW50X3ZlbCIsImlhdCI6MTYxOTA5MjA1NywiZXhwIjoxNjE5MTc4NDU3LCJhenAiOiJIMFpUTThPOVhnNmZkVHUxV3U5T3BmMjlVemxMMkJmbCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRldmVsb3BlcnMiLCJkZWxldGU6c3ByaW50cyIsImdldDpkZXZlbG9wZXJzIiwiZ2V0OnNwcmludHMiLCJwb3N0OmRldmVsb3BlcnMiLCJwb3N0OnNwcmludHMiXX0.ErtikB_8tlMZzEEjgdeNxaxbpk2zZGTSIrIkUdykbD8SqTftq_e46mkE_DjnssoN7F93JC0lregZZE1hQSbtwLKXNkqcYI7Qd9yAJOFRX2EYmlEhqMhSVOpVKRJCfmlXWHuSCIfrxCbZc_S9ojRmQ-n5DR26UvIje58n79gr4HrfT3-A_JNOVqftOUOP6tDjp0C6XxRAob8BhPzdZVePdqxah3fiCdTbcEK8N-R8cPYIOE-pwEe_Sk5K5gjQdplVfeHYh6uN_gKjOAEbqrPCSyPWWvkoxG9lKujqUIIJDsEBN0xlVZ_qPcxlTrJOOi565pYUZcL4nfuuPV3bt6EhEg"

    def tearDown(self):
        """Executed after reach test"""
        models = [Developer, Sprint]
        for model in models:
            model.objecs.all().delete()
        pass
    
    def test_get_landingpage(self):
        res = self.client().get('/abc', headers=developer_header)

        self.assertEqual(res.status_code, 200)

    def test_get_wrong_page(self):
        res = self.client().get('/abc')

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found, Client error')
        

    def test_get_developers(self):
        res = self.client().get('/developers')
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['developers'], None)

    def test_get_sprints(self):
        res = self.client().get('/sprints')
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['sprints'], None)

    def test_post_developers(self):
        res = self.client().post('/developers', json=self.new_question)
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['name'], 'Tobias')
        self.assertEqual(data['proj_participation'], 0.5)

    def test_post_developers_error(self):
        res = self.client().post('/developers', json=self.new_wrong_developer)
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request, Client Error')

    def test_post_sprints(self):
        res = self.client().post('/sprints', json=self.new_sprint)
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data["name"], "Sprint xy")
        self.assertEqual(data["sp_planned"], 127)
        self.assertEqual(data["sp_finished"], 99)
        self.assertEqual(data["velocity_factor"], 0.89)
        self.assertEqual(data["sp_prediction_next_sprint"], 105)
        self.assertEqual(data["sprint_fte_sum"], 90)
        self.assertEqual(data["date_start"], "2021-04-16")
        self.assertEqual(data["date_end"], "2021-05-06")

    def test_post_sprints_error(self):
        res = self.client().post('/sprints', json=self.new_wrong_sprint)
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request, Client Error')


    def test_patch_developers(self):
        res = self.client().patch('/developers/1', json={'name': "Tobias_changed", "proj_participation": 0.505})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['name'], 'Tobias_changed')
        self.assertEqual(data['proj_participation'], 0.505)

    def test_patch_wrongly_developer(self):
        res = self.client().patch('/developers/2', json={'name': "Tobias_changed", "proj_participation": 0.505})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found, Client error')


    def test_delete_developer(self):
        
        res = self.client().delete('/developer/1')
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)


    def test_404_delete_developer_above_limit(self):
        res = self.client().delete('/developer/2')
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found, Client error')

    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()