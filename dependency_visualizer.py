import json
import os
from git import Repo
import graphviz


def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)


def get_commit_dependencies(repo, branch_name):
    commits = list(repo.iter_commits(branch_name))
    graph = {}

    for commit in commits:
        graph[commit.hexsha] = [parent.hexsha for parent in commit.parents]

    return graph


def create_graph(graph):
    dot = graphviz.Digraph(format='png')

    for commit, parents in graph.items():
        dot.node(commit)
        for parent in parents:
            dot.edge(parent, commit)

    return dot


def save_graph(dot, output_path):
    dot.render(output_path, cleanup=True)
    print(f"Граф зависимостей успешно сохранен в {output_path}")


def main(config_path):
    config = load_config(config_path)

    repo_path = config['repo_path']
    branch_name = config['branch_name']
    output_image_path = config['output_image_path']

    if not os.path.exists(repo_path):
        print(f"Репозиторий не найден по пути: {repo_path}")
        return

    repo = Repo(repo_path)

    graph = get_commit_dependencies(repo, branch_name)
    dot = create_graph(graph)
    save_graph(dot, output_image_path)


if __name__ == "__main__":
    main('config.json')