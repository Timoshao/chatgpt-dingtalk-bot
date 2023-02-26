"""Main module."""
from fastapi import BackgroundTasks, FastAPI
from revChatGPT.V1 import AsyncChatbot
from .config import gpt_settings
from .dingtalk import DingtalkCorpAPI
from .constants import BUSSY_MESSAGE

from .schemas import ConversationTypeEnum, DingtalkAskMessage


app = FastAPI()

# Initialize chatbot
chatbot = AsyncChatbot(config=gpt_settings.dict(exclude_unset=True))
dingtalk_sdk = DingtalkCorpAPI()


async def reply(
    prompt: str,
    nickname: str,
    sender_userid: str,
    webhook_url: str,
    conversation_type: str,
):
    """发送群聊信息"""
    response = ""
    try:
        async for data in chatbot.ask(
            prompt
        ):
            response = data["message"].strip()
    except Exception as e:
        if BUSSY_MESSAGE in str(e):
            response = "在发送另一条消息之前，请等待任何其他响应完成，或者等待一分钟。"
        else:
            response = str(e)

    title = response[10:]
    payload = {"msgtype": "markdown"}
    # 群聊时加上@
    if conversation_type == ConversationTypeEnum.group and sender_userid:
        response = f"@{sender_userid}\n\n{response}"
        payload["at"] = {"atUserIds": [sender_userid]}

    payload["markdown"] = {"title": f" {title}", "text": response}
    await dingtalk_sdk.robot_webhook_send(webhook_url, json=payload)


@app.post("/chat")
async def chat(message: DingtalkAskMessage, background_tasks: BackgroundTasks):
    prompt = message.text.content.strip()
    nickname = message.senderNick
    sender_userid = message.senderStaffId
    webhook_url = message.sessionWebhook
    if prompt.startswith("清空会话"):
        chatbot.reset()

    if prompt == "":
        return

    background_tasks.add_task(
        reply,
        prompt,
        nickname,
        sender_userid,
        webhook_url,
        message.conversationType,
    )
    return "ok"
