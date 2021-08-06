# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat,Room
from channels.db import database_sync_to_async
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.Owner = self.scope['url_route']['kwargs']['Owner']
        self.Sender = self.scope['url_route']['kwargs']['Sender']
        self.room_group_name = 'chat_%s' % self.room_name
        self.room_id = await self.room_create(self.room_group_name)
        await self.accept()

        self.room_message = await self.room_message()
        await self.room_all_message(self.room_message)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.create_message(message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    async def room_all_message(self,*args,**kwargs):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'data': args[0],
        }))

    @database_sync_to_async
    def create_message(self,message):
        create = Chat.objects.create(room_id=self.room_id,message=message)
        return True

    @database_sync_to_async
    def room_create(self,room_group_name):
        room=Room.objects.get_or_create(name=room_group_name)
        room[0].users.add(self.Owner,self.Sender)
        return room[0].id

    @database_sync_to_async
    def room_message(self):
        rm = Room.objects.get(id=self.room_id)
        a = rm.chat_set.all().values()
        x=[r for r in a]
        return json.dumps(x)
