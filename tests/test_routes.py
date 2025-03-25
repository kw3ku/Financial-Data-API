import json

def test_add_financial_data(test_client):
    # First, log in to get the access token
    login_response = test_client.post('/auth/login', json={
        'username': 'testuser1',
        'password': 'testpassword'
    })
    access_token = login_response.json['access_token']
    print("Access token:", access_token)

    # Use the access token to add financial data
    print("Starting test_add_financial_data")
    response = test_client.post('/api/data', headers={
        'Authorization': f'Bearer {access_token}'
    }, json={
        'date': '2025-03-25',
        'currency': 'USD',
        'exchange_rate': 1.0,
        'stock_symbol': 'AAPL',
        'stock_price': 150.0
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 201
    assert response.json['message'] == 'Financial data added successfully'
    print("Finished test_add_financial_data")

def test_get_all_data(test_client):
    # First, log in to get the access token
    login_response = test_client.post('/auth/login', json={
        'username': 'testuser1',
        'password': 'testpassword'
    })
    access_token = login_response.json['access_token']
    print("Access token:", access_token)

    # Use the access token to get all financial data
    print("Starting test_get_all_data")
    response = test_client.get('/api/data', headers={
        'Authorization': f'Bearer {access_token}'
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 200
    assert isinstance(response.json, list)
    print("Finished test_get_all_data")