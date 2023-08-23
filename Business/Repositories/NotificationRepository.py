from Data.Persistance.database import *
from Data.Domain.Notification import Notification


class NotificationRepository:
    db_context = db_session

    def create_notification_for_user(self, user_id, message):
        notification = Notification()

        notification.user_id = user_id
        notification.content = message
        try:
            self.db_context.add(notification)
            self.db_context.commit()
        except:
            pass

    def get_new_notifications_for_user(self,user_id):
        return Notification.query.filter(Notification.user_id == user_id,Notification.seen == 0).order_by(Notification.id.desc()).all()

    def mark_notification_as_seen(self,notification_id,user_id):
        notification = Notification.query.filter(Notification.id == notification_id,Notification.user_id == Notification.user_id).first()

        notification.seen = True

        self.db_context.commit()


n = NotificationRepository()
