import json

def test_register(test_client):
    print("Starting test_register")
    response = test_client.post('/auth/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 201
    assert response.json['message'] == 'User registered successfully'
    print("Finished test_register")

def test_login(test_client):
    print("Starting test_login")
    response = test_client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 200
    assert 'access_token' in response.json
    print("Finished test_login")