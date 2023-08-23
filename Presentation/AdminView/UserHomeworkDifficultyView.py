from flask_admin.contrib.sqla import ModelView


class UserHomeworkDifficultyView(ModelView):
    column_display_pk = True
    form_columns = ['user_id', 'homework_id', 'points','temporary_code','created_at','days_remaining', 'expired', 'completed']
    column_list = form_columns
