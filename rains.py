from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =698653628176531478  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    if now == '00:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('How are UZURAS<:uzu:699374038220538006>BOT doing today?<:uzu2:700858786960900117>.....<:uzu1:700858878879072303>‼') 
    
    if now == '00:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone Mornin!Rain☔ is 1min later.<:good01:699581068285706301>51120671>')  
    
    if now == '00:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 200 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:JPYNdisco:698471276498649168>')  

    if now == '00:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 777 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:BGPT02:698471366004965406> ')

    if now == '00:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 300 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:benkeicoinsl:698471387064696833>')

    if now == '00:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 250 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:JPYNdisco:698471276498649168>')  
  
    if now == '00:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 222 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:JPYNdisco:698471276498649168>')  
    
    if now == '00:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 777 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:BGPT02:698471366004965406> ')

    if now == '00:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 333 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:benkeicoinsl:698471387064696833>')

    if now == '00:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:heart02:699580174911668225>Okay,later👋')     

    if now == '01:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone <:heart02:699580174911668225>are you ready Okay')     

    if now == '01:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 60 3 EquallyDistributed  <:good01:699581068285706301><:JPYNdisco:698471276498649168>⚾Plz receive→/catch')
    
    if now == '01:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 777 4 AttenuationDistributed  <:BGPT02:698471366004965406><:good:699580636448423936>⚾Plz receive→/catch')
    
    if now == '01:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BEN 100 4 AttenuationDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>⚾Plz receive→/catch')
    
    if now == '01:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good01:699581068285706301> Okay,later👋')  
    
    if now == '01:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 77.7 ActiveUserOnly  <:good01:699581068285706301>🌈 <:benkeicoinsl:698471387064696833> ')  
        
    if now == '02:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 10 ActiveUserOnly  🌈 <:JPYNdisco:698471276498649168> ')
        
    if now == '02:58':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767349828714606/hg.png ')    

    if now == '02:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:suika_paku:699072728153587782> Im hungry!I want to eat meat🍖🍗29coin?!')    
     
    if now == '03:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw 29coin 29292.929 5 EquallyDistributed   🍖🍗Plz receive→/catch<:hai_kao:699072592987947117>29meat🍖🍗')

    if now == '03:13':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:guru:699579775500681246>💦I’m so full that I can’t breathe.🍖🍗!Sorry....ww')
        
    if now == '03:14':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Plz.<:kanngaeru:699072662382837881> give me?【/tip 29coin *** @🌈Rains☔ 】Tip🍖')
        
    if now == '03:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good01:699581068285706301> ☑🥩29coin tip please. If you tip 29coins of 10000 or 100000, in return, I will tip JPNY COIN for a while!【/tip 29coin <@700176826282147851>】') 
        
    if now == '03:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767323304067133/hty.png ') 

    if now == '03:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good:699580636448423936>Thank you! for the MeatCoin🥩29coin<:ty:699857337980026930>Tip! Will eat later.🍖')      
        
    if now == '03:27':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain KENJ 50 ActiveUserOnly  ☔<:kenj:700136543003607101>')     
        
    if now == '03:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/701765831268368474/701767123252543498/iku.png')     
         
    if now == '03:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone <:hello:699779689127870514> Rain☔ is 1min later.<:good01:699581068285706301>✨')   
        
    if now == '03:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 1000 ActiveUserOnly  🌈 <:BGPT02:698471366004965406>') 
    
    if now == '03:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 777.77 ActiveUserOnly  🌈 <:BENKEICOIN04:698471407650209832> ')  

    if now == '03:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 333.3 ActiveUserOnly  🌈 <:JPYNdisco:698471276498649168> ')    
    
    if now == '03:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain KENJ 1111.11 ActiveUserOnly  ☔<:kenj:700136543003607101>') 
            
    if now == '03:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 400 8 EquallyDistributed  <:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168>Pls receive→/catch')
    
    if now == '03:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 1200 8 EquallyDistributed  <:good01:699581068285706301><:BGPT02:698471366004965406><:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch')
    
    if now == '03:42':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BEN 200 8 AttenuationDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>⚾Plz receive→/catch')
      
    if now == '03:44':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767323304067133/hty.png') 
          
    if now == '03:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:bye:699863270802325604>See you!またね👋')  
        
    if now == '04:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701775150743289956/migi.png ') 
        
    if now == '04:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here 👆/catch<:kaokanga:699072678614663210>? See you later!') 

    if now == '04:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 10 ActiveUserOnly  🌈 <:JPYNdisco:698471276498649168> ')   
        
    if now == '05:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 20 ActiveUserOnly  <:rain:699585875687899247><:JPYNdisco:698471276498649168><:hello:699779689127870514>')
    
    if now == '05:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 200 ActiveUserOnly  ☔<:kenj:700136543003607101>')
        
    if now == '05:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/701765831268368474/701767323304067133/hty.png ')    
        
    if now == '06:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 30 ActiveUserOnly  <:rain:699585875687899247><:JPYNdisco:698471276498649168><:hello:699779689127870514>')
    
    if now == '06:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 77.7 ActiveUserOnly  <:rain:699585875687899247><:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>')   
   
    if now == '07:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 30 ActiveUserOnly  <:rain:699585875687899247><:JPYNdisco:698471276498649168> ')
  
    if now == '07:20':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:cafe:699769671234355230>Good morning 🌎everyone.<:gm:699792760651120671>Have a nice day today! [omikuji] or [fortune] ← for today is fortune🔮Command')

    if now == '07:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 77.7 ActiveUserOnly  <:good01:699581068285706301><:rain:699585875687899247><:BGPT02:698471366004965406> ') 

    if now == '08:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 35 ActiveUserOnly  <:rain:699585875687899247><:JPYNdisco:698471276498649168><:hello:699779689127870514>')
     
    if now == '08:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:suika_paku:699072728153587782> hungry! I want to eat meat again! Meat🥩, meat🍖, meat!🍗肉29coin?!hehe')    
    
    if now == '08:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw 29coin 146460 5 EquallyDistributed   🍖meat!meat!🍗Plz receive→/catch<:hai_kao:699072592987947117>29meat!肉！🥩')

    if now == '08:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥴💦Tummy full. ate too much. The meat is gone!🥩🥩🥩!Sorry..hehe..ww')
        
    if now == '08:46':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Plz.<:kanngaeru:699072662382837881>I am hungry again, so give me 【/tip 29coin *** @🌈Rains☔ 】[meatcoin]Tip🍖')
    
    if now == '08:47':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good01:699581068285706301> ☑🥩29coin tip please. If you tip 29coins of 10000 or 100000, in return, I will tip JPNY COIN for a while!【/tip 29coin <@700176826282147851>】')
      
    if now == '09:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767323304067133/hty.png ')

    if now == '09:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good:699580636448423936>Thank you!for the MeatCoin(29coin)Tip! I will eat meat again tomorrow.🍖<:ty:699857337980026930>')
        
    if now == '09:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 40 ActiveUserOnly  <:good01:699581068285706301><:rain:699585875687899247><:JPYNdisco:698471276498649168> ')
   
    if now == '09:55':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:niko_shita:699072695823892561>Plz.Meat.Meat.beef?pork?chicken?mutton?29Tip🍖')

    if now == '09:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767349828714606/hg.png ') 
        
    if now == '10:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:aloha:699581550777597992>Hello,how are you❓ ') 
        
    if now == '10:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here <:suika_paku:699072728153587782>After 2min, I”ll ☔Rain a little... ') 
     
    if now == '10:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767123252543498/iku.png') 
    
    if now == '10:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 150 ActiveUserOnly  <:good01:699581068285706301><:rain:699585875687899247><:BGPT02:698471366004965406>') 
     
    if now == '10:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BEN 300 6 EquallyDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>⚾Plz receive→/catch')
    
    if now == '10:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 120 6 EquallyDistributed  <:good01:699581068285706301><:JPYNdisco:698471276498649168> ⚾Plz receive☞/catch')  

    if now == '10:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 1200 8 EquallyDistributed  <:good01:699581068285706301><:BGPT02:698471366004965406><:BGPT02:698471366004965406><:BGPT02:698471366004965406>Plz receive→/catch')
    
    if now == '10:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:cya:699859096794562650>👆/catch') 
        
    if now == '10:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/701765831268368474/701767323304067133/hty.png ')          
      
    if now == '11:24':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('👆/catch? <:heart02:699580174911668225>See you sometimes!<:star1:699582964853375018>')    
        
    if now == '11:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 200 ActiveUserOnly  ☔<:kenj:700136543003607101><:sangras01:699579409220370514>')
        
    if now == '11:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('How are UZURAS Wallet doing Now～!?　<:uzu2:700858786960900117>...⚡...<:uzu1:700858878879072303>‼Sorry!') 
    
    if now == '12:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone <:hello:699779689127870514>Rain<:rain:699585875687899247>is 1min later.<:good01:699581068285706301>')  

    if now == '12:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 200 ActiveUserOnly  <:rain:699585875687899247><:JPYNdisco:698471276498649168> ')

    if now == '12:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 777.77 ActiveUserOnly  <:rain:699585875687899247><:BGPT02:698471366004965406>')

    if now == '12:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 500 ActiveUserOnly  <:rain:699585875687899247><:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833> ')

    if now == '12:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 120 4 EquallyDistributed  <:JPYNdisco:698471276498649168> ⚾Plz receive☞/catch') 
    
    if now == '12:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good01:699581068285706301><:cya:699859096794562650> ') 
    
    if now == '12:39':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good01:699581068285706301> ☑🥩29coin tip please. If you tip 29coins of 10000 or 100000, in return, I will tip JPNY COIN for a while!【/tip 29coin <@700176826282147851>】I want to eat my meat🍖')
      
    if now == '13:14':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701775150743289956/migi.png ')    
   
    if now == '13:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone 👆/catch ok?<:heart02:699580174911668225>see you!<:star1:699582964853375018>')  
        
    if now == '13:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701775150743289956/migi.png ')    
        
    if now == '13:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here もうJapanでは深夜就寝前💤?ですよね。todayもあと少しだけRainします。Hello!Rain☔ is 1min later. ')       
        
    if now == '13:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767349828714606/hg.png')
    
    if now == '13:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 300 ActiveUserOnly  <:rain:699585875687899247><:good:699580636448423936> <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833> ')
    
    if now == '13:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 777.77 ActiveUserOnly  <:rain:699585875687899247><:BGPT02:698471366004965406>')
    
    if now == '13:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here <:zzz:699581950356226058><:gn:699792795363311676> JapanのEveryoneはそろそろGoodNight！☔is 30min later👋 コロナには気を付けて！<:corona:699588627868418070>Watch out for corona!→ #┃covid-19🦠news ')       
       
    if now == '13:41':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/701765831268368474/701767323304067133/hty.png ')    

    if now == '13:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hai_kao:699072592987947117><:hai_kao:699072592987947117><:hai_kao:699072592987947117>   ')      
        
    if now == '14:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 10 ActiveUserOnly  <:good01:699581068285706301><:rain:699585875687899247><:JPYNdisco:698471276498649168><:gn:699792795363311676> ')  

    if now == '14:13':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 80 4 EquallyDistributed  <:JPYNdisco:698471276498649168> ⚾Plz receive→/catch') 
   
    if now == '14:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BEN 310.8 4 EquallyDistributed  <:benkeicoinsl:698471387064696833>  ⚾Plz receive→/catch')      
    
    if now == '14:17':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw KENJ 800 4 EquallyDistributed  <:kenj:700136543003607101> ⚾Plz receive→/catch')
        
    if now == '14:19':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:bye:699863270802325604>See you! ') 
        
    if now == '15:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here 👆/catch?<:aloha:699581550777597992> ') 
        
    if now == '15:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 50 ActiveUserOnly  <:good01:699581068285706301><:BGPT02:698471366004965406> <:rain:699585875687899247><:gn:699792795363311676> ')
  
    if now == '15:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701775150743289956/migi.png ') 

    if now == '16:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 50 ActiveUserOnly  ☔<:kenj:700136543003607101> ')
        
    if now == '16:55':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 77.7 ActiveUserOnly  <:rain:699585875687899247><:BGPT02:698471366004965406>')   
        
    if now == '17:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 10 ActiveUserOnly  <:good01:699581068285706301>🌈<:JPYNdisco:698471276498649168><:rain:699585875687899247>')
    
    if now == '18:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 50 ActiveUserOnly  ☔<:kenj:700136543003607101> ')
        
    if now == '18:47':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701775150743289956/migi.png ') 
    
    if now == '19:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 5 ActiveUserOnly  <:BENKEICOIN04:698471407650209832><:good01:699581068285706301><:rain:699585875687899247> ')  

    if now == '20:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 5 ActiveUserOnly  🌈 <:JPYNdisco:698471276498649168> ') 
          
    if now == '21:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/701765831268368474/701767349828714606/hg.png ')

    if now == '21:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 50 ActiveUserOnly  <:good01:699581068285706301><:BGPT02:698471366004965406> <:rain:699585875687899247>')  
        
    if now == '22:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 20 ActiveUserOnly  <:good01:699581068285706301>🌈<:JPYNdisco:698471276498649168>HelloAll⭐')
   
    if now == '22:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Dear japanese<:cafe:699769671234355230>Everyone🌟おはようございます!<:gm:699792760651120671> Have a nice day today！【おみくじ】←で運勢を')

    if now == '23:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 20 ActiveUserOnly  <:good01:699581068285706301>🌈<:JPYNdisco:698471276498649168>HelloAll⭐')        
    
    if now == '23:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 50 ActiveUserOnly  <:good01:699581068285706301>🌈<:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833> HelloAll⭐')
    
    if now == '23:58':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 20 ActiveUserOnly  <:good01:699581068285706301>🌈<:JPYNdisco:698471276498649168>HelloAll⭐')
  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
