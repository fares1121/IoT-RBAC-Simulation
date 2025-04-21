class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

class RBAC:
    def __init__(self):
        self.roles = {
            'Admin': Role('Admin', ['view_dashboard', 'modify_widgets', 'add_device']),
            'Operator': Role('Operator', ['view_dashboard', 'modify_widgets']),
            'Viewer': Role('Viewer', ['view_dashboard'])
        }

    def get_role_permissions(self, role_name):
        role = self.roles.get(role_name)
        if role:
            return role.permissions
        return None

    def can_user(self, role_name, action):
        role = self.roles.get(role_name)
        if role:
            return action in role.permissions
        return False