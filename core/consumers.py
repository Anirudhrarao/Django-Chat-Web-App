import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    """
    ChatConsumer handles WebSocket connections for the chat application.

    Attributes:
        roomGroupName (str): The name of the chat room group.
    """

    async def connect(self):
        """
        Called when the WebSocket is handshaking as part of the connection process.
        Adds the consumer to a chat room group and accepts the connection.
        """
        self.roomGroupName = "Chat_app"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()
    
    async def disconnect(self, close_code):
        """
        Called when the WebSocket closes for any reason.
        Removes the consumer from the chat room group.
        Args:
            close_code: The code indicating the reason for the disconnection.
        """
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )
    
    async def receive(self, text_data):
        """
        Called when the WebSocket receives a message from the client.
        Parses the received JSON data and sends it to the chat room group.
        Args:
            text_data (str): The received JSON-encoded message.
        """
        text_json = json.loads(text_data)
        message = text_json['message']
        username = text_json['username']
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
            })

    async def sendMessage(self, event):
        """
        Sends a message to the WebSocket consumer.
        Args:
            event (dict): The message event containing 'message' and 'username'.
        """
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({"message": message, "username": username}))
