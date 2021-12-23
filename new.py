# 這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


def test():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message


def test_bear():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="data:image/jpeg;base64,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",
                ),
            ]
        )
    )
    return message
