import requests
import pytest


@pytest.mark.list_users
def test_list_users():
    res = requests.get(url="https://reqres.in/api/users", params={"page": 2}, verify=False)
    assert res.status_code == 200, f"Expected Status code: 200, Actual Status code: {res.status_code}"
    assert res.json()['page'] == 2, f"Expected Page No.: 2, Actual Page No.: {res.json()['page']}"


@pytest.mark.single_user
def test_single_user():
    res = requests.get(url="https://reqres.in/api/users/2", verify=False)
    assert res.status_code == 200, f"Expected Status code: 200, Actual Status code: {res.status_code}"
    assert res.json()['data']['id'] == 2, f"Expected id: 2, Actual id: {res.json()['page']}"


@pytest.mark.create_user
def test_create_user():
    res = requests.post(url="https://reqres.in/api/users", data={"name": "morpheus", "job": "leader"}, verify=False)
    assert res.status_code == 201, f"Expected Status code: 201, Actual Status code: {res.status_code}"
    assert res.json()['id'] is not None, f"ID should be mentioned"


@pytest.mark.update_user
def test_update_user():
    res = requests.put(url="https://reqres.in/api/users/2", data={"name": "morpheus", "job": "zion resident"},
                       verify=False)
    assert res.status_code == 200, f"Expected Status code: 200, Actual Status code: {res.status_code}"


@pytest.mark.delete_user
def test_delete_user():
    res = requests.delete(url="https://reqres.in/api/users/2", verify=False)
    assert res.status_code == 204, f"Expected Status code: 204, Actual Status code: {res.status_code}"
