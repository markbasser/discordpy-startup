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

    if message.content == "眠たい":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん さっさと寝ましょうねzzz")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "疲れた":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん 身体を休めてくださいね♡")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "おはよう":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん ☆おはようございます☆")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "あげる":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さんから臭い雨が降る～これあげる～☆" )  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "BENKEIS":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さんと一緒に ☆༺.Benkeis now!.༻ ༒ⷬⷬeSports༒ⷬⷬ GameON!☆")  # f文字列（フォーマット済み文字列リテラル）
        
    elif message.content == "投票":
        # リアクションアイコンを付けたい
        q = await message.channel.send("あなたはゲーマーですか？")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

                
    elif message.content == "質問":
        # リアクションアイコンを付けたい
        q = await message.channel.send("あなたはeSpotsTeam所属していますか？")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
        

    elif message.content == "おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[GAME運勢] ",
                        value=random.choice(('☆☆彡超最高☆彡☆【何してもVeryGood!勝負に強い日です】','☆最高☆【チームに恵まれた日です。チャレンジしたら幸運を招きます☆彡】','やったね☆彡！【納得出来る日でしょう。金運は余り期待出来ないです。】'
                                             ,'大吉【☆☆☆自信もって取り組めば必ず好成果となって返ってきます。♡♡♡恋愛運は超ベリグっ】', '中吉【☆☆好チャンス！攻めて成果あり。♡♡とりあえず問題なしかな！？】', '小吉【☆☆通常のセオリーを変化させたら好成果となる。♡♡現状から変化ない】'
                                             ,  '末吉【☆☆参加型オンラインゲームで好成果あり♡ゲームばかりじゃダメ。出会いを求めて外にでたら吉あり】', '吉【☆現状変化なし♡特に変化なし。そのままやっとけ！】',  '吉【☆まぁ！こんなもんよ】'
                                             , 'ごく普通やね【何それ！？と思うだろうがごく普通だ！棚から牡丹餅はない】', '大凶【▲▲吐き気するわ！駄目だこりゃ】'
                                             , '凶【▲残念！好機はないね。負けも勝ちの内かと思え！】', '大凶【▲▲吐き気するわ！駄目だこりゃ】')), inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "!ダイレクトメッセージ":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんにダイレクトメッセージ")


client.run(token)
