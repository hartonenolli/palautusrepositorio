from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")


        new_toml_string = toml.loads(content)

        name = new_toml_string["tool"]["poetry"]["name"]
        desc = new_toml_string["tool"]["poetry"]["description"]
        depend = new_toml_string["tool"]["poetry"]["dependencies"]
        dev_depend = new_toml_string["tool"]["poetry"]["dev-dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, depend, dev_depend)
