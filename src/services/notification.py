class Notification:

    def __init__(self, id, title, timestamp, source, type, status, body):
        self.id = id
        self.title = title
        self.timestamp = timestamp
        self.source = source
        self.type = type
        self.status = status
        self.body = body


class NotificationService:

    def __init__(self):
        pass

    def add_notification(self, title, timestamp, source, type, status, body):
        # Logic to send notification
        pass

    if __name__ == "__main__":
        notification_list = []

        custom_notification = Notification(
            id=1,
            title="Server Down",
            timestamp="2024-10-01T12:00:00Z",
            source="MonitoringService",
            type="Alert",
            status="Unread",
            body="The main server is down. Immediate attention required.")
