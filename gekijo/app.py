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


if 'seikou' not in st.session_state.keys():
    st.session_state['seikou'] = 0
def seikou():
    st.session_state['seikou'] = 1

if 'kaisu' not in st.session_state.keys():
    st.session_state['kaisu'] = 0
def kaisu():
    st.session_state['kaisu'] += 1

if 'koyaku' not in st.session_state.keys():
    st.session_state['koyaku'] = ""
def get_koyaku():
    st.session_state['koyaku'] = koyaku()

def game1_3():
    kaisu()

    

def reset():
    for key in st.session_state.keys():
        st.session_state[key] = 0

st.title("激情ジャッジシュミレーター")
st.header("第1ゲーム")


if st.button("レバーを叩け!", on_click=kaisu):
    if st.session_state['kaisu'] == 1:
        result = koyaku()
        st.text(result)
        if result == "チャンス目A":
            seikou()
        elif result == "チャンス目B":
            seikou()
        elif result == "強チェリー":
            seikou()
        elif result == "弱チェリー":
            judge = random.randrange(100)
            if judge < 50:
                seikou()
        elif result == "スイカ":
            judge = random.randrange(100)
            if judge < 50:
                seikou()
        elif result == "チャンスベル":
            judge = random.randrange(100)
            if judge < 50:
                seikou()
        elif result == "リプレイ":
            judge = random.randrange(100)
            if judge < 40:
                seikou()
        elif result == "三枚ベル":
            judge = random.randrange(100)
            if judge < 40:
                seikou()
        else:
            judge = random.randrange(100)
            if judge == 0:
                seikou()
    else: 
        st.text("error")

st.header("第2ゲーム")
if st.button("レバーを叩け!!", on_click=kaisu):
    if st.session_state['kaisu'] == 2:
        result = koyaku()
        st.text(result)
        if result == "チャンス目A":
            seikou()
        elif result == "チャンス目B":
            seikou()
        elif result == "強チェリー":
            seikou()
        elif result == "弱チェリー":
            judge = random.randrange(100)
            if judge < 50:
                seikou()
        elif result == "スイカ":
            judge = random.randrange(100)
            if judge < 50:
                seikou()
        elif result == "チャンスベル":
            judge = random.randrange(100)
            if judge < 50:
                seikou()
        elif result == "リプレイ":
            judge = random.randrange(100)
            if judge < 40:
                seikou()
        elif result == "三枚ベル":
            judge = random.randrange(100)
            if judge < 40:
                seikou()
        else:
            judge = random.randrange(100)
            if judge == 0:
                seikou()
    else: 
        st.text("error")

st.header("第3ゲーム")
if st.button("レバーを叩け!!!", on_click=kaisu):
    if st.session_state['kaisu'] == 3:
        result = koyaku()
        st.text(result)
        if result == "チャンス目A":
            seikou()
        elif result == "チャンス目B":
            seikou()
        elif result == "強チェリー":
            seikou()
        elif result == "弱チェリー":
            judge = random.randrange(100)
            if judge < 50:
                seikou()
        elif result == "スイカ":
            judge = random.randrange(100)
            if judge < 50:
                seikou()
        elif result == "チャンスベル":
            judge = random.randrange(100)
            if judge < 50:
                seikou()
        elif result == "リプレイ":
            judge = random.randrange(100)
            if judge < 40:
                seikou()
        elif result == "三枚ベル":
            judge = random.randrange(100)
            if judge < 40:
                seikou()
        else:
            judge = random.randrange(100)
            if judge == 0:
                seikou()
    else: 
        st.text("error")


st.header("最終ゲーム")
if st.button("運命を操れ!", on_click=kaisu):
    if st.session_state['kaisu'] == 4:
        result = koyaku()
        st.text(result)
        if result == "チャンス目A":
            seikou()
        elif result == "チャンス目B":
            seikou()
        elif result == "強チェリー":
            seikou()
        elif result == "弱チェリー":
            seikou()
        elif result == "スイカ":
            seikou()
        elif result == "チャンスベル":
            seikou()
        elif result == "リプレイ":
            seikou()
        elif result == "三枚ベル":
            seikou()
        else:
            judge = random.randrange(100)
            if judge < 10:
                seikou()
    else:
        st.text("Error")

    if st.session_state['seikou'] == 1:
        st.text("幕引!!!")
    else:
        st.text("残念")

if st.button("リセット", on_click = reset):
        st.text("再挑戦！もう一度上から押してね！")