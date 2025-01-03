import unittest
from unittest.mock import MagicMock, patch
import json
import os
from dependency_visualizer import load_config, get_commit_dependencies, create_graph, save_graph  # замените 'your_module' на название вашего файла


class TestDependencyVisualizer(unittest.TestCase):

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='{"graphviz_path": "D:/Programs/Graphviz-12.2.1-win64/bin/dot.exe", "repo_path": "D:/wtf_is_this/graph/Blitznote", "output_image_path": "D:/wtf_is_this/graph/graphdependencies_graph.png", "branch_name": "main"}')
    def test_load_config(self, mock_open):
        config = load_config('dummy_path')
        self.assertEqual(config['graphviz_path'], 'D:/Programs/Graphviz-12.2.1-win64/bin/dot.exe')
        self.assertEqual(config['repo_path'], 'D:/wtf_is_this/graph/Blitznote')
        self.assertEqual(config['output_image_path'], 'D:/wtf_is_this/graph/graphdependencies_graph.png')
        self.assertEqual(config['branch_name'], 'main')

    @patch('git.Repo')
    def test_get_commit_dependencies(self, mock_repo_class):
        mock_repo_instance = mock_repo_class.return_value
        mock_commit_1 = MagicMock()
        mock_commit_1.hexsha = 'abc123'
        mock_commit_1.parents = []
        mock_commit_2 = MagicMock()
        mock_commit_2.hexsha = 'def456'
        mock_commit_2.parents = [mock_commit_1]
        mock_repo_instance.iter_commits.return_value = [mock_commit_1, mock_commit_2]
        dependencies = get_commit_dependencies(mock_repo_instance, 'main')
        expected_dependencies = {
            'abc123': [],
            'def456': ['abc123']
        }
        self.assertEqual(dependencies, expected_dependencies)

    def test_create_graph(self):
        graph = {
            'abc123': [],
            'def456': ['abc123']
        }
        dot = create_graph(graph)
        normalized_body = [entry.strip() for entry in dot.body]
        self.assertIn('abc123', normalized_body)
        self.assertIn('def456', normalized_body)
        self.assertIn('abc123 -> def456', normalized_body)

    @patch('graphviz.Digraph')
    def test_save_graph(self, mock_digraph):
        mock_dot = MagicMock()
        mock_digraph.return_value = mock_dot

        output_path = 'D:/wtf_is_this/graph/graphdependencies_graph.png.png'
        save_graph(mock_dot, output_path)

        mock_dot.render.assert_called_once_with(output_path, cleanup=True)


if __name__ == '__main__':
    unittest.main()
