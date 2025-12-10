from utils.time import TimeUtil


class Notification:

    def __init__(self,
                 title,
                 source,
                 type="silent",
                 status="toRead",
                 body=None):
        """
                 Initialize a Notification with metadata and default state.
                 
                 Parameters:
                     title (str): Notification title.
                     source (str): Origin of the notification (e.g., service or component name).
                     type (str): Notification type; defaults to "silent".
                     status (str): Initial delivery/read status; defaults to "toRead".
                     body (Optional[Any]): Optional payload or additional details for the notification.
                 
                 Notes:
                     Sets self.id to 0 and creates a TimeUtil instance assigned to self.time_util.
                 """
                 self.time_util = TimeUtil()

        self.id = 0
        self.title = title
        self.source = source
        self.type = type
        self.status = status
        self.body = body

    def set_id(self, id):
        """
        Assigns a unique identifier to the notification.
        
        Parameters:
            id (int): Identifier to assign to this notification.
        """
        self.id = id

    def to_dict(self):
        """
        Produce a dictionary representation of the notification suitable for serialization.
        
        The dictionary contains the notification's `id`, `title`, `timestamp` (obtained at call time), `source`, `type`, `status`, and `body`.
        
        Returns:
            dict: A mapping with keys `"id"`, `"title"`, `"timestamp"`, `"source"`, `"type"`, `"status"`, and `"body"`; `"body"` may be `None`.
        """
        return {
            "id": self.id,
            "title": self.title,
            "timestamp": self.time_util.get_current_timestamp(),
            "source": self.source,
            "type": self.type,
            "status": self.status,
            "body": self.body
        }