import pytest
from unittest.mock import patch
from app.functions import replace_skills_with_json, replace_experience_with_json, parse_params, create_param_subs, \
    error_response
from app.models import User, SkillName


@pytest.fixture
def skill_name_objects_list():
    skill_name_objects_list = [SkillName(skill_name='skill1'),
                               SkillName(skill_name='skill7'),
                               SkillName(skill_name='skill3')]
    return skill_name_objects_list


@pytest.mark.parametrize('test_input', [{
    "firstname": "First Test",
    "lastname": "User",
    "skills": [
        {
            "skill_name": "skill1",
            "skill_level": 1
        },
        {
            "skill_name": "skill2",
            "skill_level": 2
        }
    ],
    "experience": [
        {
            "company": "Firma",
            "project": "Project",
            "duration": 5
        }
    ]
},
    {
        "firstname": "2nd Test",
        "lastname": "User",
        "dummy_key": "doesn't matter",
        "skills": [
            {
                "skill_name": "skill1",
                "skill_level": 1
            },
            {
                "skill_name": "skill7",
                "skill_level": 20
            },
            {
                "skill_name": "skill16",
                "skill_level": 30
            }
        ],
        "experience": []
    }
])
@patch('app.main.get_session')
def test_replace_skills_with_json_success(get_session_mock, db_credentials, skill_name_objects_list, test_input):
    new_cv = User()
    session = get_session_mock()
    expected_query_result = [obj for obj in skill_name_objects_list]
    session.query.return_value.filter.return_value.all.return_value = expected_query_result
    replace_skills_with_json(session, new_cv, test_input)
    assert new_cv.skills[0].object_as_dict() == test_input['skills'][0]
    assert new_cv.skills[-1].object_as_dict() == test_input['skills'][-1]
    assert len(new_cv.skills) == len(test_input['skills'])


@patch('app.session.get_session')
def test_replace_skills_with_json_empty(get_session_mock, db_credentials, test_input={
    "skills": []
}):
    cv = User()
    session = get_session_mock()
    expected_query_result = []
    session.query.return_value.filter.return_value.all.return_value = expected_query_result
    replace_skills_with_json(session, cv, test_input)
    assert cv.skills == []


@patch('app.session.get_session')
def test_replace_skills_with_json_wrong_key(get_session_mock, db_credentials, test_input={
    "skilsls": []
}):
    cv = User()
    session = get_session_mock()
    with pytest.raises(KeyError):
        replace_skills_with_json(session, cv, test_input)


@pytest.mark.parametrize('test_input', [{
    "firstname": "Second Test",
    "lastname": "User",
    "skills": [
        {
            "skill_name": "skill1",
            "skill_level": 1
        },
        {
            "skill_name": "skill2",
            "skill_level": 2
        }
    ],
    "experience": [
        {
            "company": "Firma",
            "project": "Project",
            "duration": 5
        }
    ]
},
    {
        "firstname": "3rd Test",
        "lastname": "User",
        "dummy_key": "doesn't matter",
        "skills": [],
        "experience": [
            {
                "company": "Firma",
                "project": "Project",
                "duration": 5
            },
            {
                "company": "Firma",
                "project": "Project2",
                "duration": 6
            },
            {
                "company": "Firma3",
                "project": "Project4",
                "duration": 7
            }
        ]
    }
])
def test_replace_experience_with_json_success(test_input):
    new_cv = User()
    replace_experience_with_json(new_cv, test_input)
    assert new_cv.experience[0].object_as_dict() == test_input['experience'][0]
    assert new_cv.experience[-1].object_as_dict() == test_input['experience'][-1]
    assert len(new_cv.experience) == len(test_input['experience'])


# TODO to miałem wyrzucic do tej powyzej, ale tu jest inny assert
@pytest.mark.parametrize('test_input', [
    {
        "firstname": "Test",
        "lastname": "1",
        "skills": [],
        "experience": []
    },
    {
        "firstname": "Test",
        "lastname": "1",
        "skills": [],
    },

    {
        "abc": "def"
    },
    {
    }
])
def test_replace_experience_with_json_empty(test_input):
    new_cv = User()
    replace_experience_with_json(new_cv, test_input)
    assert new_cv.experience == []


# TODO to miałem usunąć bo nie ma sensu, ale czy aby na pewno?
def test_replace_experience_with_json_wrong_key(test_input={
    "experience": [
        {
            "wrong_key": "hmm"
        }
    ]
}):
    new_cv = User()
    with pytest.raises(KeyError):
        replace_experience_with_json(new_cv, test_input)


@pytest.mark.parametrize('test_input, expected', [
    ([{'skill_name': 'skill1', 'skill_level': 1}, {'skill_name': 'skill2', 'skill_level': 2}],
     {'count': 2, 'param0': ('skill1', 1), 'param1': ('skill2', 2)}),
    ([{'skill_name': 'skill1', 'skill_level': 1}],
     {'count': 1, 'param0': ('skill1', 1)}),
    ([],
     {'count': 0})
])
def test_parse_params(test_input, expected):
    assert parse_params(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([{'skill_name': 'skill1', 'skill_level': 1}, {'skill_name': 'skill2', 'skill_level': 2}], ':param0, :param1'),
    ([{'skill_name': 'skill1', 'skill_level': 1}], ':param0'),
    ([], '')
])
def test_create_params_success(test_input, expected):
    assert create_param_subs(test_input) == expected


@pytest.mark.parametrize('message, code, error, expected', [
    ('msg', 666, KeyError, ({'error': 'msg'}, 666)),
    ('terrible error', 500, Exception, ({'error': 'terrible error'}, 500)),
    ('', None, None, ({'error': ''}, None)),
])
def test_error_response(message, code, error, expected):
    assert error_response(message, code, error) == expected
