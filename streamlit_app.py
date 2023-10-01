from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import streamlit as st
import json

# カラオケ曲のダミーデータ（JSON形式）
karaoke_data = {
    "songs": [
        {
            "title": "曲名1",
            "artist": "アーティスト1",
            "genre": "ジャンル1",
            "rating": 4.5
        },
        {
            "title": "曲名2",
            "artist": "アーティスト2",
            "genre": "ジャンル2",
            "rating": 4.0
        },
        {
            "title": "曲名3",
            "artist": "アーティスト3",
            "genre": "ジャンル1",
            "rating": 4.2
        },
        {
            "title": "曲名4",
            "artist": "アーティスト4",
            "genre": "ジャンル2",
            "rating": 3.8
        }
    ]
}

# カラオケ曲をJSONファイルに保存
with open('karaoke_data.json', 'w') as file:
    json.dump(karaoke_data, file, ensure_ascii=False, indent=4)

# カラオケ曲をJSONファイルから読み込む
with open('karaoke_data.json', 'r') as file:
    karaoke_data = json.load(file)

# サイドバーにページ切り替えを追加
page = st.sidebar.selectbox("アプリのページ", ["カラオケ曲一覧", "カラオケ曲追加"])

# カラオケ曲一覧のページ
if page == "カラオケ曲一覧":
    st.title("カラオケ曲の推薦アプリ")

    # ダミーデータを表示
    st.write("カラオケ曲一覧:")
    for song in karaoke_data["songs"]:
        st.write(f"曲名: {song['title']}")
        st.write(f"アーティスト: {song['artist']}")
        st.write(f"ジャンル: {song['genre']}")
        st.write(f"評価: {song['rating']}")
        st.write("---")

# カラオケ曲追加のページ
elif page == "カラオケ曲追加":
    st.title("カラオケ曲追加")

    # 新しい曲の情報を入力
    new_title = st.text_input("曲名")
    new_artist = st.text_input("アーティスト")
    new_genre = st.text_input("ジャンル")
    new_rating = st.slider("評価", 0.0, 5.0, 2.5, 0.1)

    # 追加ボタンを押して新しい曲を追加
    if st.button("曲を追加"):
        new_song = {
            "title": new_title,
            "artist": new_artist,
            "genre": new_genre,
            "rating": new_rating
        }
        karaoke_data["songs"].append(new_song)

        # カラオケ曲をJSONファイルに上書き保存
        with open('karaoke_data.json', 'w') as file:
            json.dump(karaoke_data, file, ensure_ascii=False, indent=4)

        # 追加した曲の確認メッセージ
        st.write(f"曲 '{new_title}' が追加されました！")

