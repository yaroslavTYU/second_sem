import pytest
from apps.tasks.models import Tasks


@pytest.mark.django_db
class TestTask:
    def test_create_task(self, api_client, task_data):
        response = api_client.post('/api/tasks/', task_data)

        assert response.data['title'] == task_data['title']
        assert response.data['description'] == task_data['description']
        assert response.data['is_done'] == task_data['is_done']
    def test_get_task_detail(self, api_client, existing_task):
        response = api_client.get(f'/api/tasks/{existing_task.id}/')
        
        assert response.data['id'] == existing_task.id
        assert response.data['title'] == existing_task.title

    def test_update_task(self, api_client, existing_task):
        update_data = {
            'title': 'Updated Title',
            'description': 'Updated Description',
            'is_done': True
        }

        response = api_client.put(f'/api/tasks/{existing_task.id}/', update_data)
        assert response.data['title'] == 'Updated Title'
        assert response.data['is_done'] is True

        updated_task = Tasks.objects.get(id=existing_task.id)
        assert updated_task.title == 'Updated Title'

    def test_delete(self, api_client, existing_task):
        response = api_client.delete(f'/api/tasks/{existing_task.id}/')

        assert response.status_code == 204
    
    def test_get_none_task(self, api_client):
        response = api_client.get('/api/tasks/99999/')
        
        assert response.status_code == 404
    
    def test_get_all_tasks(self, api_client):
        Tasks.objects.create(title='Task 1', description='Desc 1')
        Tasks.objects.create(title='Task 2', description='Desc 2')
        
        response = api_client.get('/api/tasks/')
        
        assert response.status_code == 200
        assert len(response.data) == 2
    
    def test_check_title(self, api_client,existing_task):
        assert str(existing_task) == existing_task.title #для 100%  покрытия models
