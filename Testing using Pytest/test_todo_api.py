"""Integration tests for TODO API endpoints.

This module contains end-to-end tests for a REST API that manages TODO tasks.
Tests verify CRUD operations (Create, Read, Update, Delete) and list functionality.

API Endpoint: https://todo.pixegami.io
"""

import requests
import uuid

# Base URL for the TODO API
ENDPOINT = "https://todo.pixegami.io"

# ========== TEST FUNCTIONS ==========

def test_can_call_endpoint():
    """Test that the API endpoint is reachable and responds.
    
    Verifies basic connectivity to the API server.
    """
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():
    """Test creating a new task and verifying its content.
    
    Workflow:
    1. Create a new task with random test data
    2. Verify creation was successful (200 status)
    3. Retrieve the created task by its ID
    4. Verify retrieved task matches the created task data
    """
    # Generate unique test data for this task
    payload = new_task_payload()
    create_task_response = create_task(payload=payload)
    assert create_task_response.status_code == 200

    # Extract task ID from creation response
    data = create_task_response.json()
    task_id = data["task"]["task_id"]
    
    # Verify we can retrieve the task
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    
    # Verify task data matches what we created
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_can_update_task():
    """Test updating an existing task's content and completion status.
    
    Workflow:
    1. Create a new task
    2. Update the task with new content and mark as done
    3. Verify the update was successful
    4. Retrieve the task and verify changes were persisted
    """
    # Create initial task
    payload = new_task_payload()
    create_task_response = create_task(payload=payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # Prepare updated task data
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True
    }
    
    # Update the task
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    # Verify updates were persisted
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]

def test_can_list_tasks():
    """Test retrieving all tasks for a specific user.
    
    Workflow:
    1. Create multiple tasks (3) for the same user
    2. Retrieve the user's task list
    3. Verify the correct number of tasks are returned
    """
    n = 3  # Number of tasks to create
    payload = new_task_payload()
    
    # Create n tasks for the same user
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # Retrieve all tasks for this user
    user_id = payload["user_id"]
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()

    # Verify correct number of tasks returned
    tasks = data["tasks"]
    assert len(tasks) == n


def test_can_delete_task():
    """Test deleting a task and verifying it no longer exists.
    
    Workflow:
    1. Create a new task
    2. Delete the task
    3. Verify deletion was successful
    4. Attempt to retrieve the deleted task
    5. Verify task no longer exists (404 status)
    """
    # Create task to be deleted
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # Delete the task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # Verify task no longer exists
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404

# ========== HELPER FUNCTIONS ==========
# These functions encapsulate API calls to keep tests clean and maintainable

def create_task(payload):
    """Create a new task via API.
    
    Args:
        payload (dict): Task data containing content, user_id, and is_done.
        
    Returns:
        requests.Response: API response object.
    """
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
    """Update an existing task via API.
    
    Args:
        payload (dict): Updated task data including task_id.
        
    Returns:
        requests.Response: API response object.
    """
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
    """Retrieve a specific task by ID.
    
    Args:
        task_id (str): Unique identifier of the task.
        
    Returns:
        requests.Response: API response object containing task data.
    """
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def list_tasks(user_id):
    """Retrieve all tasks for a specific user.
    
    Args:
        user_id (str): Unique identifier of the user.
        
    Returns:
        requests.Response: API response object containing list of tasks.
    """
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def delete_task(task_id):
    """Delete a specific task by ID.
    
    Args:
        task_id (str): Unique identifier of the task to delete.
        
    Returns:
        requests.Response: API response object.
    """
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def new_task_payload():
    """Generate a unique task payload for testing.
    
    Creates test data with unique user_id and content using UUIDs
    to avoid conflicts between test runs.
    
    Returns:
        dict: Task payload with content, user_id, and is_done fields.
    """
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False
    }
