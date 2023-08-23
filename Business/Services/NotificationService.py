from flask_login import current_user

from Business.Repositories.NotificationRepository import NotificationRepository


class NotificationService:
    _notification_repository = NotificationRepository()

    def get_new_notification_for_user(self,user_id):
        return self._notification_repository.get_new_notifications_for_user(user_id)

    def mark_notifications_as_seen(self,list_of_notification_id):
        user_id = current_user.id
        for id in list_of_notification_id:
            self._notification_repository.mark_notification_as_seen(id,user_id)
