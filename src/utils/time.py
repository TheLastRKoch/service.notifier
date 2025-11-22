from datetime import datetime, timezone


class TimeUtil:

    def get_current_time(self):
        return datetime.now(timezone.utc)

    def get_current_timestamp(self):
        return self.get_current_time().strftime('%Y-%m-%dT%H:%M:%SZ')
