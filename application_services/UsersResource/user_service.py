from application_services.BaseApplicationResource import BaseApplicationResource
from database_services.RDBService import RDBService as RDBService

class UserResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_by_template(cls, template):
        res = RDBService.find_by_template("schedule", "timeSlot", template, None)
        return res

    @classmethod
    def create(cls, resource):
        # id = RDBService.get_max_id("schedule", "timeSlot")
        # resource["Id"] = id
        res = RDBService.create("schedule", "timeSlot", resource)
        return res