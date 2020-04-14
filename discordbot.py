from discord.ext import commands
import os
import traceback
import discord
import random  # おみくじで使用

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()  # 接続に使用するオブジェクト


@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "goodmorning":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん Good morning")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "goodnight":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん Good Night! Go to bed early♡")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "おはよう":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん ☆おはようございます☆")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "goodevening":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん　Good evening～☆" )  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "BENKEIS":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さんと一緒に ☆༺.Benkeis now!.༻ ༒ⷬⷬeSports༒ⷬⷬ GameON!☆")  # f文字列（フォーマット済み文字列リテラル）
 
    if message.content == "こんにちは":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん こんにちは☺️楽しんで！")  # f文字列（フォーマット済み文字列リテラル）


    if message.content == "こんばんは":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん こんばんは😃🌃早く休みましょう🎵")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "おはよー":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん GoodMorning♡")  # f文字列（フォーマット済み文字列リテラル）

       
    elif message.content == "hi":
        # リアクションアイコンを付けたい
        q = await message.channel.send("Are you a cryptocurrency fan?")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

                
    elif message.content == "質問":
        # リアクションアイコンを付けたい
        q = await message.channel.send("あなたはeSpotsTeam所属していますか？")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
        
    elif message.content == "accept":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /accept 🔑")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

                
    elif message.content == "help":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /help ←Uzuras Wallet Help")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

        
    elif message.content == "info":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben 残高")
        [await q.add_reaction(i) for i in ('↺', '↷')]  # for文の内包表記

        
    elif message.content == "rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain ben 5 ActiveUserOnly ☔Rainを降らします")
        [await q.add_reaction(i) for i in ('☔', '⛈')]  # for文の内包表記

        
    elif message.content == "tip":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip ben 1 "f"{message.author.mention}さん にTip＄を送りました")
        [await q.add_reaction(i) for i in ('⭕', '☺')]  # for文の内包表記
  

    elif message.content == "throw":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw ben 2 2 EquallyDistributed ☞/catchで受け取ってください⚾")
        [await q.add_reaction(i) for i in ('⚾', '✋')]  # for文の内包表記


    elif message.content == "/tip":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip JPYN 1 "f"{message.author.mention}さん にTip＄を送りました")
        [await q.add_reaction(i) for i in ('⭕', '☺')]  # for文の内包表記


    elif message.content == "/info":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip bgpt 5 "f"{message.author.mention}さん にTip＄を送りました")
        [await q.add_reaction(i) for i in ('⭕', '☺')]  # for文の内包表記


    elif message.content == "/rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain jpyn 5 ActiveUserOnly ☔Rainを降らします")
        [await q.add_reaction(i) for i in ('☔', '⛈')]  # for文の内包表記


    elif message.content == "balance":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn ←Fill in this balance")
        [await q.add_reaction(i) for i in ('↺', '↷')]  # for文の内包表記


    elif message.content == "bad":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 931 "f"{message.author.mention}さん にunkoTip＄を送りました")
        [await q.add_reaction(i) for i in ('⭕', '💩')]  # for文の内包表記


    elif message.content == "unko":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 931 "f"{message.author.mention}さん にunkoTip＄を送りました")
        [await q.add_reaction(i) for i in ('⭕', '💩')]  # for文の内包表記
        
        

    elif message.content == "おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[GAME運勢YourFortune] ",
                        value=random.choice(('☆☆彡超最高☆彡☆【何してもVeryGood!勝負に強い日です】','☆最高☆【チームに恵まれた日です。チャレンジしたら幸運を招きます☆彡】','やったね☆彡！【納得出来る日でしょう。金運は余り期待出来ないです。】'
                                             ,'大吉【☆☆☆自信もって取り組めば必ず好成果となって返ってきます。♡♡♡恋愛運は超ベリグっ】', '中吉【☆☆好チャンス！攻めて成果あり。♡♡とりあえず問題なしかな！？】', '小吉【☆☆通常のセオリーを変化させたら好成果となる。♡♡現状から変化ない】'
                                             ,  '末吉【☆☆参加型オンラインゲームで好成果あり♡ゲームばかりじゃダメ。出会いを求めて外にでたら吉あり】', '吉【☆現状変化なし♡特に変化なし。そのままやっとけ！】',  '吉【☆まぁ！こんなもんよ】'
                                             , 'ごく普通やね【何それ！？と思うだろうがごく普通だ！棚から牡丹餅はない】', '大凶【▲▲吐き気するわ！駄目だこりゃ】'
                                             , '凶【▲残念！好機はないね。負けも勝ちの内かと思え！】', '大凶【▲▲吐き気するわ！駄目だこりゃ】')), inline=False)
        await message.channel.send(embed=embed)


    elif message.content == "omikuji":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="☆OMIKUJI☆", description=f"{message.author.mention}Today!YourFortune!☆",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[Today!YourFortune!] ",
                        value=random.choice(('☆☆彡VeryVeryGood☆彡☆【Very Good! It ’s a very competitive day.】','☆VeryGoood!☆【It is a good day for the team. 】','Good☆彡！【It will be a convincing day. I can not expect much money.】'
                                             ,'VeryGood【☆☆☆If you work with confidence, you will always get good results. ♡♡♡ Love luck is super berig】', 'GoodDay【☆☆Good chance! There is a result of attacking. ♡♡ For the time being, there is no problem! ?】', 'Good!【☆☆ If you change the usual theory, you will get good results. ♡♡ No change from the current situation】'
                                             ,  'usuallyGood【☆☆Good results with participatory online games ♡ Not only games. Good luck if you go outside to meet】', 'good!【☆The current situation is unchanged ♡ No particular change Let it go！】',  'Good!【☆I do not need any advice】'
                                             , 'It is normal [What is that! ? You probably think that is normal! There is no peony mochi from the shelf', 'Great evil [Great evil [▲▲ I am nauseous!]'
                                             , 'Worst【▲Sorry! There is no opportunity. I think the loss is a win！】', 'Very worst!BAD【▲▲I m nauseous! Useless】')), inline=False)
        await message.channel.send(embed=embed)



    elif message.content == "!ダイレクトメッセージ":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さん Benkeis TwitchTV🎮 Followお願いね！ https://www.twitch.tv/benkeis ")


client.run(token)
