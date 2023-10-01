from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

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

# Streamlitアプリの設定
st.title("カラオケ曲の推薦アプリ")

# ダミーデータを表示
st.write("カラオケ曲一覧:")
for song in karaoke_data["songs"]:
    st.write(f"曲名: {song['title']}")
    st.write(f"アーティスト: {song['artist']}")
    st.write(f"ジャンル: {song['genre']}")
    st.write(f"評価: {song['rating']}")
    st.write("---")

# 以下は追加の機能を組み込む部分です
# 1. フィルタリング機能
genre_filter = st.selectbox("ジャンルを選択して曲をフィルタリング", ["ジャンル1", "ジャンル2"])
filtered_songs = [song for song in karaoke_data["songs"] if song["genre"] == genre_filter]

if filtered_songs:
    st.write(f"{genre_filter} の曲一覧:")
    for song in filtered_songs:
        st.write(f"曲名: {song['title']}")
        st.write(f"アーティスト: {song['artist']}")
        st.write(f"評価: {song['rating']}")
        st.write("---")
else:
    st.write("該当する曲がありません。")

# 2. ソート機能
sort_option = st.radio("曲を評価でソート", ["昇順", "降順"])
if sort_option == "昇順":
    sorted_songs = sorted(karaoke_data["songs"], key=lambda x: x["rating"])
else:
    sorted_songs = sorted(karaoke_data["songs"], key=lambda x: x["rating"], reverse=True)

st.write("ソートされた曲一覧:")
for song in sorted_songs:
    st.write(f"曲名: {song['title']}")
    st.write(f"アーティスト: {song['artist']}")
    st.write(f"評価: {song['rating']}")
    st.write("---")
