import discord
import random
import cv2
import math
import numpy as np
import requests
from discord.ext import commands
bot = commands.Bot(
    command_prefix="!",
    help_command=None)


# 自分のBotのアクセストークン
TOKEN = ''

# 接続に必要なオブジェクトを生成
client = discord.Client()



# 起動時に動作する処理
@client.event
async def on_ready():
    print("on_ready")
    print(client.user.name)  # Botの名前
    print(client.user.id)  # ID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')
    await client.change_presence(activity=discord.Game(name="?help"))


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # メッセージの本文が ?call だった場合
    if message.content == "?call":
        #チャンネルidを取得
        global channelid
        channelid = int(message.channel.id)
        # 送信するメッセージ
        channelName = message.channel
        content = "on ready `#%s`" % channelName
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)

    #help
    if message.content == "?help":
        await message.channel.send("?call :このコマンドで呼び出したチャンネルに画像を送るとランダムに処理して返信します\n?id :botが呼び出されたチャンネルか判定します。?call コマンドを使った後に必要があれば使ってください")
        
    #idをとったチャンネルを確認
    if message.content == "?id" and message.channel.id == channelid:
        await message.channel.send("呼び出されたチャンネルです")
    elif message.content == "?id":
        await message.channel.send("呼び出されたチャンネルではありません")

    ##
    if message.channel.id == channelid:

        # 送信者がbotである場合は弾く
        if message.author.bot:
            return 
        # ファイルがある場合
        if message.attachments:
            for attachment in message.attachments:
                # Attachmentの拡張子がpng, jpg, jpegのどれかだった場合
                if attachment.url.endswith(("png", "jpg", "jpeg")):
                    attachment = message.attachments[0]
                    # 送られてきたファイルをfileSrc.pngという名前で保存する
                    await attachment.save("fileSrc.png")
                    file_dst = "dst.png"
                    img_src = cv2.imread("fileSrc.png",1)

                    randomWord = [
                     "udrl","brg","bgr","rbg","gbr","grb","rrr","ggg","bbb","yuv","ycbcr","hsv","negaposi","brightness","contrastRed","contrastEnh","heikinnheikatu","Gaussianheikatu",
                     "bilateralheikatu","medianheikatu","Sobeledge","2ndder","sharpfilter",
                    ]#23処理

                    randomChoice = random.choice(randomWord)
                    
                    if randomChoice == "udrl":
                        #main 垂直反転
                        img_dst = cv2.flip(img_src,0)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("垂直反転")

                    elif randomChoice == "brg":
                        #main (R,G,B)→(B,R,G)
                        img_bgr = cv2.split(img_src)
                        img_dst = cv2.merge((img_bgr[2],img_bgr[0],img_bgr[1]))

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("(R,G,B)→(B,R,G)")
                    
                    elif randomChoice == "bgr":
                        #main (R,G,B)→(B,G,R)
                        img_bgr = cv2.split(img_src)
                        img_dst = cv2.merge((img_bgr[2],img_bgr[1],img_bgr[0]))

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("(R,G,B)→(B,G,R)")

                    elif randomChoice == "rbg":
                        #main (R,G,B)→(R,B,G)
                        img_bgr = cv2.split(img_src)
                        img_dst = cv2.merge((img_bgr[0],img_bgr[2],img_bgr[1]))

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("(R,G,B)→(R,B,G)")
                    
                    elif randomChoice == "gbr":
                        #main (R,G,B)→(G,B,R)
                        img_bgr = cv2.split(img_src)
                        img_dst = cv2.merge((img_bgr[1],img_bgr[2],img_bgr[0]))

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("(R,G,B)→(G,B,R)")

                    elif randomChoice == "grb":
                        #main (R,G,B)→(G,R,B)
                        img_bgr = cv2.split(img_src)
                        img_dst = cv2.merge((img_bgr[1],img_bgr[0],img_bgr[2]))

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("(R,G,B)→(G,R,B)")

                    elif randomChoice == "rrr":
                        #main (R,G,B)→(R,R,R)
                        img_bgr = cv2.split(img_src)
                        img_dst = cv2.merge((img_bgr[0],img_bgr[0],img_bgr[0]))

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("(R,G,B)→(R,R,R)")

                    elif randomChoice == "ggg":
                        #main (R,G,B)→(G,G,G)
                        img_bgr = cv2.split(img_src)
                        img_dst = cv2.merge((img_bgr[1],img_bgr[1],img_bgr[1]))

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("(R,G,B)→(G,G,G)")

                    elif randomChoice == "bbb":
                        #main (R,G,B)→(B,B,B)
                        img_bgr = cv2.split(img_src)
                        img_dst = cv2.merge((img_bgr[2],img_bgr[2],img_bgr[2]))

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("(R,G,B)→(B,B,B)")
                    
                    elif randomChoice == "yuv":
                        #main RGB to YUV
                        img_dst = cv2.cvtColor(img_src,cv2.COLOR_BGR2YUV)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("RGB→YUV")

                    elif randomChoice == "ycbcr":
                        #main RGB to YCbCr
                        img_dst = cv2.cvtColor(img_src,cv2.COLOR_BGR2YCrCb)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("RGB→YCbCr")

                    elif randomChoice == "hsv":
                        #main RGB to HSV
                        img_dst = cv2.cvtColor(img_src,cv2.COLOR_BGR2HSV)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("RGB→HSV")

                    elif randomChoice == "negaposi":
                        #main ネガポジ
                        img_dst = 255 - img_src

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("ネガポジ変換")

                    elif randomChoice == "brightness":
                        #main 明度調整
                        shift = 100
                        table = np.arange(256, dtype = np.uint8)
                        for i in range(0,255):
                            j = i + shift
                            if j < 0:
                                table[i] = 0
                            elif j > 255:
                                table[i] = 255
                            else:
                                table[i] = j

                        img_dst = cv2.LUT(img_src,table)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("明度調整")

                    elif randomChoice == "contrastRed":
                        #main コントラスト低減
                        min = 100
                        max = 200
                        table = np.arange(256, dtype = np.uint8)
                        for i in range(0,255):
                            table[i] = min + i * (max - min) /255

                        img_dst = cv2.LUT(img_src,table)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("コントラスト低減")

                    elif randomChoice == "contrastEnh":
                        #main コントラスト強調
                        min = 150
                        max = 200
                        table = np.arange(256, dtype = np.uint8)
                        for i in range(0,min):
                            table[i] = 0
                        for i in range(min,max):
                            table[i] = 255 * (i - min) / (max - min)
                        for i in range(max,255):
                            table[i] = 255

                        img_dst = cv2.LUT(img_src,table)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("コントラスト強調")

                    elif randomChoice == "heikinnheikatu":
                        #main 平滑化(平均化オペレータ)
                        img_dst = cv2.blur(img_src,(3,3))

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("平滑化(平均化オペレータ)")

                    elif randomChoice == "Gaussianheikatu":
                        #main 平滑化(Gaussianオペレータ)
                        img_dst = cv2.GaussianBlur(img_src,(11,11),1)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("平滑化(Gaussianオペレータ)")

                    elif randomChoice == "bilateralheikatu":
                        #main 平滑化(バイラテラルオペレータ)
                        img_dst = cv2.bilateralFilter(img_src,11,50,100)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("平滑化(バイラテラルオペレータ)")

                    elif randomChoice == "medianheikatu":
                        #main 平滑化(中央値フィルタ)
                        img_dst = cv2.medianBlur(img_src,9)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("平滑化(中央値フィルタ)")

                    elif randomChoice == "Sobeledge":
                        #main エッジ検出(Sobelオペレータ)
                        img_tmp = cv2.Sobel(img_src,cv2.CV_32F,1,0)
                        img_dst = cv2.convertScaleAbs(img_tmp)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("エッジ検出(Sobelオペレータ)")

                    elif randomChoice == "2ndder":
                        #main エッジ検出(2次微分オペレータ)
                        img_tmp = cv2.Laplacian(img_src,cv2.CV_32F,3)
                        img_dst = cv2.convertScaleAbs(img_tmp)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("エッジ検出(2次微分オペレータ)")

                    elif randomChoice == "sharpfilter":
                        #main 鮮鋭化フィルタ処理
                        k = 1.0
                        op = np.array([[-k,-k,      -k],
                                    [-k,1 + 8 * k,-k],
                                    [-k,-k,       -k]])

                        img_tmp = cv2.filter2D(img_src,-1,op)
                        img_dst = cv2.convertScaleAbs(img_tmp)

                        cv2.imwrite(file_dst,img_dst) #処理結果の保存
                        await message.channel.send(file=discord.File("dst.png"))
                        await message.channel.send("鮮鋭化フィルタ処理")

                    else:
                        await message.channel.send("ERROR")
        


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)