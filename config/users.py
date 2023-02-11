from testdata.users import Users as USR
class Users:

    @staticmethod
    def get_user_email():
        return USR.USER1_EMAIL

    @staticmethod
    def get_user_password():
        return USR.USER1_PSW

    @staticmethod
    def get_user_expected_full_name():
        return USR.USER1_FULL_NAME
