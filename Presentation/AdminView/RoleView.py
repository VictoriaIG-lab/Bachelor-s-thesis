from flask_admin.contrib.sqla import ModelView

class RoleView(ModelView):
    column_display_pk = True
    form_columns = ['name','description']
    column_list = form_columns + ['id']