from utils.time import TimeUtil


class NotificationService:

    def __init__(self):
        self.time_util = TimeUtil()

    def _generate_new_id(self, notification_list):
        if len(notification_list) == 0:
            return 1
        id_list = [
            notification.get("id") for notification in notification_list
        ]
        id_list.sort()
        last_id = id_list[-1]
        return last_id + 1

    def add(self, notification_list, title, source, type, status, body):
        new_id = self._generate_new_id(notification_list)

        notification_list.append({
            "id": new_id,
            "title": title,
            "timestamp": self.time_util.get_current_timestamp(),
            "source": source,
            "type": type,
            "status": status,
            "body": body
        })

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
