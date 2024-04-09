import logging


class LogEvent:
    def __init__(self):
        pass

    @staticmethod
    def log_get(user, route) -> None:
        logging.info(f"User {user} visited page: {route}")

    @staticmethod
    def log_post(user, action, entity) -> None:
        logging.info(f"User {user} {action} {entity}")

    @staticmethod
    def log_insufficient_privileges(user, route) -> None:
        logging.info(f"User {user} had insufficient privileges when opening the page {route}")
