from discord import Webhook, RequestsWebhookAdapter, Embed

def avatar_url():
    return "https://cdn.discordapp.com/avatars/597049067738103808/87268e7934f8da3add6bd5621ee610d5.webp?size=128"

def send_webhook():
    url = 'webhook_link'
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(color=65365,title='Successfully checked out!',\
    description='Rammellzee Tee')\
    .set_thumbnail(url='https://assets.supremenewyork.com/187962/rs/xAV4l1Q02ks.jpg')\
    .add_field(name='store',value='Supreme EU',inline=True)\
    .add_field(name='Size',value='XLarge',inline=True)\
    .add_field(name='Profile',value='||eason||',inline=True)\
    .add_field(name='Order',value='||fake||',inline=True)\
    .add_field(name='Proxy List',value='||GEO||',inline=True)\
    .add_field(name='Color',value='White',inline=True)\
    .add_field(name='Category',value='T-Shirts',inline=True)\
    .add_field(name='3D Secure',value='Disabled',inline=True)\
    .add_field(name='Mode',value='Safe',inline=True)\
    .set_footer(icon_url='https://images-ext-2.discordapp.net/external/AFl8btw6-OdaFIC4DU6c8as5gTG8SIVdsOx_hLOXnEs/https/cdn.cybersole.io/media/discord-logo.png',text='CyberAIO • 14/04/2020 00:30:18.195')
    webhook.send(embed=embed,avatar_url=avatar_url(),username="CyberAIO")
send_webhook()
