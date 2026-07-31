import streamlit as st

st.markdown("# :red[💪แอปพลิเคชันคำนวณค่าดัชนีมวลกาย BMI ]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม) :")
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):")

if st.button("คำนวณค่า BMI ⚙️"):
  height_m = height_cm / 100
  bmi = weight / (heigh_m ** 2)

  st.write("---")
  st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")
