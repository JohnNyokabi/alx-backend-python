# 0x03. Unittests and Integration Tests

## Requirements
    * Ubuntu
    * Python3
    * Pycodestyle
    * vim/vi/emacs

## Tasks
    | Task | Details |
    | ---- | ------- |
    | [ 0. Parameterize a unit test ] | Implements the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to |
    | [ 1. Parameterize a unit test ] | Implements `TestAccessNestedMap.test_access_nested_map_exception` and uses the `assertRaises` context manager to test that a KeyError is raised for the following inputs |
    | [ 2. Mock HTTP calls ] | Defines the `TestGetJson(unittest.TestCase)` class and implement the `TestGetJson.test_get_json` method to test that `utils.get_json` returns the expected result |
    | [ 3. Parameterize and patch ] | Implements the `TestMemoize(unittest.TestCase)` class with a `test_memoize` method. |
    | [ 4. Parameterize and patch as decorators ] | Declares the `TestGithubOrgClient(unittest.TestCase)`class and implement the `test_org` method which tests if `GithubOrgClient.org` returns the correct value |
    | [ 5. Mocking a property ] | Implements the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url |`
    | [ 6. More patching ] | Uses patch as a context manager to mock `GithubOrgClient._public_repos_url` and return a value of choice |
    | [ 7. Parameterize ] | Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license` |
    | [ 8. Integration test: fixtures ] | Create the `TestIntegrationGithubOrgClient(unittest.TestCase)` class and implement the `setUpClass` and `tearDownClass` which are part of the `unittest.TestCase` API |
    | [ 9. Integration tests ] | Implement `test_public_repos_with_license` to test the `public_repos` with the argument `license="apache-2.0"` and make sure the result matches the expected value from the fixtures |
