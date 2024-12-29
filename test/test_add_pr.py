from model.project import Project


def test_add_project(app):
    old_projects = app.project.get_project_list()
    project_test = Project(name=app.project.random_string(), description=app.project.random_string())
    app.project.add_project(project_test)
    old_projects.append(project_test)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.name_sort) == sorted(new_projects, key=Project.name_sort)


def test_add_project_soap(app):
    old_projects = app.soap.get_project_list_soap()
    project_test = Project(name=app.project.random_string(), description=app.project.random_string())
    app.project.add_project(project_test)
    new_projects = app.soap.get_project_list_soap()
    old_projects.append(project_test)
    assert sorted(old_projects, key=Project.name_sort) == sorted(new_projects, key=Project.name_sort)