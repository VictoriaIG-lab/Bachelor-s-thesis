from flask_admin.contrib.sqla import ModelView
class ChapterLessonView(ModelView):
    column_display_pk = True
    form_columns = ['chapter_id','lesson_id']
    column_list = form_columns