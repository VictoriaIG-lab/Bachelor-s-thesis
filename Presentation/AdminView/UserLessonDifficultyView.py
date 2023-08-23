from flask_admin.contrib.sqla import ModelView

class UserLessonDifficultyView(ModelView):
    column_display_pk = True
    form_columns = ['user_id','lesson_id','elo_rating','completed','temporary_code']
    column_list = form_columns