from flask_admin.contrib.sqla import ModelView


class UserEloUpdateView(ModelView):
    column_display_pk = True
    form_columns = ['user_id', 'elo_difference', 'created_at', 'notes']
    column_list = form_columns + ['id']
