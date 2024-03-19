import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st

st.title('米国株価可視化アプリ')

st.sidebar.write("""
# GAFA株価
こちらは株価可視化ーつです。以下のオプションから表示日数を指定
                 """)

st.sidebar.write('表示日数選択')
days = st.sidebar.slider('日数',1,50,20)


st.write(f"""
### 過去 **{days}日間**のGAFAの株価
""")

@st.cache_data
def get_data(days,tickers):
    df = pd.DataFrame()

    for company in tickers.keys():

        trk = yf.Ticker(tickers[company])
        hist = trk.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name ='Name'
        df = pd.concat([df,hist])

    return df

try:
    st.sidebar.write("""
    ## 株価の範囲指定
    """)

    ymin,ymax = st.sidebar.slider('範囲を指定してください',0,2000,(0,2000))

    tickers = {'apple':'AAPL',
            'Meta':'Meta',
            'Google':'GOOGL',
            'microsoft':'MSFT',
            'amazon':'AMZN',
            'netflix':'NFLX'
            }

    df = get_data(days,tickers)

    companies = st.multiselect(
        '会社名を選択してください',
        list(df.index),
        ['Google','amazon','Meta','apple']
    )
    if not companies:
        st.error('少なくとも1社は選んでください')
    else:
        data = df.loc[companies]
        st.write("### 株価(USD)",data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date'])
        data.rename(columns={'value':'Stock Prices(USD)'},inplace=True)
        chart = (
            alt.Chart(data)
            .mark_line(opacity = 0.8,clip=True)
            .encode(
                x = "Date:T",
                y = alt.Y("Stock Prices(USD)",stack = None, scale=alt.Scale(domain=[ymin,ymax])),
                color = 'Name:N'
            )
        )
        st.altair_chart(chart,use_container_width=True)
except:
    st.error(
        "何かエラーが起きているようです"
    )
