import pytest

from backend import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    return app


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()


@pytest.fixture(scope="function")
def app_context(app):
    with app.app_context():
        yield
