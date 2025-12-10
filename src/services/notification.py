from models.notification import Notification
from utils.time import TimeUtil


class NotificationService:

    def _generate_new_id(self, notification_list):
        """
        Generate the next integer notification ID from the IDs present in notification_list.
        
        Parameters:
            notification_list (list): Sequence of notification dictionaries that contain an "id" key.
        
        Returns:
            int: 1 if notification_list is empty, otherwise one greater than the maximum `id` found.
        """
        if len(notification_list) == 0:
            return 1
        id_list = [
            notification.get("id") for notification in notification_list
        ]
        id_list.sort()
        last_id = id_list[-1]
        return last_id + 1

    def __init__(self):
        """
        Initialize the NotificationService.
        
        Creates a TimeUtil instance and stores it on self.time_util for time-related utilities used by the service.
        """
        self.time_util = TimeUtil()

    def add(self, notification_list, new_notification: Notification):
        """
        Add a Notification object to an in-memory notification list.
        
        Parameters:
            notification_list (list): List of notification dictionaries to which the notification will be appended.
            new_notification (Notification): Notification instance whose `id` will be set to the next available integer and then converted to a dictionary and appended to `notification_list`.
        """
        new_notification.set_id(self._generate_new_id(notification_list))
        notification_list.append(new_notification.to_dict())

    def get_by_id(self, notification_list, id):
        """
        Retrieve a notification dictionary from a list by its numeric id.
        
        Parameters:
            notification_list (list): List of notification dictionaries, each expected to contain an "id" key.
            id: The id to match; will be cast to int for comparison.
        
        Returns:
            dict or None: The notification dictionary with a matching `id`, or `None` if no match is found.
        """
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