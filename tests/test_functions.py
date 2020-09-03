import pytest
from app.functions import replace_skills_with_json, replace_experience_with_json, parse_params, create_param_subs, \
    error_response
from app.models import User


@pytest.mark.skip('WIP')
def test_replace_skills_with_json(mock_json_data_correct):
    pass


def test_replace_experience_with_json_success(mock_json_data_correct):
    new_cv = User()
    replace_experience_with_json(new_cv, mock_json_data_correct)
    assert new_cv.experience[0].object_as_dict() == mock_json_data_correct['experience'][0]


def test_replace_experience_with_json_empty(mock_json_data_no_exp):
    new_cv = User()
    replace_experience_with_json(new_cv, mock_json_data_no_exp)
    assert new_cv.experience == []


def test_replace_experience_with_json_wrong_key(mock_json_data_incorrect_exp):
    new_cv = User()
    with pytest.raises(KeyError):
        replace_experience_with_json(new_cv, mock_json_data_incorrect_exp)


@pytest.mark.skip('WIP')
def test_parse_params():
    pass


@pytest.mark.parametrize('test_input, expected', [
    ([{'skill_name': 'skill1', 'skill_level': 1}, {'skill_name': 'skill2', 'skill_level': 2}], ':param0, :param1'),
    ([{'skill_name': 'skill1', 'skill_level': 1}], ':param0'),
    ([], '')
])
def test_create_params_success(test_input, expected):
    assert create_param_subs(test_input) == expected


def test_create_params_raises_error():  # ten test niczego szczegolnego nie testuje, ale chcialem zmusic ta funkcje do rzucenia bledu
    with pytest.raises(TypeError):
        create_param_subs(User())


@pytest.mark.skip('WIP')
def test_error_response():
    pass
