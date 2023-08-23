from flask_admin.contrib.sqla import ModelView

class NotificationView(ModelView):
    column_display_pk = True
    column_list = ['user_id','created_at','content','seen']
    form_columns = column_list + ['id']