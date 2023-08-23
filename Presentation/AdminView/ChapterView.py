from flask_admin.contrib.sqla import ModelView
class ChapterView(ModelView):
    column_display_pk = True
    form_columns = ['title']
    column_list = form_columns + ['id']