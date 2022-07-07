# -*- coding: utf-8 -*-

from http import client
from multiprocessing.connection import answer_challenge
import random
import discord

client = discord.Client()


@client.event
async def on_ready():
    print("봇 구동 중")
    bar = discord.Game("영어 도와주기")
    await client.change_presence(status=discord.Status.online, activity=bar)


EnglishWord = {
    "fair": "공평한",
    "attempt": "시도",
    "merely": "한낱",
    "diversify": "다양화하다",
    "revolve": "돌다",
    "evolve": "진화하다",
    "accuse": "고발하다",
    "include": "포함하다",
    "exclude": "제외하다",
    "approach": "접근하다",
    "nervertheless": "그럼에도 불구하고",
    "reliable": "믿을수 있는",
    "promote": "증진하다",
    "adjust": "적응하다",
    "predict": "예언하다",
    "install": "설치하다",
    "alternative": "대안",
    "variable": "변하기 쉬운",
    "various": "여러가지의",
    "varied": "가지각색의",
    "appoint": "임명하다",
    "locate": "위치하다",
    "celebrity": "유명 인사",
    "hospitality": "환대",
    "hostility": "적의",
    "aware": "알아차린",
    "caution": "조심",
    "barrier": "장애",
    "anticipate": "예상하다",
    "breed": "번식하다",
    "commit": "범하다",
    "hence": "따라서",
    "achieve": "이루다",
    "throughout": "~도처에",
    "distribute": "나누어 주다",
    "steep": "가파른",
    "former": "이전의",
    "latter": "후반의",
    "perceive": "인지하다",
    "combine": "결합하다",
    "proceed": "계속하다",
    "obvious": "명백한",
    "apply": "신청하다",
    "concentrate": "집중하다",
    "crisis": "위기",
    "inclined": "~하는 경향이 있는",
    "permanent": "영속하는",
    "temporary": "일시적인",
    "feature": "특징",
    "conceal": "숨기다",
    "reveal": "드러내다",
    "concern": "걱정",
    "classify": "분류하다",
    "circumstance": "상황",
    "involve": "포함하다",
    "occasion": "경우",
    "exterior": "바깥쪽의",
    "respect": "존경하다",
    "clarify": "명백하게 하다",
    "artificial": "인공의"
}
b = ""
check = False


@client.event
async def on_message(message):
    global EnglishWord, b, check
    if message.content.startswith("!영어"):
        if check == False:
            subject = message.content[4:]
            if subject == "단어":
                a = random.choice(list(EnglishWord.keys()))
                b = EnglishWord[a]
                check = True
                await message.channel.send("`" + a + "`")

        elif check == True:
            await message.channel.send("`이미 퀴즈를 푸시는 중 입니다.`")

    if message.content.startswith("!정답"):
        if check == True:
            answer = message.content[4:]
            if answer == b:
                check == False
                await message.channel.send("`정답입니다`")
                check = False
            elif answer != b:
                await message.channel.send("`오답입니다`")

              
        elif check == False:
            await message.channel.send("`풀고 있는 문제가 없습니다`")

    if message.content.startswith("!패스"):
        if check == True:
            await message.channel.send("`정답은 '" + b + "'(이)였습니다\n문제를 건너 뛰셨습니다.`")

        elif check == False:
            await message.channel.send(
                "`풀고 있는 문제가 없습니다, 만약 문제를 풀고 싶으시다면 채널 채팅창에 '!영어 단어'를 입력해주세요.`")

client.run(
    "OTkzNzc2Njg5NTYzODMyMzQx.GF7l8_.U_6RveTbV_NgShSeeRhNRj2FB25228bgY4zhQ4")