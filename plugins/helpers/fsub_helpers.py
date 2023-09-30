from pyrogram import enums, Client


async def is_owner(chat_id: int, user_id: int):
    async for x in Client.get_chat_members(chat_id):
        if x.status == enums.ChatMemberStatus.OWNER:
             if x.user.id == user_id:
                 return True
             else: return False

async def is_admin(chat_id: int, user_id: int):
     admin = await Client.get_chat_member(chat_id, user_id)
     if admin.privileges:
         return True
     return False

async def can_ban_members(chat_id: int, user_id: int):
     admin = await Client.get_chat_member(chat_id, user_id)
     if admin.privileges.can_restrict_members:
         return True
     return False

async def can_pin_messages(chat_id: int, user_id: int):
     admin = await Client.get_chat_member(chat_id, user_id)
     if admin.privileges.can_pin_messages:
         return True
     return False

async def can_delete_messages(chat_id: int, user_id: int):
     admin = await Client.get_chat_member(chat_id, user_id)
     if admin.privileges.can_delete_messages:
         return True
     return False

async def can_promote_members(chat_id: int, user_id: int):
     admin = await Client.get_chat_member(chat_id, user_id)
     if admin.privileges.can_promote_members:
         return True
     return False

async def can_promote_members(chat_id: int, user_id: int):
     admin = await Client.get_chat_member(chat_id, user_id)
     if admin.privileges.can_promote_members:
         return True
     return False

async def can_change_info(chat_id: int, user_id: int):
     admin = await Client.get_chat_member(chat_id, user_id)
     if admin.privileges.can_change_info:
         return True
     return False

