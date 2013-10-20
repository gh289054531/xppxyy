from mhtrade.tests import *

class TestUserregisterController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='userRegister', action='index'))
        # Test response...
