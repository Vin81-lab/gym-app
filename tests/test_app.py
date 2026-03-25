# Basic Test setup
import pytest
from app import app, db
from models import Member

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

# Test Home Route
def test_home(client):
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200

# Test Members Page (GET)
def test_members_get(client):
    response = client.get('/members')
    assert response.status_code == 200

# Test Add Member (POST)
def test_add_member(client):
    response = client.post('/members', data={
        'name': 'John',
        'age': 25,
        'plan': 'Monthly'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'John' in response.data

# Test Database logic
def test_member_model(client):
    with app.app_context():
        member = Member(name="Alice", age=30, plan="Yearly")
        db.session.add(member)
        db.session.commit()

        result = Member.query.filter_by(name="Alice").first()
        assert result is not None
        assert result.plan == "Yearly"

# Test Validation (Edge Cases)
def test_empty_member(client):
    response = client.post('/members', data={
        'name': '',
        'age': '',
        'plan': ''
    }, follow_redirects=True)
    assert response.status_code == 200


