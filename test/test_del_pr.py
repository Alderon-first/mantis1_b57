import random
from model.project import Project


def test_del_project(app):
    if len(app.project.get_project_list()) == 0:
        project_test = Project(name=app.project.random_string(), description=app.project.random_string())
        app.project.add_project(project_test)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.del_project(project.name)
    old_projects.remove(project)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.name_sort) == sorted(new_projects, key=Project.name_sort)


def test_delete_first_project_soap(app):
    if len(app.soap.get_project_list_soap()) == 0:
        project_test = Project(name=app.project.random_string(), description=app.project.random_string())
        app.project.add_project(project_test)
    old_projects = app.soap.get_project_list_soap()
    project = random.choice(old_projects)
    app.project.del_project(project.name)
    old_projects.remove(project)
    new_projects = app.soap.old_projects_soap()
    assert sorted(old_projects, key=Project.name_sort) == sorted(new_projects, key=Project.name_sort)