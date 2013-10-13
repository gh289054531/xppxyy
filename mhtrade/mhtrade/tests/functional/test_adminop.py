from mhtrade.tests import *

class TestAdminopController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='adminop', action='index'))
        # Test response...
