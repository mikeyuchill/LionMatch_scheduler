from flask import Flask, Response, request
import database_services.RDBService as d_service
from flask_cors import CORS
import json
import utils.rest_utils as rest_utils
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from application_services.imdb_artists_resource import IMDBArtistResource
from application_services.UsersResource.user_service import UserResource


application = Flask(__name__)
CORS(application)

@application.route('/')
def hello_world():
    return '<u>Hello World!</u>'


# @application.route('/imdb/artists/<prefix>')
# def get_artists_by_prefix(prefix):
#     res = IMDBArtistResource.get_by_name_prefix(prefix)
#     rsp = Response(json.dumps(res), status=200, content_type="application/json")
#     return rsp


@application.route('/<resource>', methods=['GET', 'POST'])
def get_users(resource):
    input = rest_utils.RESTContext(request, resource)
    if input.method == "GET":
        res = UserResource.get_by_template({})
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    else:
        res = UserResource.create(input.data)
        #headers = [{"Location", "/schedule/" + str(res)}]
        #rsp = Response("CREATED", status=201, headers=headers, content_type="text/plain")
        rsp = Response("CREATED", status=201, content_type="text/plain")
    return rsp

# @application.route('/timeSlot/<id>')
# def get_artists_by_prefix(prefix):
#     res = IMDBArtistResource.get_by_name_prefix(prefix)
#     rsp = Response(json.dumps(res), status=200, content_type="application/json")
#     return rsp


# #@application.route('/Project/users/first_name/<prefix>')
# @application.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
# def get_by_prefix(db_schema, table_name, column_name, prefix):
#     res = d_service.get_by_prefix(db_schema, table_name, column_name, prefix)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp


if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=5000)
    application.run()
