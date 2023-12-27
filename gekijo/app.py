from re import X
import streamlit as st
import math
import random

chance_A = math.floor(65536/350 )
chance_B = math.floor(65536/350 )
chance_bell = math.floor(65536/150)
suica = math.floor(65536/100)
jcherry = math.floor(65536/98)
kcherry = math.floor(65536/327)
replay = math.floor(65536/7)
bell3 = math.floor(65536/24)
yaku1 = math.floor(65536/49)
oshijun = math.floor(65536/1.5)

def koyaku():
    ransu = random.randrange(65536)
    if ransu < chance_A:
        result = "チャンス目A"
    elif ransu < (chance_A + chance_B):
        result = "チャンス目B"
    elif ransu < (chance_A + chance_B + chance_bell):
        result = "チャンスベル"
    elif ransu < (chance_A + chance_B + chance_bell + suica):
        result = "スイカ"
    elif ransu < (chance_A + chance_B + chance_bell + suica + jcherry):
        result = "弱チェリー"
    elif ransu < (chance_A + chance_B + chance_bell + suica + jcherry + kcherry):
        result = "強チェリー"
    elif ransu < (chance_A + chance_B + chance_bell + suica + jcherry + kcherry + replay):
        result = "リプレイ"
    elif ransu < (chance_A + chance_B + chance_bell + suica + jcherry + kcherry + replay + bell3):
        result = "三枚ベル"
    elif ransu < (chance_A + chance_B + chance_bell + suica + jcherry + kcherry + replay + bell3 + yaku1):
        result = "共通一枚"
    elif ransu < (chance_A + chance_B + chance_bell + suica + jcherry + kcherry + replay + bell3 + yaku1 + oshijun):
        result = "押し順ベル"
    else:
        result = "ハズレ"
    return result

x = 1
st.title("激情ジャッジシュミレーター")
st.header("第1ゲーム")

seikou = 0
if st.button("レバーを叩け!"):
    if x == 1:
        result = koyaku()
        st.text(result)
        if result == "チャンス目A":
            seikou = seikou + 1
        elif result == "チャンス目B":
            seikou = seikou + 1
        elif result == "強チェリー":
            seikou = seikou + 1
        elif result == "弱チェリー":
            judge = random.randrange(100)
            if judge < 50:
                seikou = seikou +1
        elif result == "スイカ":
            judge = random.randrange(100)
            if judge < 50:
                seikou = seikou +1
        elif result == "チャンスベル":
            judge = random.randrange(100)
            if judge < 50:
                seikou = seikou +1
        elif result == "リプレイ":
            judge = random.randrange(100)
            if judge < 40:
                seikou = seikou +1
        elif result == "三枚ベル":
            judge = random.randrange(100)
            if judge < 40:
                seikou = seikou +1
        else:
            judge = random.randrange(100)
            if judge == 0:
                seikou = seikou +1
    else: 
        st.text("error")
x = x + 1
st.header("第2ゲーム")
if st.button("レバーを叩け!!"):
    if x == 2:
        result = koyaku()
        st.text(result)
        if result == "チャンス目A":
            seikou = seikou + 1
        elif result == "チャンス目B":
            seikou = seikou + 1
        elif result == "強チェリー":
            seikou = seikou + 1
        elif result == "弱チェリー":
            judge = random.randrange(100)
            if judge < 50:
                seikou = seikou +1
        elif result == "スイカ":
            judge = random.randrange(100)
            if judge < 50:
                seikou = seikou +1
        elif result == "チャンスベル":
            judge = random.randrange(100)
            if judge < 50:
                seikou = seikou +1
        elif result == "リプレイ":
            judge = random.randrange(100)
            if judge < 40:
                seikou = seikou +1
        elif result == "三枚ベル":
            judge = random.randrange(100)
            if judge < 40:
                seikou = seikou +1
        else:
            judge = random.randrange(100)
            if judge == 0:
                seikou = seikou +1
    else: 
        st.text("error")

x = x + 1
st.header("第3ゲーム")
if st.button("レバーを叩け!!!"):
    if x == 3:
        x = x + 1
        result = koyaku()
        st.text(result)
        if result == "チャンス目A":
            seikou = seikou + 1
        elif result == "チャンス目B":
            seikou = seikou + 1
        elif result == "強チェリー":
            seikou = seikou + 1
        elif result == "弱チェリー":
            judge = random.randrange(100)
            if judge < 50:
                seikou = seikou +1
        elif result == "スイカ":
            judge = random.randrange(100)
            if judge < 50:
                seikou = seikou +1
        elif result == "チャンスベル":
            judge = random.randrange(100)
            if judge < 50:
                seikou = seikou +1
        elif result == "リプレイ":
            judge = random.randrange(100)
            if judge < 40:
                seikou = seikou +1
        elif result == "三枚ベル":
            judge = random.randrange(100)
            if judge < 40:
                seikou = seikou +1
        else:
            judge = random.randrange(100)
            if judge == 0:
                seikou = seikou +1
    else: 
        st.text("error")

x = x + 1
st.header("最終ゲーム")
if st.button("運命を操れ!"):
    if x == 4:
        result = koyaku()
        st.text(result)
        if result == "チャンス目A":
            seikou = seikou + 1
        elif result == "チャンス目B":
            seikou = seikou + 1
        elif result == "強チェリー":
            seikou = seikou + 1
        elif result == "弱チェリー":
            seikou = seikou + 1
        elif result == "スイカ":
            seikou = seikou + 1
        elif result == "チャンスベル":
            seikou = seikou + 1
        elif result == "リプレイ":
            seikou = seikou + 1
        elif result == "三枚ベル":
            seikou = seikou + 1
        else:
            judge = random.randrange(100)
            if judge < 10:
                seikou = seikou +1
    else:
        st.text("Error")

    if seikou != 0:
        st.text("幕引!!!")
    else:
        st.text("残念")


if st.button("リセット"):
    x = 1
    seikou = 0