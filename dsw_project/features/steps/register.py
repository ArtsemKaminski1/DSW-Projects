# steps/user_registration_steps.py
from behave import *
import requests

registration_url = "https://reqres.in/api/register"

#  GIVEN
@step('The user is on the registration page')
def step_given(context):
    pass

# WHEN
@step('User submits registration details with email:{email} and password:{password}')
def step_when_registration(context, email, password):
    payload = {}
    if email:
        payload['email'] = email
    if password:
        payload['password'] = password

    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(registration_url, headers=headers, json=payload)

# THEN
@step('User should receive a status code {status_code}')
def step_then_status_code(context, status_code):
    assert context.response.status_code == int(status_code), f"Expected status code: {status_code}, but got: {context.response.status_code}"

@step('The response contains {expected_response}')
def step_then_response_contains(context, expected_response):
    assert expected_response in context.response.text, f"Expected response: {expected_response}. Response was: {context.response.json()['message']}"
