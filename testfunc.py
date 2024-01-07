
from linebot import LineBotApi,WebhookParser
from linebot.models import *
from settings import *
from sql import *
import psycopg2
import json
import os

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(LINE_CHANNEL_SECRET)

try:
    conn=psycopg2.connect(host=HOST_NAME, 
                        user=USER_NAME, 
                        password=PASSWORD, 
                        dbname=DB_NAME, 
                        port=PORT_NUM)
    cur=conn.cursor()

    #conn.commit()

    print ("success")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)







def quicktest(event):
    try:
        t=TextSendMessage(
                        text='疾病選擇?',
                        quick_reply=QuickReply(
                            items=[
                                QuickReplyButton(
                                    action=PostbackAction(
                                        label='憂鬱症',
                                        data='action=url&item=clarence',
                                        text='憂鬱症'
                                    )
                                ),
                                QuickReplyButton(
                                    action=MessageAction(
                                    label='憂鬱症',
                                    text='sheet'
                                    )
                                ),
                                QuickReplyButton(
                                    action=DatetimePickerAction(
                                        label='Select date',
                                        data="storeId=12345",
                                        mode="datetime",
                                        initial="2024-01-01t00:00",
                                        max="2024-01-30t23:59",
                                    )
                                ),
                            ]
                        )
                    )
        line_bot_api.reply_message(event.reply_token,t)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='失敗'))

def buttontest(event):
    try:
        t=TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title='憂鬱症',
                    text='請選擇功能',
                    actions=[
                        MessageTemplateAction(
                            label='簡介說明',
                            text='test'
                        ),
                        MessageTemplateAction(
                            label='常見症狀',
                            text='test'
                        ),
                        MessageTemplateAction(
                            label='分布情形',
                            text='test'
                        )
                    ]
                )
        )
        line_bot_api.reply_message(event.reply_token,t)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='失敗'))

def flextest(event):
    try:
        flexmsg=FlexSendMessage(
            alt_text='測試flex',
            contents = {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                    }
                }
            }
        )
        line_bot_api.reply_message(event.reply_token,flexmsg)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='失敗'))


