from flask_admin.contrib.sqla import ModelView

class ChapterExerciseView(ModelView):
    column_display_pk = True
    form_columns = ['exercise_id','chapter_id']
    column_list = form_columns