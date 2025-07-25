#!/usr/bin/env python3
""" Unitest Module
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test GithubOrgClient.org.
    """
    @parameterized.expand([
        ("google", {"google", True}),
        ("abc", {"abc", True})])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """ Test the GithubOrgClient.org method for correct API call.
        """
        get_patch.return_value = expected
        gh_client = GithubOrgClient(org)
        self.assertEqual(gh_client.org, expected)
        get_patch.assert_called_once_with(f'https://api.github.com/orgs/{org}')

    def test_public_repos_url(self):
        """ Test that the _public_repos_url property returns the expected URL.
        """
        expected_url = 'https://api.github.com/orgs/google/repos'
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value={'repos_url': expected_url})):
            gh_client = GithubOrgClient("google")
            self.assertEqual(gh_client._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """ Test the public_repos property of GithubOrgClient class.
        """

        mock_repos_url = 'https://api.github.com/orgs/google/repos'

        expected_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
        ]

        mocked_get_json.return_value = expected_repos_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public_repos_url:
            mocked_public_repos_url.return_value = mock_repos_url

            gh_client = GithubOrgClient("google")

            self.assertEqual(gh_client.public_repos(), ["repo1", "repo2"])

            mocked_get_json.assert_called_once_with(mock_repos_url)

            mocked_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the GithubOrgClient.has_license method."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient.public_repos method.
    """

    @classmethod
    def setUpClass(cls):
        """Initial setup for the integration tests.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_response_org = Mock()
        cls.mock_response_repos = Mock()

        cls.mock_response_org.json.return_value = cls.org_payload
        cls.mock_response_repos.json.return_value = cls.repos_payload

        cls.mock_get.side_effect = [
            cls.mock_response_org,
            cls.mock_response_repos,
        ]

    @classmethod
    def tearDownClass(cls):
        """Cleans up the patch after the tests.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests retrieval of public repositories.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Tests filtering of repositories by license.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
