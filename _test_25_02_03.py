import pandas as pd
import streamlit as st
import plotly.express as px

# ตัวอย่างข้อมูลตารางสอน
data = {
    'อาจารย์': ['ดร.กิตติ', 'ผศ.สมชาย', 'รศ.สุชาติ', 'อ.กมล', 'ดร.นภาพร'],
    'รายวิชา': ['ชีวเคมี', 'จุลชีววิทยา', 'พันธุศาสตร์', 'สรีรวิทยา', 'เภสัชวิทยา'],
    'ชั่วโมงสอนต่อสัปดาห์': [6, 4, 5, 3, 17]
}
df = pd.DataFrame(data)

# สร้าง Dashboard
st.title("📊 AI Dashboard: ตารางสอนและภาระงานอาจารย์")

# แสดงตารางสอน
st.subheader("📅 ตารางสอนอาจารย์")
st.dataframe(df)

# แสดงกราฟภาระงานอาจารย์
fig = px.bar(df, x='อาจารย์', y='ชั่วโมงสอนต่อสัปดาห์', color='รายวิชา', title='ภาระงานสอนของอาจารย์')
st.plotly_chart(fig)

# วิเคราะห์ความสมดุลภาระงาน
avg_hours = df['ชั่วโมงสอนต่อสัปดาห์'].mean()
st.subheader("⚖️ วิเคราะห์ภาระงาน")
st.write(f"ค่าเฉลี่ยชั่วโมงสอนต่อสัปดาห์: {avg_hours:.2f} ชั่วโมง")

if any(df['ชั่วโมงสอนต่อสัปดาห์'] > avg_hours + 2):
    st.warning("⚠️ มีอาจารย์บางท่านที่มีภาระงานเกินกว่าค่าเฉลี่ยมาก ควรพิจารณาปรับตารางสอน!")

