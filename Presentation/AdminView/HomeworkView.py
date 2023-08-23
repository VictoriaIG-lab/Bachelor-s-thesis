from flask_admin.contrib.sqla import ModelView


class HomeworkView(ModelView):
    column_display_pk = True
    form_columns = ['title', 'content', 'days_available', 'default_points', 'test_cases']
    column_list = form_columns + ['id']
