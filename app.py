import os
import sys
from flask import Flask, request, abort, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Developer, Sprint, Vacation
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={r"/api/*": {'origins': '*'}})
  app.secret_key = os.getenv('SECRET_KEY')

  @app.route('/', methods=['GET'])
  def index():
    return '<h1> Welcome to the Sprint Velocity Planning Tool SprintVel! </h1>', 200

  @app.route('/developers', methods=['GET'])
  @requires_auth('get:developers')
  def get_developers(jwt):
    developers = Developer.query.all()
    developers = [developer.json_representation() for developer in developers]
    return jsonify({
      'success': True,
      'developers': developers
    }), 200

  @app.route('/sprints', methods=['GET'])
  @requires_auth('get:sprints')
  def get_sprints(jwt):
    sprints = Sprint.query.all()
    sprints = [sprint.json_representation() for sprint in sprints]
    return jsonify({
      'success': True,
      'sprints': sprints
    }), 200

  @app.route('/developers', methods=['POST'])
  @requires_auth('post:developers')
  def post_developers(jwt):

    error = False
    body = request.get_json()
    #print(body)
    name = body.get('name')
    #print(name)
    proj_participation = body.get('proj_participation')
    #print(proj_participation)

    new_developer = Developer(name=name, proj_participation=proj_participation)

    try:
      new_developer.insert()
      #flash('New Developer ' + str(new_developer.name) + ' was successful listed!')
    except Exception as e:
      error = True
      print(e)
      #flash('An error occurred. New Developer ' + str(new_developer.name) + ' could not be listed.')
    if error:
      abort(400)
    else:
      return jsonify({
        'success': True,
        'name': name,
        'proj_participation': proj_participation
      }), 200

  @app.route('/sprints', methods=['POST'])
  @requires_auth('post:sprints')
  def post_sprints(jwt):

    error = False
    body = request.get_json()
    #print(body)
    name = body.get('name')
    sp_planned = body.get('sp_planned')
    sp_finished = body.get('sp_finished')
    velocity_factor = body.get('velocity_factor')
    sp_predicitions_next_sprint = body.get('sp_prediction_next_sprint')
    sprint_fte_sum = body.get('sprint_fte_sum')
    date_start = body.get('date_start')
    date_end = body.get('date_end')


    new_sprint = Sprint(name=name, sp_planned=sp_planned, sp_finished=sp_finished, 
    velocity_factor=velocity_factor, sp_predicitions_next_sprint=sp_predicitions_next_sprint,
    sprint_fte_sum=sprint_fte_sum, date_start=date_start, date_end=date_end)

    try:
      new_sprint.insert()
      #flash('New Sprint ' + str(new_sprint.name) + ' was successful listed!')
    except Exception as e:
      error = True
      print(e)
      #flash('An error occurred. New Sprint ' + str(new_sprint.name) + ' could not be listed.')
    if error:
      abort(400)
    else:
      return jsonify({
        'success': True,
        'name': name,
        'sp_planned': sp_planned,
        'sp_finished': sp_finished,
        'velocity_factor': velocity_factor,
        'sp_prediction_next_sprint': sp_predicitions_next_sprint,
        'sprint_fte_sum': sprint_fte_sum,
        'date_start': date_start,
        'date_end': date_end
      }), 200

  @app.route('/developers/<int:developer_id>', methods=['PATCH'])
  @requires_auth('post:developers')
  def patch_an_existing_developer(jwt, developer_id):
    body = request.get_json()
    name = body.get('name')
    proj_participation = body.get('proj_participation')

    try:
        developer = Developer.query.get(developer_id)
    except Exception as e:
        print(e)
        abort(404)

    try:
        if name == None:
            None
        else:
            developer.name = name
        if proj_participation == None:
            None
        else:
            developer.proj_participation = proj_participation
        developer.update()

    except Exception as e:
        print(e)
        print(422)

    return jsonify({
            "success": True,
            "name": name,
            "proj_participation": proj_participation
                    }), 200

  @app.route('/developers/<int:developer_id>', methods=['DELETE'])
  @requires_auth('delete:developers')
  def delete_developer(jwt, developer_id):
    error = False
    try:
      developer = Developer.query.get(developer_id)
      developer.delete()
    except Exception as e:
      error = True
      print(e)
    if error:
      abort(404)
    else:
      return jsonify({
        'success': True,
        'deleted': developer_id
        }), 200
    return None

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "bad request, Client Error"
    }), 400

  @app.errorhandler(401)
  def unauthorized_request(error):
    return jsonify({
      "success": False,
      "error": 401,
      "message": "unauthorized request, please check your permissions"
    }), 401

  @app.errorhandler(403)
  def request_forbidden(error):
    return jsonify({
      "success": False,
      "error": 403,
      "message": "request is forbidden"
    }), 403

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "resource not found, Client error"
    }), 404

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      "success": False,
      "error": 405,
      "message": "method not allowed"
    }), 405

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "request unprocessable"
    }), 422

  @app.errorhandler(AuthError)
  def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response





  return app

app = create_app()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)