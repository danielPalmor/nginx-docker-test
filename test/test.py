import requests
import os


# Define endpoints
HTML_SERVER_URL = "http://nginx_servers:8080"
ERROR_SERVER_URL = "http://nginx_servers:8081"

def test_html_server():
    # Get request from endpoint
    response = requests.get(HTML_SERVER_URL)

    # Define expected parameters
    expected_status_code, expected_content = 200, 'OK'

    assert response.status_code == expected_status_code, f'got: {response.ok}. expected: {expected_status_code}'
    assert expected_content in response.text, f'got: {response.text}. expected: {expected_content}'


def test_error_server():
    RESULTS_DIR = '/test-results'
    
    try:
        # Run Tests
        test_html_server()
        test_error_server()

        # Write to artifact that tests passed
        with open(os.path.join(RESULTS_DIR, 'succeeded'), 'w') as f:
            f.write("All tests passed")
        exit(0)

    except AssertionError as e:
        # Write to artifact that tests failed
        with open(os.path.join(RESULTS_DIR, 'fail'), 'w') as f:
            f.write(f"Tests failed: {e}")
        exit(1)