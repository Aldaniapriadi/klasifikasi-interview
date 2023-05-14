import pickle
import streamlit as st

# membaca model
HR_model = pickle.load(open('klasifikasi_HR.sav', 'rb'))

#judul web
st.title('Prediksi Interview Kandidat ')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    years_of_experience = st.number_input ('Jumlah tahun pengalaman yang dimiliki kandidat di bidangnya')
    functional_competency_score = st.number_input ('Skor yang mewakili kompetensi fungsional kandidat berdasarkan tes')
    top1_skills_score = st.number_input ('Skor keterampilan paling berharga yang dimiliki kandidat')
    top2_skills_score = st.number_input ('Skor keterampilan paling berharga kedua yang dimiliki kandidat')
    top3_skills_score = st.number_input ('Skor keterampilan paling berharga ketiga yang dimiliki kandidat')

with col2 :
    behavior_competency_score = st.number_input ('Skor yang mewakili kompetensi perilaku kandidat yang diperoleh dari tes SDM')
    top1_behavior_skill_score = st.number_input ('Skor keterampilan perilaku paling berharga yang dimiliki kandidat')
    top2_behavior_skill_score = st.number_input ('Skor keterampilan perilaku paling berharga kedua yang dimiliki kandidat')
    top3_behavior_skill_score = st.number_input ('Skor dari keterampilan perilaku paling berharga ketiga yang dimiliki kandidat')

# code untuk prediksi
HR_predict = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Interview'):
    HR_prediction = HR_model.predict([[years_of_experience, functional_competency_score,
                                       top1_skills_score, top2_skills_score, top3_skills_score,
                                       behavior_competency_score, top1_behavior_skill_score,
                                       top2_behavior_skill_score, top3_behavior_skill_score]])

    if(HR_prediction[0] == 1):
        HR_predict = 'Kandidat Dipanggil Untuk Interview'
    else:
        HR_predict = 'Kandidat Tidak Dipanggil Untuk Interview'
st.success(HR_predict)
