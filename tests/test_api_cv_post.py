from unittest.mock import patch

import pytest
from app.models import User, SkillUser, SkillName, Experience


@pytest.fixture
def api_cv_post(db_credentials):
    from app.main import api_cv_post
    return api_cv_post


# @pytest.mark.parametrize()
@patch('app.main.get_session')
@patch('app.main.request')
@patch('app.main.User')
@patch('app.main.replace_skills_with_json')
@patch('app.main.replace_experience_with_json')
def test_exception_when_no_json(replace_experience_with_json_mock, replace_skills_with_json_mock,
                                request_mock, user_mock, get_session_mock, api_cv_post):
    request_mock.get_json.return_value = {'firstname': 'sdfsf', 'lastname': 'dsds'}
    actual = api_cv_post()
    expected = ({'success': 'item added'}, 201)
    assert actual == expected


@pytest.mark.skip('WIP')
def test_exception_when_no_key():
    with pytest.raises(KeyError):
        new_cv = User()
        json_data = {'a': 1}
        new_cv.firstname = json_data['firstname']
        pass


@pytest.mark.skip('WIP')
def test_exception_when_wrong_json():
    # raises AttributeError?
    pass


@pytest.mark.skip('WIP')
def test_exception_when_TypeError___():
    # hmm
    pass


@pytest.mark.skip('WIP')
def test_exception_when_db_error():
    # raises DataError
    pass


@pytest.mark.skip('WIP')
def test_cv_added_on_success():
    # assert {'success': 'item added'}, 201
    pass
