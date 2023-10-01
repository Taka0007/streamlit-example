from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import streamlit as st
import json

import streamlit as st
import json
import requests

# GitHubのJSONファイルのURL
github_url = "https://github.com/Taka0007/streamlit-example/blob/master/data/songs.json"

# JSONデータをGitHubから読み込む
response = requests.get(github_url)
if response.status_code == 200:
    karaoke_data = json.loads(response.text)
else:
    st.error("JSONデータを読み込めません。GitHub URLを確認してください。")

# サイドバーにページ切り替えを追加
page = st.sidebar.selectbox("アプリのページ", ["カラオケ曲一覧", "カラオケ曲追加"])

# カラオケ曲一覧のページ
if page == "カラオケ曲一覧":
    st.title("カラオケ曲の推薦アプリ")

    # カラオケ曲一覧を表示
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

        # カラオケ曲をGitHubのJSONファイルに上書き保存
        response = requests.put(github_url, data=json.dumps(karaoke_data))
        if response.status_code == 200:
            st.success(f"曲 '{new_title}' が追加されました！")
        else:
            st.error("曲を追加できませんでした。GitHub URLを確認してください。")

