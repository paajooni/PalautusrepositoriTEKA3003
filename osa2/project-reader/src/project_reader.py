from urllib import request
import tomllib
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        data = tomllib.loads(content)
        print(data)

        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"].get("description", "")
        license = data["tool"]["poetry"].get("license", "")
        authors = data["tool"]["poetry"].get("authors", [])

        dependencies = list(data["tool"]["poetry"]["dependencies"].keys())
        dev_group = data.get("dependency-groups", {}).get("dev", [])
        dev_dependencies = []
        if isinstance(dev_group, list):
            for item in dev_group:
                dev_dependencies.append(item.split()[0])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)

        
