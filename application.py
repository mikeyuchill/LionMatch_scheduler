from flask import Flask, Response, request
from flask_cors import CORS
import json
import utils.rest_utils as rest_utils
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from application_services.AvailabilityResource.availability_service import AvailabilityResource
from application_services.TimeSlotResource.time_slot_service import TimeSlotResource


application = Flask(__name__)
CORS(application)

@application.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@application.route('/availability', methods=['GET', 'POST'])
def all_availability():
    req = rest_utils.RESTContext(request)
    if req.method == "GET":
        res = AvailabilityResource.get_by_template({})
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    else:
        AvailabilityResource.create(req.data)
        rsp = Response("CREATED", status=201, content_type="text/plain")
    return rsp


@application.route('/timeSlot', methods=['GET', 'POST'])
def all_time_slot():
    req = rest_utils.RESTContext(request)
    if req.method == "GET":
        res = TimeSlotResource.get_by_template({})
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    else:
        TimeSlotResource.create(req.data)
        rsp = Response("CREATED", status=201, content_type="text/plain")
    return rsp


@application.route('/availability/<aid>', methods=['GET', 'PUT', 'DELETE'])
def availability_id(aid):
    req = rest_utils.RESTContext(request)
    if req.method == "GET":
        res = AvailabilityResource.get_by_template({"Id": aid})
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    elif req.method == "PUT":
        AvailabilityResource.update(req.data, aid)
        rsp = Response("UPDATED", status=200, content_type="text/plain")
    else:
        AvailabilityResource.delete_by_template({"Id": aid})
        rsp = Response("DELETED", status=200, content_type="text/plain")
    return rsp


@application.route('/timeSlot/<tid>', methods=['GET', 'PUT', 'DELETE'])
def time_slot_id(tid):
    req = rest_utils.RESTContext(request)
    if req.method == "GET":
        res = TimeSlotResource.get_by_template({"Id": tid})
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    elif req.method == "PUT":
        TimeSlotResource.update(req.data, tid)
        rsp = Response("UPDATED", status=200, content_type="text/plain")
    else:
        TimeSlotResource.delete_by_template({"Id": tid})
        rsp = Response("DELETED", status=200, content_type="text/plain")
    return rsp


if __name__ == '__main__':
    application.run()
