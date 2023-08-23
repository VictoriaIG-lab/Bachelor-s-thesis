from unittest import *

from Business.Services.UserService import UserService


class UserServiceTest(TestCase):

    def setUp(self):
        self.user_service = UserService()

    def tearDown(self):
        self.user_service = None

    def test_get_user_by_id(self):

        a = self.user_service.get_user_by_id(1)
        self.assertIsNotNone(self.user_service.get_user_by_id(1))

    def test(self):
        usr = self.user_service.get_current_user()
        self.assertIsNotNone(usr)
