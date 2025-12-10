from models.notification import Notification
from utils.time import TimeUtil


class NotificationService:

    def _generate_new_id(self, notification_list):
        if len(notification_list) == 0:
            return 1
        id_list = [
            notification.get("id") for notification in notification_list
        ]
        id_list.sort()
        last_id = id_list[-1]
        return last_id + 1

    def __init__(self):
        self.time_util = TimeUtil()

    def add(self, notification_list, new_notification: Notification):
        new_notification.set_id(self._generate_new_id(notification_list))
        notification_list.append(new_notification.to_dict())

    def get_by_id(self, notification_list, id):
        for notification in notification_list:
            if notification.get("id") == int(id):
                return notification
        return None

    def remove_by_id(self, notification_list, id):
        notification_to_delete = next(
            (notification for notification in notification_list
             if notification.get("id") == int(id)), None)
        if notification_to_delete:
            notification_list.remove(notification_to_delete)
            return True
        return False
