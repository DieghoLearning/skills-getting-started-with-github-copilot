import copy

import pytest
from fastapi.testclient import TestClient

import src.app


@pytest.fixture
def client():
    """Provide a FastAPI TestClient for the application."""
    # Arrange (shared): create an in-process client for endpoint tests
    return TestClient(src.app.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities state before and after each test."""
    # Arrange: snapshot mutable module-level state
    original_activities = copy.deepcopy(src.app.activities)
    src.app.activities.clear()
    src.app.activities.update(copy.deepcopy(original_activities))

    yield

    # Cleanup: restore original state so tests remain isolated
    src.app.activities.clear()
    src.app.activities.update(original_activities)
