import string
from password.new_password import generate_password

def test_password_characters():
    
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  
    for char in password:
        assert char in valid_characters

def test_password_length():
   
    for length in [8, 12, 20, 100]:  
        password = generate_password(length)
        assert len(password) == length

def test_password_uniqueness():
    
    password1 = generate_password()
    password2 = generate_password()
    assert password1 != password2