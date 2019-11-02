# generic-flask-skeleton

This Flask skeleton is set up in the particular way that my team and I like so that we can get moving quickly on projects.

This skeleton includes some utilites for both GitHub and GitLab. Repository specific files should be removed as necessary.


# Pre-Commit

This project uses pre-commit hooks to ensure consistent code style throughout the repo. We use
[black](https://github.com/ambv/black) for Python files and Python code within documentation. We use
[prettier](https://github.com/prettier/prettier) for all other filetypes.

Make sure you've installed all the packages listed in both `requirements.txt`.
This will install pre-commit for you. Then run `pre-commit install` to set up the local pre-commit environment.

Pre-commit will run each time you attempt to commit staged changes. You can run the pre-commit checks at any time
using `pre-commit run`.

Running Tests
-------------

To run the test suite, make sure you've installed the packages listed in `requirements.txt`. Then run `pytest --cov=application_name`

Pull requests that cause the repository's overall test coverage to drop below X% or cause a decrease in coverage of %Y
or more will be rejected. Please make sure to update tests in accordance with your changes.
