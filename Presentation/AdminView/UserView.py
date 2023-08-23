from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    column_display_pk = True
    form_columns = ['id', 'name', 'email', 'elo_rating', 'active', 'role']
    column_list = form_columns + ['password']
