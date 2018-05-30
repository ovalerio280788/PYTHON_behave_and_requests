# content of test_class.py
import unittest

import requests

from requests_example.base import BaseAPI


class TestClass(BaseAPI):

    def test_one(self):
        r = requests.get("{}/orgs/octokit/repos".format(self.base_url))
        assert r.status_code == 200
        assert len(r.json()) > 0

    def test_two(self):
        r = requests.get("{}/user".format(self.base_url))
        assert r.status_code == 401
        assert r.json()['message'] == 'Requires authentication'

    def test_three(self):
        r = requests.get("{}/repos/octokit/octokit.rb".format(self.base_url))
        assert r.status_code == 200
        assert r.json()['description'] == 'Ruby toolkit for the GitHub API'
        assert r.json()['private'] is False


if __name__ == '__main__':
    unittest.main()
