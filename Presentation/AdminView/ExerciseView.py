from flask_admin.contrib.sqla import ModelView
class ExerciseView(ModelView):
    column_display_pk = True
    form_columns = ['title','content','source_code','default_elo_rating','solved_source_code']
    column_list = form_columns + ['id']