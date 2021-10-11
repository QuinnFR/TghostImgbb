from ..IMGClient import IMG
from pyrogram import filters
from pyrogram.types import Message
from ..workers.img_uploader import img_uploader


@IMG.on_message(filters.photo)
async def onPhotho(client, msg):
    file_path = await msg.download(file_name=f"downloads/{msg.chat.id}/")
    responce = await img_uploader(file_path=file_path, msg=msg)
    if (responce is None):
        return
    title = responce['data']['title']

    # print(see['data']['url'])
    await client.send_message(
        chat_id=msg.chat.id,
        text=
        f"**Name: {title}\nDirect URL: [{title}]({responce['data']['url']})**",
        parse_mode="markdown",
        reply_to_message_id=msg.message_id,
    )
