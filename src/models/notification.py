from utils.time import TimeUtil


class Notification:

    def __init__(self,
                 title,
                 source,
                 type="silent",
                 status="toRead",
                 body=None):

        self.time_util = TimeUtil()

        self.id = 0
        self.title = title
        self.source = source
        self.type = type
        self.status = status
        self.body = body

    def set_id(self, id):
        self.id = id

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "timestamp": self.time_util.get_current_timestamp(),
            "source": self.source,
            "type": self.type,
            "status": self.status,
            "body": self.body
        }
