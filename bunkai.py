import discord
import os
import random
import unicodedata
import markovify
import MeCab
import csv

TOKEN = os.environ['DISCORD_BOT_TOKEN']
ls=[]
bc=0
test=0
pronum=0
client = discord.Client()
f=open ("history.csv" , "r" , encoding="utf_8")
reader = csv . reader ( f )
line = [row for row in reader]

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

def soinsu(x):
    r=list()
    now=2
    while x!=1:
        if(now*now>x):
            r.append(x)
            break
        if(x%now==0):
            r.append(now)
            x=x//now
        else:
            now+=1

    return r

@client.event
async def on_ready():
    print('AC')

@client.event
async def on_message(message):
    sentence=message.content
    if message.author.bot:
        return
    if message.author.bot:
        return
    if ('716349767348912128' in message.content)|('713286619611791471' in message.content):
        msg=""
        async for message in message.channel.history():
            if not message.author.bot:
                msg+="\n"+message.content
        parsed_text = MeCab.Tagger('-Owakati').parse(msg)
        # Build model
        parsed_text=parsed_text.replace('。', '.')
        parsed_text=parsed_text.replace('、', ',')
        parsed_text=parsed_text.replace(' , ', ',')
        parsed_text=parsed_text.replace(' .', '\n')
        parsed_text=parsed_text.replace('@', '')
        parsed_text=parsed_text.replace('<', '')
        parsed_text=parsed_text.replace('>', '')
        parsed_text=parsed_text.replace('!', '')
        text_model = markovify.NewlineText(parsed_text)
        t=text_model.make_sentence(tries=30)
        #print(t)
        if(t==None):
            await message.channel.send("素材不足...")
        else:
            t=t.replace(',', '、')
            t=t.replace('.', '。\n')
            t=t.replace(' ', '')
            await message.channel.send(t)
    if sentence.startswith("!totsu"):
        s=sentence[7:len(sentence)]
        sw=get_string_width(s)//2
        s="＿人"+"人"*sw+"人＿\n"+"＞　"+s+"　＜\n"+"  ￣Y"+"^Y"*sw+"￣  \nby"+message.author.name
        await message.channel.send(s)
        await message.delete()
    if sentence.startswith("!Help"):
        em = discord.Embed(title="素因数分解bot ver.1.2.3",color=0x00ffff)
        em.add_field(name="!bunkai *N*",value="*N*を素因数分解した結果を表示させる")
        em.add_field(name="!totsu *S*",value="*S*を角吹き出しで表示させる")
        em.add_field(name="!bc *L*",value="レベルが*L*の素因数分解の問題を出題，ans=で回答")
        em.add_field(name="!クイズ",value="主にテスト対策のクイズを出題，ans=で回答")
        await message.channel.send(embed=em)
    if ('歌って' in message.content):
        songs=["VICTORIA歌います。　サァウ↓ヴァ↑ｗｗｗ リィディアツャｗｗｗケィラァトォカｗｗｗマッジャラストゥ↑ｗｗｗファーレドォｗwｗｗｗ ラファランドゥｗｗｗオグゥトゥアｗｗｗルゥクィアロｗｗｗストォフィアァｗｗｗ ラグゥrｪフｧgarcんｗｗｗｗｗｗ","HARDCOREノ心得歌います。\n1にﾊｰｺｰ\n2にﾊｰｺｰ\n3,4がなくて\n鶏ガラSOOOOOOOOOOOOOOOUPｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ","おしゃま歌います。Lets 牛乳 Death!!ﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｯﾃﾞｯﾃﾞｯﾃﾞｯﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗﾃﾞｰﾝｗｗｗ(ヘドバン( ՞ةڼ◔)ヘドバン( ՞ةڼ◔))","Aleph-0歌います。ジャンｗｗﾃﾞﾚｯﾃｯﾃﾚｯﾃﾚｯﾃｯジャンジャンジャンジャンジャン↑ｗｗｗｗｗﾃﾞﾚｯﾃｯﾃﾚｯﾃﾚｯﾃｯジャンジャンジャンジャンジャン↑ｗｗｗｗデケデケデｗｗｗデケデケデｗｗｗｗデケデケデケデケｗｗｗｗ(temptation…)バババババババババbbb","大宇宙ステージ歌います。「俺　が　一　緒　に　い　て　や　る　か　ら　…　…　」ﾋﾟｭｰｰﾝｗｗｗﾋﾟｰｰｰｯｗｗｗｗﾃﾞｹﾃﾞｹｰｯﾃﾞｹﾃﾞｹｰｯピロリロリロピロリロリロロリロリロロロリロリロロリロリロロピロロロピロロロピロロロピロロロピロロロピロロロピロロロピロロロ","オォ UNDEAD HEARTｗｗｗｗｗ\nオォ UNDEAD HEART ｗｗｗｗｗ\nヽ( ˆᴗˆ )ﾉ ヽ( ˆᴗˆ )ﾉ ヽ( ˆᴗˆ )ﾉ  \n  　/  / 　　　/  / 　　　/  / 　　\n ノ😇ゝ　  ノ😇ゝ　 ノ😇ゝ","Garakuta Doll Play歌います。ｼｰｻﾞｰﾜｯﾄﾝｗｗｗｗｗｱﾝﾀﾞｽﾃｨｰﾝｗｗｗｗｗ(ｱｱｱｱｱｱｱｱ…)ｱｸｼﾌﾞｾｨｰﾃｨｰｗｗｗｵｯﾌﾞｯｼｯﾉｯ!ｗｗｗｗｱﾝﾀﾞｰｽﾃｨｰﾝ(ｱｰｰ…ｴﾌﾞﾘﾅ----","(´･_･`)＜レッツ牛乳death☆wwwwwwﾃｪﾝ↑ﾃｪﾝ↑ﾃｪﾝ↑ﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃﾃﾃﾃﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝﾃｪﾝwwwwｲﾖｫｰ↑↑↑レッツ牛乳death☆(以上繰り返し)","BATTLE NO.1 歌います。アモアモアモアモアアモオジィｫﾞｵﾞｨﾃﾞﾝﾃﾞﾝﾃﾞﾝﾃﾞﾃﾞﾃﾞﾝﾃﾞﾝ\ｱﾓｱﾓ（՞ټ՞☝/ﾃﾞﾝﾃﾞﾝﾃﾞｹﾚﾚ\ｧｱﾓｱﾓ（՞ټ՞;☝/レッツゴォォｵｯｵｯｵｯｵｯｵｯｵｯ…ﾄﾄﾄﾄﾀﾀﾀﾀﾀﾀ\ｱﾓオｩジィ/ｲﾞｴﾞ💪(´･_･`💪)","ᕕ(՞ةڼ◔)ᕗ⁾⁾クァ～ww⇊wユゥ～ン⇈wwwフィ～⇊ン↑↑マイ→ソォ～⇈wwウィンwwウォ↑↑www～ズwww₍₍ ᕕ(՞ةڼ◔)ᕗ⁾⁾wwwア～イ↑↑wwウォ～ンwwwトゥ↓wゴォw↑↑↑wwバットゥ⇊wwア～⇈ハァ～⇈ww₍₍ ᕕ(՞ةڼ◔)ᕗ⁾⁾","エレクリだーーー チャーーラーラーrーtrwrgwウィmrgtzbダツツダツツダツツダツツダツダツデツツデツツ","conflict歌います。ズォールヒ～～↑ｗｗｗｗヴィヤーンタースｗｗｗｗｗワース フェスツｗｗｗｗｗｗｗルオルｗｗｗｗｗプローイユクｗｗｗｗｗｗｗダルフェ スォーイヴォーｗｗｗｗｗスウェンネｗｗｗｗヤットゥ ヴ ヒェンヴガｒジョｊゴアｊガオガオッガｗｗｗじゃｇｊｊ","Cyaegha歌います。ユーアーレッシーwwwワイ↑レッスィ～ジャンwwwwwハィディングシーアンwwwwフィーリンエヴァァ↓ユーアーレッシーwwwワイ↑レッスィ～ジャンwwwwwリィンユァーハァゥアンwwwwwフィーリンバァヴィル↑www","インド人歌います。ｳﾞｪﾝｳﾞｪﾝｳﾞｪﾝｗｗｗｗｗｗｳﾞｪﾊﾊｳﾞｪｯﾊｳﾞｪﾝｗｗｗｗｗ(ﾊｯ!( ﾟдﾟ )彡)ｳﾞｪﾝｳﾞｪﾝｳﾞｪﾝｗｗｗｗｗｗｳﾞｪﾊﾊｳﾞｪｯﾊｳﾞｪﾝｗｗｗｗｗ(ﾊｯﾊ( -д- )彡)","BrainPower歌います。O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A- JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA","Garakuta Doll Play歌います。オーマイガーーーァァァァーーーーァァーーーァｗｗｗｗｗｗｗｗｗｗｗｗｗオーマイガーーーァァァァーーァァーーーァｗｗｗｗｗｗｗｗｗｗｗオーマイガーーーァァァァーーァァーーァァーーーァｗｗｗｗｗｗｗｗｗｗｗｗｗｗ","Fracture Ray歌います。テケテケテケテケ…ア～ｱﾋｨｨｨ…ン～ｱﾋｨｨーｲｲｲ… テンテンテンテテテテテンテンテレレン… テンテレレン…テレレン… ｾﾌﾞﾝ…ｽｨｯｸｽ…ﾌｧｲ…ﾌｫｳ…ｽﾘｨ…ﾄｳｩ…ﾜﾝ（ﾃﾚﾃﾚﾚｰ）…ｾﾞﾛ… ドゥーンｗｗｗｗ","Second Heaven歌います。Countdown…8…　7…　6…　5…　4・3・2・1三↓倍↑アイスクリームｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ(ﾃｯﾃﾚﾚｯﾃﾚﾚｯﾃｯﾃｰｗｗｗｗ↓ﾃﾚﾚｯﾃﾚﾚｯﾃﾚﾚｰ↑ﾚｰ↑ﾚｰﾚｰｗｗｗ↓)×∞","QZKago Requiem歌います。テレレレレレン♪テレレレレレレレレ♪テレレレレレン♪テレレレレ♪　イスラム教ｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫｫォォォォォォォ(ﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞbｯｳﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞﾊﾞ)","Gleam stone歌います！ ワッソン👩‍🏭やっくん🙎システィー👉仮面ヾ(O¥O)ゞねびばり👇役者の👆ディープス🤚💂 (´･_･`)＜ササササ 溺れる審査員😱😭テケフォーはいプラ✡️ (´･_･`)＜ギャギャギャギャ ジョイァン💪ジャイアン💪"]
        await message.channel.send(random.choice(songs))
    
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

        if(len(prime)!=2 or pow[1]!=1):
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

    global ls
    global bc
    me=f'{message.author.mention}\n'
    if sentence.startswith("!bc "):
        n=int(sentence[4:len(sentence)])
        if(n>50):
            await message.channel.send(me+"The maximum level is 50. Please choice lower level.")
        else:
            m=random.randint(2**n,2**(n+1))
            ls=soinsu(m)
            await message.channel.send(me+"Level:"+str(n)+", Question:Prime factorization "+str(m))
            bc=1

    if bc and sentence.startswith("ans="):
        s=sentence[4:len(sentence)]
        lsa = [int(x.strip()) for x in s.split(',')]
        lsa.sort()
        bc=0
        if(lsa==ls):
            await message.channel.send(me+"correct!!")
        else:
            await message.channel.send(me+"WrongAnswer......   The ans is"+str(ls))
            
    global test
    global pronum
    if test==0 and (sentence.startswith("!クイズ") or sentence.startswith("！クイズ")):
        pronum=random.randint(1,len(line))
        test=1
        await message.channel.send("[問題]\n"+line[pronum][1])

    if test==1 and sentence.startswith("ans="):
        s=sentence[4:len(sentence)]
        test=0
        if(s==line[pronum][2]):
            await message.channel.send(me+"正解！　答えは"+str(line[pronum][2])+" "+str(line[pronum][3]))
        else:
            await message.channel.send(me+"残念！　答えは"+str(line[pronum][2])+" "+str(line[pronum][3]))

client.run(TOKEN)
