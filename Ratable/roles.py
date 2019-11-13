from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {

        'add_user': True,
        'add_line_manager': True,
        'add_department': True,
        'add_area' : True,
        'add_kpi': True,
        'remove_user': True,
        'remove_line_manager': True,
        'remove_department': True,
        'remove_area' : True,
        'remove_kpi': True,

    }


class LineManager(AbstractUserRole):
    available_permissions = {
        'add_area' : True,
        'add_kpi': True,
        'remove_area' : True,
        'remove_kpi': True,

    }


class Staff(AbstractUserRole):
    available_permissions = {
        'add_kpi': True,
        'remove_kpi': True,
    }