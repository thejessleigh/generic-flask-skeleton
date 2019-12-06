# generic-flask-skeleton

This Flask skeleton is set up in the particular way that my team and I like so that we can get moving quickly on projects.

This skeleton includes some utilites for both GitHub and GitLab. Repository specific files should be removed as necessary.

[Poetry](https://poetry.eustace.io) is used to manage dependencies and the virtual environment. 
Please note that `poetry shell` [does not work correctly](https://github.com/sdispater/poetry/issues/571).

# Pre-Commit

This project uses pre-commit hooks to ensure consistent code style throughout the repo. We use
[black](https://github.com/ambv/black) for Python files and Python code within documentation. We use
[prettier](https://github.com/prettier/prettier) for all other filetypes.

Make sure you've installed all the packages listed in `requirements.txt`.
This will install pre-commit for you. Then run `pre-commit install` to set up the local pre-commit environment.

Pre-commit will run each time you attempt to commit staged changes. You can run the pre-commit checks at any time
using `pre-commit run`.

# Running Tests

To run the test suite, make sure you've run `poetry install --dev` and activated your virtual environment. Then run `pytest --cov=application_name`

Pull requests that cause the repository's overall test coverage to drop below X% or cause a decrease in coverage of %Y
or more will be rejected. Please make sure to update tests in accordance with your changes.

# Configuring the Application

The application expects environment variables to be available in order to run.

To facilitate local development we use `python-dotenv` to load environment variables from a `.env` file in the project. To get started, create a `.env` file from the template.

```
cp .env.sample .env`
```

Adjust the SQLALCHEMY\_DATABASE\_URI to point to an actual running postgres instance.

# Running the Application

To run the application locally, use the `run.py` script:

```
python run.py
```

Use the status check endpoint located at `localhost:5000/status` in order to check the status of the database connection.

# Adding Resources: Models, Views, Routes, and Blueprints

All models should extend `application_name.database.BaseModel`. Models, views, and Blueprints should all be added to the respective resource module in the `application_name/` directory.

New Blueprints will need to be registered in `application_name.app`:

```
from application_name.resource_name.views import new_blueprint

app.register_blueprint(new_blueprint)
```

See `application_name/resource_name/` for an example.

# Database Migrations

Flask-Migrate is used to manage database migrations. An initial migration with the example models is available in `migrations/versions/`

In order to run the migration, you'll first need to configure the application to connect to your database. Next, run the following command to create the table:

```
flask db upgrade
```

In your own project, after adding a new model or updating the columns, you can create the migration and apply it with following commands:

```
flask db migrate -m "second migration"
flask db upgrade
```
