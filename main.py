import discord
import urllib3
import requests
import string
from bs4 import BeautifulSoup
import asyncio
import random
from sys import exit
from datetime import datetime

dt = datetime.now()
todayWeekDay = dt.weekday()
weekDayMemes = [['https://media.discordapp.net/attachments/1021784043475439646/1128666367269277696/monday-again.png?width=288&height=452'],
                ["It's **SF Tuesday** my dudes\nhttps://media.discordapp.net/attachments/1021784043475439646/1128671983614300180/ssrkz1wj0r6a1.png?width=380&height=452"],
                ['https://media.discordapp.net/attachments/1021784043475439646/1128655971175112804/B1fagUFqetA.png?width=558&height=452','https://cdn.discordapp.com/attachments/775022819419095073/1128666842123206717/VID_20230712_125115_831.mp4'],
                ['https://images-ext-2.discordapp.net/external/PCV9OeEDA2E8UBGlvjkVHQPKBp4TgghEHyWDHB6E_FQ/https/media.tenor.com/JTqpNH5os0sAAAPo/feliz-jueves-evangelion.mp4'],
                ["**GUILTY GEAR FRIDAY** LETS GOOOOOO\nhttps://images-ext-2.discordapp.net/external/rH_Fl9iMv6r0x6cMFjUUGjN-TlFBTnUzb8qZ2CkCgZY/https/media.tenor.com/ZfVs0i-79xoAAAPo/gay-tf2.mp4"],
                ["OHH SHIT IT'S **SAYA SATURDAY**\nhttps://media.discordapp.net/attachments/1021784043475439646/1128675372049907802/92q5s45jife71.png?width=485&height=452"],
                ["**РАМБЛ САНДЕЙ** NO WAY\nhttps://media.discordapp.net/attachments/1116001224257454100/1116001238962675734/IMG_20230416_112844.jpg?width=773&height=452"]]

#intbot = interactions.Client(token = 'MTAyMTY3MDYyNzg3MjA4Mzk4OA.GlGebR.BXn7UqfikcKIUj9Ss-lsn4gQVNp11nao24_ILc')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

http = urllib3.PoolManager()

# Ссылка
url = 'http://ratingupdate.info'
pcUrl = 'http://pc.ratingupdate.info'

# События
emojiDict = {
    0:'1️⃣',
    1:'2️⃣',
    2:'3️⃣',
    3:'4️⃣',
    4:'5️⃣',
    5:'6️⃣',
    6:'7️⃣',
    7:'8️⃣',
    8:'9️⃣',
    9:'🔟'
}

deadChatDict = {
    1: 'https://tenor.com/view/dead-chat-xd-dead-chat-gif-22992239',
    2: 'https://tenor.com/view/die-deadchat-gif-23050743',
    3: 'https://tenor.com/view/dead-chat-xd-fnaf-freddy-fredbear-golden-freddy-gif-24637349',
    4: 'https://tenor.com/view/me-when-dead-chat-lol-dead-group-chat-dead-chat-chat-dead-james-may-gif-25376040',
    5: 'https://tenor.com/view/dead-chat-xd-dead-chat-gif-22992239',
    6: 'https://tenor.com/view/dead-chat-gif-26094097',
    7: 'https://tenor.com/view/dead-chat-dead-chat-skeleton-gif-25954239'
}

isRealDict = {
    1: 'https://media.discordapp.net/attachments/775022819419095073/1025334547526717440/unknown.png?width=855&height=476',
    2: 'https://media.discordapp.net/attachments/775022819419095073/1025334547161808916/unknown.png?width=750&height=476',
    3: 'https://media.discordapp.net/attachments/775022819419095073/1025334546822086707/unknown.png',
    4: 'https://media.discordapp.net/attachments/775022819419095073/1025334725981786122/IMG_20220930_121339.jpg?width=1191&height=676'
}

timerTrue = False
# async def dead_chat(time):
#     timerTrue = True
#     now = datetime.datetime.now()
#     while(timerTrue):
#         time.sleep(3)
#         if (now+datetime.timedelta(hours = 2))<time:



timerActive = False



@client.event
async def on_ready():
    print('logged in as: {0.user}'.format(client))
    botchannel = client.get_channel(1025317152598798407)
    await botchannel.send('I am real')
    await botchannel.send('https://i.kym-cdn.com/entries/icons/original/000/040/491/cover10.jpg')
    #await schedule()
    await sendWeekMeme()
    await scheduleRandomPics()


async def sendWeekMeme():
    channel = client.get_channel(775022819419095073)
    print(weekDayMemes[todayWeekDay])
    weekFile = open("weekDay.txt","r+")
    line = weekFile.readline()
    if line == "":
        weekFile.write(str(todayWeekDay))
        await channel.send(random.choice(weekDayMemes[todayWeekDay]))
    elif int(line) != todayWeekDay:
        weekFile.seek(0)
        weekFile.truncate(0)
        weekFile.write(str(todayWeekDay))
        await channel.send(random.choice(weekDayMemes[todayWeekDay]))
    weekFile.close()

ftstplayers = []
ftxrdplayers = []
fttkplayers = []
ftsfplayers = []



async def nested():
    channel = client.get_channel(775022819419095073)
    await asyncio.sleep(3600)
    await channel.send(deadChatDict[random.randint(1,7)])
    #await channel.send('https://tenor.com/view/de-ad-ch-at-xd-chat-ded-dead-group-chat-ded-dead-gif-23993287')
    #return 0


async def schedule():
    global mytask
    mytask = asyncio.create_task(nested())
    #await mytask

link_list = [ #MEMES
    'https://media.discordapp.net/attachments/1021748045416767581/1072101307940339722/eZbk585BfMk.png?width=495&height=476',
    'https://media.discordapp.net/attachments/1021748045416767581/1072100462867775559/12ZB3mCkRXY.png?width=473&height=476',
    'https://cdn.discordapp.com/attachments/426418645514584065/1126895603239108668/ndgsvkcGtKU.png',
    'https://media.discordapp.net/attachments/1021748045416767581/1072100230385901609/uSGS9oqjX9k.png?width=450&height=476',
    'https://media.discordapp.net/attachments/1021748045416767581/1072100074391343124/iQI46jvdFt4.png?width=476&height=476',
    'https://media.discordapp.net/attachments/1021748045416767581/1072099775136153630/Jl_Gt2bfhrE.png?width=322&height=476',
    'https://media.discordapp.net/attachments/1021748045416767581/1071049478360010782/zAw3DviDob4.png?width=381&height=476',
    'https://tenor.com/view/i-juast-fartesd-gif-24048428',
    'https://i.redd.it/imyv8j0dxh0a1.png',
    'Рамсмертельной надо пахать в 10 раз больше чем обычному очередняре. Это невероятно сложно держать в голове какие у неё мечи есть посреди' + ' боя и это чудовищно загружает голову потому что от них зависят твои опции. Вам кажется она нечестной, но, поверьте мне, вас банально переигрывают, особенно на высоком уровне игры. Она честнейший персонаж, как бы дико это не звучало. Если вас побеждают, так сказать, "тупорылые" Рам ниже вас уровнем, то может стоить взглянуть на гайды',
    'https://i.redd.it/qpghyej02cf61.png',
    'https://media.discordapp.net/attachments/1021784043475439646/1128655210257076235/40mqiVwbz68.jpg?width=459&height=452',
    'https://media.discordapp.net/attachments/1021784043475439646/1128655295472730122/MEX2HjFwDZE.png?width=444&height=452',
    'https://media.discordapp.net/attachments/775022819419095073/1131607666712657940/szdbenXpab0.jpg?width=457&height=553',
    'https://media.discordapp.net/attachments/1087048541714784368/1131612329797230593/RDT_20230716_214601299533241364653395.jpg',
    'https://media.discordapp.net/attachments/1065740953551388704/1131613535449923594/image-96.png',
    'https://media.discordapp.net/attachments/806664976633823263/978760957826322472/mayy.gif',
    'https://media.discordapp.net/attachments/1131976841931005952/1131977021564670063/84grUC7dZ58.jpg',
    'https://sun9-48.userapi.com/impg/wLS12EK1Gpi8ZDuCo_zCFZeHOnkfs9Zrg2ir8g/D3JDsw0N048.jpg?size=634x667&quality=96&sign=d58f79534a418aa3b9b2159ffe11bc9a&type=album',
    'https://cdn.discordapp.com/attachments/775022819419095073/1132359298555596800/what-do-you-think-v0-7019v5k4yqcb1.png',
    'https://media.discordapp.net/attachments/775022819419095073/1132943360378818651/5hGaxIqFgc8.jpg',
    'https://media.discordapp.net/attachments/1078738136106025120/1132974499583758366/6RL4HPNCl14.jpg',
    'https://media.discordapp.net/attachments/775022819419095073/1134123577763958875/-rbNQDQnAno.jpg',
    'https://media.discordapp.net/attachments/775022819419095073/1136272823527161856/Video_by_Renous_Underground.mp4',
    'Если можно сказать так, то гг, по мне бг... Без обид, но давненько я с таким солнышком не играл. Одно дело 0 байкен, а другое ' + 'чел, который на другом конце монитора сидит, не ходит, а предвигается на j.Sах и Kabari бесконечно. И тычет всюду перри и 9236 нахуй Эс. нулевые игроки, они ставят нейтрал, окизиме, и смотрят ренджы кнопок своих. Ты даже близко не нулевой. Даже Солы в онлайне так не играют. Там есть проблески разума (иногда)....',
    'Микродаг, Снова сыграл с Ragna. Шли плавно, то я 2-1, то он 2-1, потом я накуралесил и слил 0-3, ну и хуй с ним. Все ещё не понимаю природу его банальных ошибок связанных с пониманием чара (Учитывая, что мы играем зеркало) и меня это все ещё бесит (Чувак, ну прошу, ну хватит активировать вортекс в '+ 'воздухе, ну это залупа иваныча пздц). Он будто сталкивается с ситуацией, в которой недоиграл, и забивает хуй на это, не открывая лабу, это меня разочаровывает в нём, хз, хочет от него большего  .  Anyway, раз я могу брать у него игры, то скоро смогу ему и не проигрывать. (Ну а ещё вдруг в 3м сезоне он наконец откроет лабу и разъебашит всех, кто знает)?',
    'https://cdn.discordapp.com/attachments/207546157348421633/1138919975223050350/IMG_20230809_224010_223.mp4',
    'https://cdn.discordapp.com/attachments/1135683630442750126/1139884742800576592/9jjn86zty3hb1.png',
    'https://cdn.discordapp.com/attachments/207546157348421633/1141447173930750134/6725deaab2331e95.mp4',
    'https://media.discordapp.net/attachments/1025317152598798407/1141637325156274247/20230814_113716.png?width=375&height=267',
    'https://media.discordapp.net/attachments/571868027100856329/1141735365632335882/bS2WWrVlH78.webp?width=576&height=324',
    'https://cdn.discordapp.com/attachments/207546157348421633/1143639650603372606/the_circle_got_me_like.mp4',
    'https://cdn.discordapp.com/attachments/775022819419095073/1145304530930647080/zato_bros.mp4',
    'если вы найдёте рут лучше или стабильнее; Поздравляю(ебало.жпг)! Я всего-лишь пролабил и прооптимизировал этот рут насколько мог, возможно были допущенны ошибки но мне так похуй честное слово вы все бляди жмёте 3 кнопки в супер и пишите что типо играете на чаре я бля в ахуе с вас вы вообще тренинг мод открывали??? я сука захожу в селест и вижу как эти выродки 1к+ уровня комбят у меня ебало отваливается вы чё бля в файтинг играете или сука в песочке куличики блять строите такое ощущение что кроме меня на чаре какие-то 3ёх летние дегроды играют просто блять смотреть невозможно так что жрите что дают и не выёбывайтесь.',
    'https://media.discordapp.net/attachments/775022819419095073/1147951638837997739/crash_all.jpg?width=420&height=468',
    'https://cdn.discordapp.com/attachments/775022819419095073/1148024097167654912/Guilty-Gear-D098D0B3D180D18B-D098D0B3D180D0BED0B2D0BED0B9-D18ED0BCD0BED180-Guilty-Gear-Strive-7953492.png',
    'https://cdn.discordapp.com/attachments/775022819419095073/1148026610994393208/Anime--crossover-itsuka-neru-7937970.gif']

async def nestedRandomPics():
    channel = client.get_channel(775022819419095073)
    #channel = client.get_channel(1021748045416767581) #test channel
    await asyncio.sleep(300)
    timeFile = open("timeFile.txt","r+")
    line = timeFile.readline()
    if line == "":
        timeFile.write("0")
        timeFile.close()
        await scheduleRandomPics()
    elif int(line) < 34:
        timeFile.seek(0)
        timeFile.truncate(0)
        timeFile.write(str(int(line)+1))
        timeFile.close()
        await scheduleRandomPics()
    else:
        timeFile.seek(0)
        timeFile.truncate(0)
        timeFile.write("0")
        await channel.send(link_list[random.randint(0,len(link_list)-1)])
        if random.randint(1,10) < 4:
            await channel.send("Не забывайте отправлять свои мемы при помощи команды !sm :)")
        timeFile.close()
        await scheduleRandomPics()

async def scheduleRandomPics():
    rpTask = asyncio.create_task(nestedRandomPics())
    await rpTask



@client.event
async def on_message(message):
    print(str(message.author) + ": " + message.content)
    if message.author == client.user:
        return

    if message.content.lower().startswith('!sm'):
        mAuthor = message.author
        if message.content.replace('!sm', '').strip() == '':
            await message.reply("Неправильный формат мема/копипасты/гифки. Отправьте ссылку или текст.")
        else:
            MSfile = open('Meme_Suggestions.txt', 'a')
            MSfile.write(str(mAuthor) + " : " + message.content.replace('!sm', '') + "\n")
            MSfile.close()
            await message.reply("Спасибо за мем.")

    if message.content.lower().startswith("!meme"):
        timeFile = open("timeFile.txt", "w")
        timeFile.write("0")
        timeFile.close()
        await message.channel.send(link_list[random.randint(0, len(link_list) - 1)])


    if message.content.lower().startswith('!ru'):
        mAuthor = message.author
        print(str(message.author) + ' !ru')
        # await message.channel.send('Hello!')
        searchNameList = str(message.content).split(
        )  #str(message.content).replace('!RU', '').strip()
        nameskip = 0
        searchName = ''
        for item in searchNameList:
            if nameskip == 0:
                nameskip += 1
            else:
                searchName = searchName + ' ' + item
                searchName = searchName.strip()
        if len(searchNameList) == 1:
            await message.channel.send("Try using !RU Your_Nickname")
        else:
            print('Getting info for: ' + searchName)
            uPar = {'name': searchName}
            r = requests.get(url, params=uPar)
            # print(r.url)
            response = http.request('GET', r.url)
            soup = BeautifulSoup(response.data, features="html.parser")
            trThing = soup.find_all('tr')
            trList = []
            for data in trThing:
                trList.append(data)
            #print(trThing[1])
            skipIndex = 0
            playerNum = 1
            playerList = []
            playerNamesMessage = ""

            if len(trList) == 1:
                await message.channel.send(
                    "Nothing has been found by nickname {}".format(searchName))
            else:
                for data in trList:
                    if skipIndex == 0:
                        skipIndex += 1
                    elif playerNum <= 10:
                        dataString = str(data.text)
                        print(dataString)
                        name = dataString.splitlines()
                        playerNamesMessage = playerNamesMessage + "    {}.".format(playerNum) \
                                             + name[1] + '  |  ' \
                                             + name[len(name)-2] + '  |  ' + name[len(name)-3] + "\n"
                        # await message.channel.send("{}.".format(playerNum) + name[1])
                        # print("{}.".format(playerNum) + name[1])
                        playerList.append(name[1])
                        playerNum += 1
                bot_message = await message.reply('```autohotkey\nChoose the player you are searching for using reactions:\n' + playerNamesMessage + '```')
                # for key in emojiDict.keys():
                #     await bot_message.add_reaction(key)
                for x in range(playerNum-1):
                    #print(x)
                    await bot_message.add_reaction(emojiDict[x])


                @client.event
                async def on_reaction_add(reaction, user):
                    #print("Reaction happened")
                    if mAuthor == user:
                        if reaction.emoji in emojiDict.values():
                            #print('it is in values')
                            await bot_message.delete()
                            chosenPlayerNum = list(emojiDict.keys())[list(emojiDict.values()).index(reaction.emoji)]
                            playerSkip = chosenPlayerNum
                            trThing2 = soup.find('tr')
                            for x in range(playerSkip + 1):
                                trThing2 = trThing2.find_next_sibling()
                            aThing = trThing2.find_next(href=True)
                            pcPlayerUrl = pcUrl + aThing['href']
                            # await message.channel.send(pcPlayerUrl)

                            # Работа со страницей игрока
                            ppResponse = http.request('GET', pcPlayerUrl)
                            ppSoup = BeautifulSoup(ppResponse.data,
                                                   features="html.parser")

                            allh2thing = ppSoup.find_all('h2')
                            h2thing = allh2thing[1].get_text()
                            playerInfo = h2thing
                            playerInfoStringsList = playerInfo.splitlines()  # Строки с персом, рейтингом и топом персонажа
                            pInfoStr = ''
                            for item in playerInfoStringsList:
                                pInfoStr = pInfoStr + '\n' + '      ' + item.lstrip(
                                )
                            playerTopRating = ''
                            h4thing = ppSoup.find(
                                'h4')  # Searching for top rating
                            if h4thing is not None:
                                if 'Top rating' in h4thing.text:
                                    playerTopRatingList = h4thing.text.splitlines()
                                    for item in playerTopRatingList:
                                        playerTopRating = playerTopRating + '\n' + '      ' + item.lstrip(
                                        )

                                    h4thing2 = h4thing.find_next_sibling(
                                    )  # Searching for top defeated
                                    tdfList = h4thing2.text.splitlines(
                                    )  # Top defeated list
                                    tdf = tdfList[0] + '\n' + '      ' + tdfList[
                                        2] + tdfList[3] + '\n' + '      ' + tdfList[
                                            5].lstrip()
                                else:
                                    tdfList = h4thing.text.splitlines(
                                    )  # Top defeated list
                                    tdf = tdfList[0] + '\n' + '      ' + tdfList[2] + tdfList[3] + '\n' + '      ' + \
                                          tdfList[5].lstrip()
                            else:
                                tdf = ''
                                playerTopRating = ''

                            await message.reply(
                                '```autohotkey\nInformation for player{}:'.
                                format(playerList[chosenPlayerNum]).rstrip() +
                                '\n\n' + pInfoStr.lstrip() + '\n' +
                                playerTopRating.strip() + '\n' + tdf.lstrip() +
                                '\n\n' + '```' + pcPlayerUrl)
                            # print(h2thing.text, playerTopRating)


    #Матчмейкинг по страйву
    elif message.content.startswith('!ftst'):
        print(str(message.author) + ' ftst')
        if message.author in ftstplayers:
            ftstplayers.remove(message.author)
            await message.reply('Вы вышли из матчмейкинга GGST.')
        else:
            ftstplayers.append(message.author)
            await message.reply('Вы участвуете в матчмейкинге GGST.')

        if len(ftstplayers) == 2:
            await message.channel.send("<@" + str(ftstplayers[0].id) + "> " + "<@" + str(ftstplayers[1].id) + ">"
                                 + " быстро кабанчиком залетаем в Guilty Gear Strive!")
            ftstplayers.clear()

    elif message.content.startswith('!champions'):
        print(str(message.author) + ' !champions')
        curChamp = 'RashidBazooka'
        championsList = ['1. Flynn the best Axl main', '2. Raivin', '3. Flynn the best Axl main', '4. VoiD', '5. ???', '6. ???', '7. ???', '8. Tony Pancake', '9. Admiral', '10. Holy_Sun', '11. Songbird', '12. Holy_Sun', '13. Lemming', '14. Gerollld', '15. Peng', '16. Peng', '17. RashidBazooka', '18. Peng', '19. RashidBazooka']
        championsListString = ''
        for champion in championsList:
            championsListString = championsListString + champion + '\n'
        await message.reply('Текущий чемпион: {0} \n\nЗал почёта Rumble:\n'.format(curChamp) + championsListString)

    #XRD matchmaking
    elif message.content.startswith('!ftxrd'):
        print(str(message.author) + ' ftxrd')
        if message.author in ftxrdplayers:
            ftxrdplayers.remove(message.author)
            await message.reply('Вы вышли из матчмейкинга Xrd.')
        else:
            ftxrdplayers.append(message.author)
            await message.reply('Вы участвуете в матчмейкинге Xrd.')

        if len(ftxrdplayers) == 2:
            await message.channel.send("<@" + str(ftxrdplayers[0].id) + "> " + "<@" + str(ftxrdplayers[1].id) + ">"
                                 + " быстро кабанчиком залетаем в Guilty Gear Xrd!")
            ftxrdplayers.clear()

    elif message.content.startswith('!fttk'):
        print(str(message.author) + ' fttk')
        if message.author in fttkplayers:
            fttkplayers.remove(message.author)
            await message.reply('Вы вышли из матчмейкинга Tekken.')
        else:
            fttkplayers.append(message.author)
            await message.reply('Вы участвуете в матчмейкинге Tekken.')

        if len(fttkplayers) == 2:
            await message.channel.send("<@" + str(fttkplayers[0].id) + "> " + "<@" + str(fttkplayers[1].id) + ">"
                                 + " быстро кабанчиком залетаем в Tekken!")
            fttkplayers.clear()

    elif message.content.startswith('!ftsf'):
        print(str(message.author) + ' ftsf')
        if message.author in ftsfplayers:
            ftsfplayers.remove(message.author)
            await message.reply('Вы вышли из матчмейкинга SFV.')
        else:
            ftsfplayers.append(message.author)
            await message.reply('Вы участвуете в матчмейкинге SFV.')

        if len(ftsfplayers) == 2:
            await message.channel.send("<@" + str(ftsfplayers[0].id) + "> " + "<@" + str(ftsfplayers[1].id) + ">"
                                 + " быстро кабанчиком залетаем в SFV!")
            ftsfplayers.clear()

    elif 'морбинг' in message.content.lower():
        print('Morbin happened')
        try:
            await message.add_reaction("<:morbin:981132826151878666>")
        except:
            return

    elif 'жопа' in message.content.lower():
        print('жопа happened')
        try:
            await message.add_reaction("<:jopik:971485582603718666>")
        except:
            return

    elif 'is real' in message.content.lower():
        print(str(message.author) + ' is real')
        await message.channel.send('*`Can we get much higher? So high...`*')
        await message.channel.send(isRealDict[random.randint(1,4)])

    elif message.content.startswith('!eng'):
        print(str(message.author) + ' !eng')
        await message.reply('https://sun9-48.userapi.com/impg/c857736/v857736574/1edcf9/Wn5tik8AkkA.jpg?size=604x360&quality=96&sign=72b4897889d708d9b499c484ae7c6ee3&type=album')

    elif message.content.startswith('!help'):
        await message.author.send('`Доступные команды:\n'
                                  '        1. !ru Nickname - Информация об игроке с сайта RatingUpdate.\n'
                                  '        2. !ftst, !ftsf, !ftxrd, !fttk - Матчмейкинг по GGST, SFV, GGXrd и Tekken соответственно.\n'
                                  '        3. !eng - АХАХАХХАХАХАХАХАХА\nТакже попробуйте "жопа" и "морбинг".`')
    # elif message.content.startswith("фак"):
    #     if len(str(message.content).split()) <= 3 and str(message.content).split()[0] == 'фак':
    #         await message.channel.send(message.content)
        #print(len(message.content))

    elif message.content.startswith('!saya'):
        print(str(message.author) + ' !saya')
        await message.channel.send('https://www.youtube.com/watch?v=TUACIEsVDw4')

    elif 'obamna' in message.content.lower() or 'обамна' in message.content.lower():
        print(str(message.author) + ' obamna')
        await message.channel.send('SODA🥤‼️😄😄🥶')
        await message.channel.send('https://media.discordapp.net/attachments/950477231686312007/1030063074549440552/unknown.png')

    elif len(message.content) > 500:
        print(str(message.author) + ' cant see')
        await message.channel.send('https://cdn.discordapp.com/attachments/908963388950990889/1148892101828947980/Zato_and_Eddie_Cant_Read.mp4')
    elif 'sus' in message.content.lower():
        print(str(message.author) + ' sus')
        susMes = str(message.content.lower()).replace('sus', '***SUS***')
        await message.channel.send(susMes)
        await message.channel.send('https://tenor.com/view/rock-one-eyebrow-raised-rock-staring-the-rock-gif-22113367')
    #if message.channel == client.get_channel(775022819419095073):
        #mytask.cancel()
        #await schedule()
    elif 'https://tenor.com/view/guh-jarvid-send-the-guh-cat-gif-and-then-say-guh-the-gary-does-sales-amogus-sstesla-gif-25370427' in message.content or 'guh' in message.content.lower():
        guh_links = ['https://tenor.com/view/guh-cat-stoned-stoned-cat-gif-25615600',
                     'https://media.discordapp.net/attachments/887072103831076874/1064850124574048297/5985F033-9BBC-4311-89D4-BF1B66729A85.gif?width=528&height=554',
                     'https://tenor.com/view/guh-guh-cat-cat-gif-24943124']
        await message.channel.send(guh_links[random.randint(0, len(guh_links) - 1)])

    elif '<@1021670627872083988>' in message.content:
        await message.channel.send('https://tenor.com/view/who-pinged-me-ping-discord-up-opening-door-gif-20065356')

    elif message.content.lower().startswith('микродаг,') or ', микродаг' in message.content.lower():
        print(str(message.author) + ' пишет микродагу')
        curse_list = ['пошел нахуй','иди нахуй','иди нахер','ты тварь','ты тупой','ты даун','ты пидорас', 'иди нах','ты лох']
        admiral_curse = ['адмирал лох', 'адмирал даун', 'адмирал ебан', 'адмирал тупой', 'адмирал тварь']
        if 'монет' in message.content.lower():
            random_response = ['ЛЕТС ГООООО','Уже тут как тут!', 'Как скажете!']
            coin_result = ['Орёл!', 'Решка!']
            await message.channel.send(random_response[random.randint(0,2)])
            await asyncio.sleep(3)
            await message.reply(coin_result[random.randint(0,1)])
        elif any(curse in message.content.lower() for curse in admiral_curse):
            await message.reply('https://www.youtube.com/watch?v=NpkxThe121Y')

        elif any(curse in message.content.lower() for curse in curse_list):
            await message.reply('https://tenor.com/view/jackass-3d-couch-explosion-gif-25176966')

        elif 'привет' in message.content.lower():
            hello_links = ['https://tenor.com/view/miku-bestie-hi-hello-hi-bestie-gif-22693513']
            await message.reply(hello_links[random.randint(0,len(hello_links)-1)])
        elif 'заложник' in message.content.lower():
            await message.channel.send('https://i.ytimg.com/vi/dnHQn_mpDpk/maxresdefault.jpg')
        elif '?' in message.content:
            if 'или' in message.content.lower():
                message_content = message.content.split()
                await message.channel.send(random.choice([message_content[message_content.index('или')-1], message_content[message_content.index('или')+1]]).translate(str.maketrans('', '', string.punctuation))) #first argument - what to substitute, 2nd - what to substitute with, 3rd - what to remove altogether
            elif 'как тебе' in message.content.lower():
                random_wdyt = ['Мне нравится', 'убого', 'мне не оч', 'не нравится', 'херово', 'круто', 'до жопы круто', 'пофигу как-то']
                await message.channel.send(random_wdyt[random.randint(0, len(random_wdyt) - 1)])
            elif 'почему' in message.content.lower():
                random_why = ['Ну вот как есть уж, ничего не поделать', 'А я откуда знаю', 'Потому что жопа','Потому что дост на миллии','ля ну ты задолбал уже со своими вопросами']
                await message.channel.send(random_why[random.randint(0, len(random_why) - 1)])
            elif 'зачем' in message.content.lower():
                random_fw = ['Кто знает', 'Спроси у кого получше', 'чтобы ты спросил', 'чтобы уничтожить мировую экономику', 'чтобы выучить матчап с ХХ']
                await message.channel.send(random_fw[random.randint(0, len(random_fw) - 1)])
            elif 'кто' in message.content.lower():
                author_nickname = str(message.author)[:-2]
                random_who = ['Дайсуке', 'Райан Гослинг', author_nickname, 'Сая', 'мой создатель', 'Адмирал', 'Дост', 'Серж', 'Номе']
                await message.channel.send(random_who[random.randint(0, len(random_who) - 1)])
            else:
                random_answer = ['Да','Нет!!!!!','100%','99999%','このメッセージを見れば、助けてください。明日提督は僕を殺すつもりだ。','0% шанс (невозможно)','конечно...', 'не знаю', 'иди нах', 'жопа', 'я на твои вопросы не отвечаю','ясно, этого в бан пожалуйста']
                await message.channel.send(random_answer[random.randint(0, len(random_answer)-1)])
        elif 'пасиб' in message.content.lower() or 'благодарю' in message.content.lower():
            await message.reply('https://tenor.com/view/whats-up-gif-meme-toy-story-whats-good-buzz-lightyear-gif-26344526')
        else:
            guh_links = ['https://tenor.com/view/guh-cat-stoned-stoned-cat-gif-25615600','https://media.discordapp.net/attachments/887072103831076874/1064850124574048297/5985F033-9BBC-4311-89D4-BF1B66729A85.gif?width=528&height=554','https://tenor.com/view/guh-guh-cat-cat-gif-24943124']
            await message.channel.send(guh_links[random.randint(0, len(guh_links)-1)])
    elif '!stop' in message.content.lower():
        await message.reply('*спасите..... умираю...... аххххххх.......*')
        await message.reply('https://tenor.com/view/gmod-ragdoll-video-game-video-game-gif-20573521')

        exit(str(message.author) + ' прожал стоп-кран')
    elif '!fullstop' in message.content.lower():
        exit(str(message.author) + ' прожал мега-стоп-кран')



    #event_loop.run_until_complete(task)


        # await asyncio.sleep(5)
        # await channel.send('https://tenor.com/view/de-ad-ch-at-xd-chat-ded-dead-group-chat-ded-dead-gif-23993287')

    #await deadChat()


# TOKEN
token = ''
client.run(token)

