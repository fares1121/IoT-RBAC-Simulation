import unittest
from src.rbac.roles import Role, Admin, Operator, Viewer
from src.rbac.permissions import check_permission

class TestRBAC(unittest.TestCase):

    def setUp(self):
        self.admin = Admin()
        self.operator = Operator()
        self.viewer = Viewer()

    def test_admin_permissions(self):
        self.assertTrue(check_permission(self.admin, 'view_dashboard'))
        self.assertTrue(check_permission(self.admin, 'modify_widgets'))
        self.assertTrue(check_permission(self.admin, 'add_device'))

    def test_operator_permissions(self):
        self.assertTrue(check_permission(self.operator, 'view_dashboard'))
        self.assertTrue(check_permission(self.operator, 'modify_widgets'))
        self.assertFalse(check_permission(self.operator, 'add_device'))

    def test_viewer_permissions(self):
        self.assertTrue(check_permission(self.viewer, 'view_dashboard'))
        self.assertFalse(check_permission(self.viewer, 'modify_widgets'))
        self.assertFalse(check_permission(self.viewer, 'add_device'))

if __name__ == '__main__':
    unittest.main()