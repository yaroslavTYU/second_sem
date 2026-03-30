import pytest
from rest_framework.test import APIClient
from apps.tasks.models import Tasks  

@pytest.fixture
def api_client():

    return APIClient()


@pytest.fixture
def task_data():

    return {
        'title': 'Test Task',
        'description': 'Test Description',
        'is_done': False
    }


@pytest.fixture
def existing_task(db):

    return Tasks.objects.create(
        title='Existing Task',
        description='Existing Description',
        is_done=False
    )