import string
import random
from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        self.open_new_project_form()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def open_new_project_form(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("description")) > 0):
            wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("status", project.status)
        self.change_field_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name != "status" and field_name != "view_state":
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
            elif field_name == "status" or field_name == "view_state":
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            for row in wd.find_elements_by_class_name("row-1"):
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                if status != "":
                    view_state = cells[3].text
                    description = cells[4].text
                    self.project_cache.append(
                        Project(name=name, status=status, view_state=view_state, description=description))
            for row in wd.find_elements_by_class_name("row-2"):
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                if status != "":
                    view_state = cells[3].text
                    description = cells[4].text
                    self.project_cache.append(
                        Project(name=name, status=status, view_state=view_state, description=description))
        return list(self.project_cache)

    project_cache = None

    def del_project(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    @staticmethod
    def random_string():
        maxlen = 20
        symbols = string.ascii_letters + string.digits
        return "project_" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])