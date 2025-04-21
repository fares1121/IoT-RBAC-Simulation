class Permissions:
    def __init__(self):
        self.permissions = {
            'Admin': {
                'view_dashboard': True,
                'modify_widgets': True,
                'add_device': True
            },
            'Operator': {
                'view_dashboard': True,
                'modify_widgets': True,
                'add_device': False
            },
            'Viewer': {
                'view_dashboard': True,
                'modify_widgets': False,
                'add_device': False
            }
        }

    def check_permission(self, role, action):
        if role in self.permissions:
            return self.permissions[role].get(action, False)
        return False

    def get_permissions(self, role):
        return self.permissions.get(role, {})