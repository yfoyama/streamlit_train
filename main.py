import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバー表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!!'

# df = pd.DataFrame({
#     '1列目':[1 ,2 ,3 ,4],
#     '2列目':[10 ,20 ,50 ,40]
# })

## 表を書く
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

## テキストを書く
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

## グラフを書く
# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns = ['a','b','c']
# )

# st.bar_chart(df)


## マップを書く
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69,139.70],
#     columns = ['lat','lon']
# )

# st.map(df)

## 画像読み込み
## チェックボックス
# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img,caption='Gemba Cat')

## セレクトボックス
# option = st.selectbox('あなたが好きな数字を教えてください、',
#              list(range(1,11))
#              )
# 'あなたが好きな数字は、',option,'です。'

## テクストボックス
# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は：',text

## スライダー
# condition = st.slider('あならの今の調子は？',0,100,50)
# 'コンディション：',condition

## カラム
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

## 
expander1 = st.expander('問い合わせ1')
expander1.write('回答1')
expander2 = st.expander('問い合わせ2')
expander2.write('回答2')
expander3 = st.expander('問い合わせ3')
expander3.write('回答3')