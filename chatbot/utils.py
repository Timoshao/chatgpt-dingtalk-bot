import uuid

from revChatGPT.V1 import AsyncChatbot

from .config import gpt_settings


def get_conversation_id(convo_id: str):
    """
    将钉钉会话id转成uuid
    """
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, convo_id))


def init_chatbots():
    """
    初始化
    """
    config = gpt_settings.dict(exclude_unset=True)
    accounts = config.pop("accounts").split(",") if "accounts" in config else []
    access_tokens = (
        config.pop("access_tokens").split(",") if "access_tokens" in config else []
    )
    if accounts and access_tokens:
        raise ValueError("You cannot set both account and token!")

    bots = []
    for account in accounts:
        try:
            email, password = account.split(":")
        except Exception:
            raise ValueError("邮箱密码格式错误，正确格式为: <邮箱1>:<密码1>,<邮箱2>:<密码2>...")
        print(dict(email=email, password=password, **config))
        c = dict(email=email, password=password, **config)
        bots.append(AsyncChatbot(config=c))

    for access_token in access_tokens:
        c = dict(access_token=access_token, **config)
        bots.append(c)

    return bots
