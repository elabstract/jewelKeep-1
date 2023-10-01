# app/user_accounts.py

```python
class UserAccounts:
    def __init__(self):
        self.users = []

    def register_user(self, username, password):
        user = {
            'username': username,
            'password': password
        }
        self.users.append(user)

    def login_user(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return True
        return False

    def delete_user(self, username):
        for user in self.users:
            if user['username'] == username:
                self.users.remove(user)
                return True
        return False
```
