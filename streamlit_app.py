import streamlit as st

st.title('Syarat Pendaftaran KIP Kuliah')

st.image('data:image/jpeg;base64,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', width=400)
    
st.header('Syarat Pendaftaran Khusus')
st.write('1. Jenjang Pendidikan minimal D1 atau S1 dan maksimal S2')
st.write('2. Akreditasi Perguruan Tinggi minimal akreditasi B')
st.write('3. Akreditasi Program Studi minimal akreditasi C')
st.write('4. Nilai IPK Semester Terakhir nilai IPK semester terakhir harus kurang dari 2.50')
