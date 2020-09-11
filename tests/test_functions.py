import pytest
from unittest.mock import patch
from app.functions import replace_skills_with_json, replace_experience_with_json, parse_params, create_param_subs, \
    error_response
from app.models import User, SkillName


@pytest.mark.parametrize('test_input, skill_name_objects_list, expected', [
(
    {
    'skills': []
    },
    [],
    []
),
(
    {
    'firstname': 'Test 2',
    'lastname': 'User',
    'skills': [
        {
        'skill_name': 'skill1',
        'skill_level': 1
        }
    ],
    'experience': [
        {
        'company': 'Firma',
        'project': 'Project',
        'duration': 5
        }
    ]
    },
    [SkillName(skill_name='skill1')],
    [{'skill_name': 'skill1', 'skill_level': 1}]
),
(
    {
    'firstname': 'Test 3',
    'lastname': 'User',
    'skills': [
        {
        'skill_name': 'skill1',
        'skill_level': 1
        },
        {
        'skill_name': 'skill2',
        'skill_level': 2
        }],
    'experience': [
        {
        'company': 'Firma',
        'project': 'Project',
        'duration': 5
        }]
    },
    [SkillName(skill_name='skill1'), SkillName(skill_name='skill7'), SkillName(skill_name='skill3')],
    [{'skill_name': 'skill1', 'skill_level': 1}, {'skill_name': 'skill2', 'skill_level': 2}]
),
(
    {
    'firstname': '4th Test',
    'lastname': 'User',
    'dummy_key': 'doesnt matter',
    'skills': [
        {
        'skill_name': 'skill1',
        'skill_level': 1
        },
        {
        'skill_name': 'skill7',
        'skill_level': 20
        },
        {
        'skill_name': 'skill16',
        'skill_level': 30
        }
    ],
    'experience': []
    },
    [SkillName(skill_name='skill1'),
     SkillName(skill_name='skill7'),
     SkillName(skill_name='skill16')],
    [{'skill_name': 'skill1', 'skill_level': 1},
     {'skill_name': 'skill7', 'skill_level': 20},
     {'skill_name': 'skill16', 'skill_level': 30}]
)
])
@patch('app.main.get_session')
def test_replace_skills_with_json(get_session_mock, db_credentials, skill_name_objects_list, expected,
                                          test_input):
    new_cv = User()
    session = get_session_mock()
    session.query.return_value.filter.return_value.all.return_value = skill_name_objects_list
    replace_skills_with_json(session, new_cv, test_input)
    assert [skill.object_as_dict() for skill in new_cv.skills] == expected


@pytest.mark.parametrize('test_input, expected', [
(
    {
    'abc': 'def'
    },
    []
),
(
    {
    'experience': []
    },
    []
),
(
    {
    'firstname': 'Test 2',
    'lastname': 'User',
    'skills': [
        {
        'skill_name': 'skill1',
        'skill_level': 1
        }],
    'experience': [
        {
        'company': 'Firma',
        'project': 'Project',
        'duration': 5
        }]
    },
    [{'company': 'Firma', 'project': 'Project', 'duration': 5}]
),
(
    {
    'firstname': 'Third Test',
    'lastname': 'User',
    'skills': [
        {
        'skill_name': 'skill1',
        'skill_level': 1
        },
        {
        'skill_name': 'skill2',
        'skill_level': 2
        }],
    'experience': [
        {
        'company': 'Firma',
        'project': 'Project',
        'duration': 5
        },
        {
        'company': 'Firma2',
        'project': 'Project2',
        'duration': 50
        }]
    },
    [{'company': 'Firma', 'project': 'Project', 'duration': 5},
     {'company':'Firma2', 'project': 'Project2', 'duration': 50}]
),
(
    {
    'firstname': '3rd Test',
    'lastname': 'User',
    'dummy_key': 'doesnt matter',
    'skills': [],
    'experience': [
        {
        'company': 'Firma',
        'project': 'Project',
        'duration': 5
        },
        {
        'company': 'Firma',
        'project': 'Project2',
        'duration': 6
        },
        {
        'company': 'Firma3',
        'project': 'Project4',
        'duration': 7
        }]
    },
    [{'company': 'Firma', 'project': 'Project', 'duration': 5},
     {'company': 'Firma', 'project': 'Project2', 'duration': 6},
     {'company': 'Firma3', 'project': 'Project4', 'duration': 7}]
)
])
def test_replace_experience_with_json(test_input, expected):
    new_cv = User()
    replace_experience_with_json(new_cv, test_input)
    assert [exp.object_as_dict() for exp in new_cv.experience] == expected


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
def test_create_params(test_input, expected):
    assert create_param_subs(test_input) == expected


@pytest.mark.parametrize('message, code, error, expected', [
    ('msg', 666, KeyError, ({'error': 'msg'}, 666)),
    ('terrible error', 500, Exception, ({'error': 'terrible error'}, 500)),
    ('', None, None, ({'error': ''}, None)),
])
def test_error_response(message, code, error, expected):
    assert error_response(message, code, error) == expected
