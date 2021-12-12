from wtforms.validators import ValidationError
from password_strength import PasswordPolicy, PasswordStats
class EnforcingStrongPasswords():
    def __init__(self, length=8, uppercase=1, numbers=1, strength=0.67):
        self.policy = PasswordPolicy.from_names(
            length=length,  # min length: 8
            uppercase=uppercase,  # need min. 2 uppercase letters
            numbers=numbers,  # need min. 2 digits
            strength=strength # need a password that scores at least 0.5 with its entropy bits
            )
    def check(self, password):
        stats = PasswordStats(password)
        print(password, stats.strength())
        checkpolicy = self.policy.test(password)
        print(password, checkpolicy)

"""
Callable class for enforcing strong passwords
@param password: your password
@param length: the minimum length of the password
@param numbers: the minimum - 1 number of passwords
@param strength: the degree of entropy with the password

@return: boolean: whether or not the password meets these requirements.
"""
class EnforcingStrongPasswords():
    def __init__(self, length=8, uppercase=1, numbers=1, strength=0.66):
        self.policy = PasswordPolicy.from_names(
            length=length,  # min length: 8
            uppercase=uppercase,  # need min. 2 uppercase letters
            numbers=numbers,  # need min. 2 digits
            strength=strength # need a password that scores at least 0.5 with its entropy bits
            )
    def __call__(self, form, password):
        stats = PasswordStats(password)
        print(stats)
        checkpolicy = self.policy.test(password)
        if not checkpolicy:
            raise ValidationError("Your password is not strong enough. Try again.")

if __name__ == "__main__":
    print(EnforcingStrongPasswords().check("aeiouaeiouaeiou"))
    print(EnforcingStrongPasswords().check("V3ryG00dPassw0rd?!"))
    print(EnforcingStrongPasswords().check("kayaking"))
    print(EnforcingStrongPasswords().check("99areacode"))
    print(EnforcingStrongPasswords().check("99"))
    print(EnforcingStrongPasswords().check("k34"))