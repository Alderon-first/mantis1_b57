from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHepler:

    def __init__(self, app):
        self.app = app

    def get_project_list_soap(self):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            project_list = client.service.mc_projects_get_user_accessible(self.app.config["webadmin"]["username"],
                                                                          self.app.config["webadmin"]["password"])
            projects = []
            for project in project_list:
                projects.append(Project(id=project.id, name=project.name))
            return projects
        except WebFault:
            return None
