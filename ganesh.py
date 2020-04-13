from discord import Webhook, RequestsWebhookAdapter, Embed

def avatar_url():
    return None

def send_webhook():
    url = 'https://discordapp.com/api/webhooks/699307331191570514/4KaKkDhC2YMVrUt1MwfibEDgBlh-tWe9sd0C1bb1EE0yI_D_K_AKo2NFb8_G5BmnQ6IO'
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(color=272183,title='Successful Checkout!',url='https://twitter.com/GaneshBot',\
    description='[Track Order](https://discordapp.com)')\
    .set_thumbnail(url='https://images-ext-2.discordapp.net/external/jC5X2if_uh33Ut8mfclRG0bKVsFEXz50WFRdC404WEM/http/runnerspoint.scene7.com/is/image/rpe/314100260604')\
    .add_field(name='Date Time',value='||14/11/2019 08:58:59||',inline=True)\
    .add_field(name='Website',value='Footlocker EU (DE)',inline=True)\
    .add_field(name='Profile',value='||eason.qqqqq.com||',inline=False)\
    .add_field(name='Product',value='Jordan 1 Mid - Men Shoes',inline=True)\
    .add_field(name='Size',value='EU 41 / US 8',inline=True)\
    .add_field(name='Order Number',value='||14190527079123456789||',inline=False)\
    .add_field(name='Proxy',value='||GB-30m.geosurf.io:8000:12345+GB+12345-123456789123:123455||',inline=False)\
    .set_footer(icon_url='https://images-ext-2.discordapp.net/external/XnfnaHmjhY6X2sMmA_z-5DoHnj5ZzpfudyBd2ABJ9h0/https/s3.eu-west-2.amazonaws.com/ganeshbotdl/ganesh_logo_square.png',text='@GaneshBot•2020/04/14')
    webhook.send(embed=embed,avatar_url=avatar_url(),username="GaneshBot Checkout")
send_webhook()