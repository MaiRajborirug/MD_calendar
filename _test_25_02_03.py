import streamlit as st
import pandas as pd

# Sample teaching schedule data
data = {
    'อาจารย์': ['ดร.กิตติ', 'ผศ.สมชาย', 'รศ.สุชาติ', 'อ.กมล', 'ดร.นภาพร'],
    'รายวิชา': ['ชีวเคมี', 'จุลชีววิทยา', 'พันธุศาสตร์', 'สรีรวิทยา', 'เภสัชวิทยา'],
    'ชั่วโมงสอนต่อสัปดาห์': [6, 4, 5, 3, 7]
}
df = pd.DataFrame(data)

# Streamlit Web UI
st.title("📚 ตารางสอนอาจารย์ (Teaching Schedule)")
st.write("นี่คือตารางสอนของอาจารย์แต่ละท่านในแต่ละวิชา")

# Display table
st.dataframe(df)

# Add Filters
selected_teacher = st.selectbox("เลือกอาจารย์:", df['อาจารย์'].unique())

# Filtered Table
filtered_df = df[df['อาจารย์'] == selected_teacher]
st.write(f"📅 ตารางสอนของ {selected_teacher}")
st.dataframe(filtered_df)