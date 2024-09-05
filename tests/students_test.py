from core.models.assignments import Assignment,AssignmentStateEnum
def test_get_assignments_student_1(client, h_student_1):
    response = client.get(
        '/student/assignments',
        headers=h_student_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 1


def test_get_assignments_student_2(client, h_student_2):
    response = client.get(
        '/student/assignments',
        headers=h_student_2
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 2


def test_post_assignment_null_content(client, h_student_1):
    """
    failure case: content cannot be null
    """

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': None
        })

    assert response.status_code == 400

def test_post_assignment_not_in_draft_state(client, h_student_1):
    """
    failure case: editing assignment not in draft state
    """

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'id':3,
            'content': "New Edited Text"
        })

    assert response.status_code == 400
    
def test_submit_nonexistent_assignment(client, h_student_1):
    """
    Test submitting an assignment that does not exist.
    """
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 999,
            'teacher_id': 2
        }
    )

    assert response.status_code == 404

def test_post_assignment_student_1(client, h_student_1):
    content = 'ABCD TESTPOST'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': content
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == 'DRAFT'
    assert data['teacher_id'] is None


def test_submit_assignment_student_1(client, h_student_1):
    draft_assignment = Assignment.query.filter_by(state=AssignmentStateEnum.DRAFT,student_id=1).first()
    if draft_assignment is not None:
        response = client.post(
            '/student/assignments/submit',
            headers=h_student_1,
            json={
                'id': draft_assignment.id,
                'teacher_id': 2
            })

    assert response.status_code == 200

    data = response.json['data']
    assert data['student_id'] == 1
    assert data['state'] == 'SUBMITTED'
    assert data['teacher_id'] == 2


def test_assignment_resubmit_error(client, h_student_1):
    draft_assignment = Assignment.query.filter_by(state=AssignmentStateEnum.DRAFT,student_id=1).first()
    if draft_assignment is not None:
        response = client.post(
            '/student/assignments/submit',
            headers=h_student_1,
            json={
                'id': draft_assignment.id,
                'teacher_id': 2
            })
        error_response = response.json
        assert response.status_code == 400
        assert error_response['error'] == 'FyleError'
        assert error_response["message"] == 'only a draft assignment can be submitted'


def test_submit_assignment_invalid_student_id(client):
    """
    failure case: Invalid student id
    """

    response = client.post(
        '/student/assignments/submit',
        headers={"user_id":6, "student_id":4},
        json={
            "id":2,
            "teacher_id":2
        })

    assert response.status_code == 401