from discord import Webhook, RequestsWebhookAdapter, Embed

def avatar_url():
    return None

def send_webhook():
    url = 'webhook_link'
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(color=272183,title='FY5158 Checkout Successful | Splashforce',url='https://twitter.com/GaneshBot',)\
    .set_thumbnail(url='https://assets.yeezysupply.com/images/w_937,f_auto,q_auto:sensitive,fl_lossy/c3c8886a281e42e786a9ab95010b82fb_ce49/YEEZY_BOOST_350_V2_LINEN_FY5158_FY5158_04_standard.png')\
    .add_field(name='PID',value='FY5158',inline=True)\
    .add_field(name='Size',value='5',inline=True)\
    .add_field(name='Order Number',value='AYS12345678',inline=True)\
    .add_field(name='Profile',value='eason',inline=False)\
    .set_footer(icon_url='https://media.discordapp.net/attachments/284082692591583252/585559939746103308/emote.png',text='Splashforce•2020/04/18')
    webhook.send(embed=embed,avatar_url=avatar_url(),username="Splashforce")
send_webhook()
