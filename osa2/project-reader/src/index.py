from project_reader import ProjectReader


def main():
    url = "https://raw.githubusercontent.com/paajooni/PalautusrepositoriTEKA3003/main/osa2/project-reader/pyproject.toml"
    reader = ProjectReader(url)
    project = reader.get_project()
    print(project)


if __name__ == "__main__":
    main()
