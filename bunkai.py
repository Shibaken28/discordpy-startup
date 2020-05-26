import discord
import os
import random

TOKEN = os.environ['DISCORD_BOT_TOKEN']


client = discord.Client()

def get_char_width(c):
    data = unicodedata.east_asian_width(c)
    if data == 'Na' or data == 'H':
        return 1
    return 2


def get_string_width(string):
    width = 0
    for c in string:
        width += get_char_width(c)
    return width

@client.event
async def on_ready():
    print('AC')

@client.event
async def on_message(message):
    sentence=message.content
    if message.author.bot:
        return
    
    if sentence.startswith("!totsu"):
        s=sentence[7:len(sentence)]
        sw=get_string_width(s)//2
        s="＿人"+"人"*sw+"人＿\n"+"＞　"+s+"　＜\n"+"  ￣Y"+"^Y"*sw+"￣  "
        await message.channel.send(s)
    if sentence.startswith("!help"):
        em = discord.Embed(title="素因数分解bot ver.1.1.4",color=0x00ffff)
        em.add_field(name="!bunkai *N*",value="*N*を素因数分解した結果を表示させる")
        em.add_field(name="!totsu *S*",value="*S*を角吹き出しで表示させる")
        await message.channel.send(embed=em)
    if ('TINTIN' in message.content) or ('おっぱい' in message.content) or ('ちんちん' in message.content) or ('ero' in message.content)or ('Ero' in message.content)or ('エロ' in message.content):
        file_img = discord.File("partyParrot.gif")
        await message.channel.send(file=file_img)
    if 'おはよう' in message.content:
        m = "おはようございます，" + message.author.name + "さん！"
        await message.channel.send(m)
    if 'ZAP' in message.content:
        m = "＿人人人人人人人人＿\n＞　 突然のZAP　 ＜\n￣Y^Y^Y^Y^Y^Y^Y￣"
        await message.channel.send(m)
    if '死' in message.content:
        m = "＿人人人人人人＿\n＞　突然の死　＜\n￣Y^Y^Y^Y^Y￣"
        await message.channel.send(m)
    if 'おやすみ' in message.content:
        m = "おやすみなさい，" + message.author.name + "さん...zzz"
        await message.channel.send(m)
    if ('歌って' in message.content):
        songs=["HARDCOREノ心得歌います。\n1にﾊｰｺｰ\n2にﾊｰｺｰ\n3,4がなくて\n鶏ガラSOOOOOOOOOOOOOOOUPｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ","おしゃま歌います。Lets 牛乳 Death!!ﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｯﾃﾞｯﾃﾞｯﾃﾞｯﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗ(ヘドバン( ՞ةڼ◔)ヘドバン( ՞ةڼ◔))","Aleph-0歌います。ジャンｗｗﾃﾞﾚｯﾃｯﾃﾚｯﾃﾚｯﾃｯジャンジャンジャンジャンジャン↑ｗｗｗｗｗﾃﾞﾚｯﾃｯﾃﾚｯﾃﾚｯﾃｯジャンジャンジャンジャンジャン↑ｗｗｗｗデケデケデｗｗｗデケデケデｗｗｗｗデケデケデケデケｗｗｗｗ(temptation…)バババババババババbbb","大宇宙ステージ歌います。「俺　が　一　緒　に　い　て　や　る　か　ら　…　…　」ﾋﾟｭｰｰﾝｗｗｗﾋﾟｰｰｰｯｗｗｗｗﾃﾞｹﾃﾞｹｰｯﾃﾞｹﾃﾞｹｰｯピロリロリロピロリロリロロリロリロロロリロリロロリロリロロピロロロピロロロピロロロピロロロピロロロピロロロピロロロピロロロ","オォ UNDEAD HEARTｗｗｗｗｗ\nオォ UNDEAD HEART ｗｗｗｗｗ\nヽ( ˆᴗˆ )ﾉ ヽ( ˆᴗˆ )ﾉ ヽ( ˆᴗˆ )ﾉ  \n  　/  / 　　　/  / 　　　/  / 　　\n ノ😇ゝ　  ノ😇ゝ　 ノ😇ゝ","Garakuta Doll Play歌います。ｼｰｻﾞｰﾜｯﾄﾝｗｗｗｗｗｱﾝﾀﾞｽﾃｨｰﾝｗｗｗｗｗ(ｱｱｱｱｱｱｱｱ…)ｱｸｼﾌﾞｾｨｰﾃｨｰｗｗｗｵｯﾌﾞｯｼｯﾉｯ!ｗｗｗｗｱﾝﾀﾞｰｽﾃｨｰﾝ(ｱｰｰ…ｴﾌﾞﾘﾅ----","(´･_･`)＜レッツ牛乳death☆wwwwwwﾃｪﾝ↑ﾃｪﾝ↑ﾃｪﾝ↑ﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃﾃﾃﾃﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝwwwwｲﾖｫｰ↑↑↑レッツ牛乳death☆(以上繰り返し)","BATTLE NO.1 歌います。アモアモアモアモアアモオジィｫﾞｵﾞｨﾃﾞﾝﾃﾞﾝﾃﾞﾝﾃﾞﾃﾞﾃﾞﾝﾃﾞﾝ\ｱﾓｱﾓ（՞ټ՞☝/ﾃﾞﾝﾃﾞﾝﾃﾞｹﾚﾚ\ｧｱﾓｱﾓ（՞ټ՞;☝/レッツゴォォｵｯｵｯｵｯｵｯｵｯｵｯ…ﾄﾄﾄﾄﾀﾀﾀﾀﾀﾀ\ｱﾓオｩジィ/ｲﾞｴﾞ💪(´･_･`💪)","ᕕ(՞ةڼ◔)ᕗ⁾⁾クァ～ww⇊wユゥ～ン⇈wwwフィ～⇊ン↑↑マイ→ソォ～⇈wwウィンwwウォ↑↑www～ズwww₍₍ ᕕ(՞ةڼ◔)ᕗ⁾⁾wwwア～イ↑↑wwウォ～ンwwwトゥ↓wゴォw↑↑↑wwバットゥ⇊wwア～⇈ハァ～⇈ww₍₍ ᕕ(՞ةڼ◔)ᕗ⁾⁾","エレクリだーーー チャーーラーラーrーtrwrgwウィmrgtzbダツツダツツダツツダツツダツダツデツツデツツ","conflict歌います。ズォールヒ～～↑ｗｗｗｗヴィヤーンタースｗｗｗｗｗワース フェスツｗｗｗｗｗｗｗルオルｗｗｗｗｗプローイユクｗｗｗｗｗｗｗダルフェ スォーイヴォーｗｗｗｗｗスウェンネｗｗｗｗヤットゥ ヴ ヒェンヴガｒジョｊゴアｊガオガオッガｗｗｗじゃｇｊｊ","Cyaegha歌います。ユーアーレッシーwwwワイ↑レッスィ～ジャンwwwwwハィディングシーアンwwwwフィーリンエヴァァ↓ユーアーレッシーwwwワイ↑レッスィ～ジャンwwwwwリィンユァーハァゥアンwwwwwフィーリンバァヴィル↑www","インド人歌います。ｳﾞｪﾝｳﾞｪﾝｳﾞｪﾝｗｗｗｗｗｗｳﾞｪﾊﾊｳﾞｪｯﾊｳﾞｪﾝｗｗｗｗｗ(ﾊｯ!( ﾟдﾟ )彡)ｳﾞｪﾝｳﾞｪﾝｳﾞｪﾝｗｗｗｗｗｗｳﾞｪﾊﾊｳﾞｪｯﾊｳﾞｪﾝｗｗｗｗｗ(ﾊｯﾊ( -д- )彡)","BrainPower歌います。O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A- JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA","Garakuta Doll Play歌います。オーマイガーーーァァァァーーーーァァーーーァｗｗｗｗｗｗｗｗｗｗｗｗｗオーマイガーーーァァァァーーァァーーーァｗｗｗｗｗｗｗｗｗｗｗオーマイガーーーァァァァーーァァーーァァーーーァｗｗｗｗｗｗｗｗｗｗｗｗｗｗ","Fracture Ray歌います。テケテケテケテケ…ア～ｱﾋｨｨｨ…ン～ｱﾋｨｨーｲｲｲ… テンテンテンテテテテテンテンテレレン… テンテレレン…テレレン… ｾﾌﾞﾝ…ｽｨｯｸｽ…ﾌｧｲ…ﾌｫｳ…ｽﾘｨ…ﾄｳｩ…ﾜﾝ（ﾃﾚﾃﾚﾚｰ）…ｾﾞﾛ… ドゥーンｗｗｗｗ","Second Heaven歌います。Countdown…8…　7…　6…　5…　4・3・2・1三↓倍↑アイスクリームｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ(ﾃｯﾃﾚﾚｯﾃﾚﾚｯﾃｯﾃｰｗｗｗｗ↓ﾃﾚﾚｯﾃﾚﾚｯﾃﾚﾚｰ↑ﾚｰ↑ﾚｰﾚｰｗｗｗ↓)×∞","QZKago Requiem歌います。テレレレレレン♪テレレレレレレレレ♪テレレレレレン♪テレレレレ♪　イスラム教ｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫォォォォォォォ(ﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞbｯｳﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞ)","Gleam stone歌います！ ワッソン👩‍🏭やっくん🙎システィー👉仮面ヾ(O¥O)ゞねびばり👇役者の👆ディープス🤚💂 (´･_･`)＜ササササ 溺れる審査員😱😭テケフォーはいプラ✡️ (´･_･`)＜ギャギャギャギャ ジョイァン💪ジャイアン💪"]
        await message.channel.send(random.choice(songs))
    if '!neko' in message.content:
        await message.channel.send('にゃーん')
    
    if sentence.startswith("!roll "):
        d=int(sentence[6:len(sentence)])

    if sentence.startswith("!bunkai "):
        n=int(sentence[8:len(sentence)])
        sn=n
        prime=[-1]
        pow=[-1]
        kind=0
        now=2
        if(len(str(n))>=2000):
            await message.channel.send("数が大きすぎます，1999桁まで入力可能です(それでもタイムアウトの可能性あり)")
            return
        if(n<=0):
            await message.channel.send("自然数を入力してね")
            return
        if(n==1):
            await message.channel.send("1は素数じゃないよ")
            return
        if(n==57):
            await message.channel.send("57は約数が4つある素数だよ")
            return
        
        while n!=1:
            if(now>=10000000):
                await message.channel.send("タイムアウト><")
                return
            if(n<now*now):
                if(n==prime[kind]):
                    pow[kind]+=1
                    break
                else:
                    prime.append(int(n))
                    pow.append(1)
                    break
            if(n%now==0):
                if(now==prime[kind]):
                    pow[kind]+=1
                else:
                    prime.append(int(now))
                    pow.append(1)
                    kind+=1
                n=int(int(n)//int(now))
                #await message.channel.send(str(now)+"で割ります")
                #await message.channel.send(str(n)+"になります")
                now=int(1)
            now+=int(1)

        output=f'{message.author.mention}\n'

        if(len(prime)!=2&&pow[1]!=1):
            output+=str(sn)+"="
            k=1
            for i in prime:
                if(i==-1):
                    continue
                add="^"+str(pow[k])
                if(pow[k]==1):
                    add=""
                output+=str(i)+add+"x"
                k+=1
            output=output[0:-1]
        else:
            output+=str(int(n))+"は素数です"

        await message.channel.send(output)

client.run(TOKEN)
