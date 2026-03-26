from unittest import TestCase

from uc3m_consulting import EnterpriseManager, EnterpriseManagementException

class TestRF1(TestCase):

    def test_TC1(self):
        o=EnterpriseManager()
        result=o.register_project('B12345678','PRO01','valid text','HR','18/02/2026',100000.00)
        #self.assertEqual(result,"")