from behave import *
import requests
import json

base_url = "https://reqres.in/api/login"

# GIVEN
@given('The user is on the login page')
def step_given(context):
    pass

# Krok WHEN
@when('User submits login credentials with email:{email} and password:{password}')
def step_when(context, email, password):
    payload = json.dumps({
        "email": email,
        "password": password
    })
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(base_url, headers=headers, data=payload)

# Krok THEN
@then('User should receive a status code {status_code}')
def step_then_status_code(context, status_code):
    assert context.response.status_code == int(status_code), f"Expected status code: 200, but got: {status_code}"

# Krok THEN
@then('The response contains {expected_response}')
def step_then_response_contains(context, expected_response):
    assert expected_response in context.response.text, f"Expected response: {expected_response}, but response was: {context.response.text}"
