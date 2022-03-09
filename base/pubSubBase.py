import stomp

from base.configReader import Configuration


class PubSubBase:
    """the basic pub sub provides the topic one can send at or receive to."""

    def __init__(self, config: Configuration):
        self.connection = None
        self.config = config
        self.connect()

    def connect(self):
        """creates a connection with the message broker"""
        self.connection = stomp.Connection([
            (self.config['transport']['ip'],
             self.config['transport']['port'])])
        self.connection.set_listener('', stomp.PrintingListener())
        self.connection.connect(wait=True)

    def __del__(self):
        """disconnects while object is destructed"""
        if self.connection.is_connected:
            self.connection.disconnect()
