from mhtrade.tests import *

class TestUserRegisterController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='user_register', action='index'))
        # Test response...
