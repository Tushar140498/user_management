import uuid
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import (
    UserBase,
    UserCreate,
    UserUpdate,
    UserResponse,
    UserListResponse,
    LoginRequest,
    validate_password_complexity
)

# Fixtures for common test data
@pytest.fixture
def user_base_data():
    return {
        "nickname": "john_doe_123",
        "email": "john.doe@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "role": "AUTHENTICATED",
        "bio": "I am a software engineer with over 5 years of experience.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoe",
        "github_profile_url": "https://github.com/johndoe"
    }

@pytest.fixture
def user_create_data(user_base_data):
    return {**user_base_data, "password": "SecurePassword123!"}

@pytest.fixture
def user_update_data():
    return {
        "email": "john.doe.new@example.com",
        "nickname": "j_doe",
        "first_name": "John",
        "last_name": "Doe",
        "bio": "I specialize in backend development with Python and Node.js.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe_updated.jpg"
    }

@pytest.fixture
def user_response_data(user_base_data):
    return {
        "id": uuid.uuid4(),
        "nickname": user_base_data["nickname"],
        "first_name": user_base_data["first_name"],
        "last_name": user_base_data["last_name"],
        "role": user_base_data["role"],
        "email": user_base_data["email"],
        "links": []
    }

@pytest.fixture
def login_request_data():
    return {"email": "john_doe_123@emai.com", "password": "SecurePassword123!@"}

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# Tests for UserResponse
def test_user_response_valid(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.id == user_response_data["id"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

@pytest.mark.parametrize("password, expected", [
    ("Valid@123", True),
    ("Strong$Pass2024", True),
    ("P@ssw0rd1234", True),
    ("Comp!ex123", True),
    ("NoSpecial123", False),
    ("Short1!", False),
    ("onlyletters@", False),
    ("12345678!", False),
    ("password!", False),
    ("UPPERCASE123", False),
    ("lowercase@123", False),
    ("1234abcd@", False),
    ("abcd!1234", False),
    ("uppercase#123", False),
    ("password", False),
    ("@!#&", False),
])
def test_validate_password_complexity(password, expected):
    if expected:
        assert validate_password_complexity(password) == password
    else:
        with pytest.raises(ValueError):
            validate_password_complexity(password)


#More test case
def test_user_create_missing_password(user_base_data):
    with pytest.raises(ValidationError):
        UserCreate(**user_base_data)

def test_user_create_weak_password(user_base_data):
    user_base_data["password"] = "weak"
    with pytest.raises(ValueError):
        UserCreate(**user_base_data)

@pytest.mark.parametrize("missing_field", ["email", "password"])
def test_login_request_missing_fields(missing_field, login_request_data):
    login_request_data.pop(missing_field)
    with pytest.raises(ValidationError):
        LoginRequest(**login_request_data)
        
def test_user_base_url_empty_string(user_base_data):
    user_base_data["profile_picture_url"] = ""
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

@pytest.mark.parametrize("url", ["mailto://email@example.com", "data:image/png;base64"])
def test_user_base_url_invalid_protocols(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

@pytest.mark.parametrize("password", [
    "Ab1!",  # Minimum length, valid
    "Ab1"    # Too short
])
def test_password_complexity_edge_length(password):
    if len(password) >= 8:  # Adjust based on your minimum length
        assert validate_password_complexity(password) == password
    else:
        with pytest.raises(ValueError):
            validate_password_complexity(password)


@pytest.mark.parametrize("password", [
    "ONLYUPPERCASE1234",  # Missing lowercase and special
    "onlylowercase1234",  # Missing uppercase and special
    "OnlylowerUPPER",     # Missing digits and special
])
def test_password_complexity_missing_character_types(password):
    with pytest.raises(ValueError):
        validate_password_complexity(password)

def test_user_base_multiple_invalid_fields(user_base_data):
    user_base_data["nickname"] = "a"  # Too short
    user_base_data["email"] = "invalidemail"  # Invalid format
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)
