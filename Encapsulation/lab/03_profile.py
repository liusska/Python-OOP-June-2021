class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_length_valid(value) and self.contains_digits(value) and self.contains_uppercase(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def is_length_valid(self, password):
        if len(password) >= 8:
            return True

    def contains_uppercase(self, password):
        upper_letters = [ch for ch in password if ch.isupper()]
        return True if upper_letters else False

    def contains_digits(self, password):
        digits = [ch for ch in password if ch.isdigit()]
        return True if digits else False

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*"*len(self.password)}'


# profile_with_invalid_username = Profile('Too_long_username', 'Any')

# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
