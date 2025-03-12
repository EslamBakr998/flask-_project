import flask
import pytest
from app_2 import app_1

def test_request():
    TestResonse =app_1.test_client().get('/')
    response_status_code= TestResonse.status_code
    response_data=TestResonse.data

    assert response_status_code==200,"response invalid "
    assert response_data==b'<h1 style = "color:blue">Hello world ! </h>' 

