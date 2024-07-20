import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('火星隕石のスペクトルデータの可視化')

uploaded_file = st.file_uploader('CSVファイルをアップロードしてください')
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        
        # データをプロット
        fig, ax = plt.subplots()
        ax.plot(df['wavelength'], df['intensity'], label='Spectral Data')
        ax.set_xlabel('Wavelength')
        ax.set_ylabel('Intensity')
        ax.legend()
        st.pyplot(fig)
    except Exception as e:
        st.error(f'ファイルの読み込みに失敗しました: {e}')
