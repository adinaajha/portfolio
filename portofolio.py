import streamlit as st 
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(layout="wide")



with open("st.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

col1,col2=st.columns(2,gap="small")
with col1 :
    #     # Path ke foto
    photo_path = "img/Frame 2.png"
    # Tampilkan foto
    st.image(photo_path, width=300)
with col2 :
    st.title('ADINA')
    st.subheader("Selamat Datang di profil saya! :wave:")
    st.write("Saya Adalah Mahasiswa dari Universitas STMIK IKMI Kota Cirebon dengan minat di bidang teknik informatika. Saya memiliki pengalaman di berbagai bidang, termasuk manajemen proyek, dan pengembangan perangkat lunak.")
    
    # Icon kecil untuk tautan sosial media
    st.write("[Instagram](https://www.instagram.com/didinjuandiansyah/) | [GitHub](https://github.com/adinaajha) | [WEBSITE](https://rekayasa-ebkdqkunhy8f5td3bouvlo.streamlit.app/)")

    st.write("Jangan ragu untuk menghubungi saya atau mengikuti profil saya di platform ini.")
st.write('---')

col1, col2 = st.columns([3,1])
with col1:
    st.header("Career Objective")
    st.write("Saya ADINA, Mahasiswa Universitas STMIK IKMI Cirebon, jurusan Rekayasa Perangkat Lunak. Saya memiliki pengalaman berpartisipasi dalam berbagai program industri, termasuk Studi SIB ERP, bootcamp Hasmicro di Odoo ERP, dan bootcamp FGA Database SQL Oracle. Semangat saya untuk belajar berasal dari pengalaman kerja yang mendorong saya untuk terus mengembangkan diri. Saya selalu fokus pada pemahaman materi yang menantang dan bersedia bekerja ekstra dalam proses pembelajaran. Selama perjalanan ini, saya telah membangun keterampilan kerja tim saya dan selalu siap untuk berkolaborasi. Saat ini saya masih dalam tahap studi, namun saya memiliki visi untuk menerapkan keterampilan tersebut dengan lebih efektif di masa depan.")

st.write('---')

with col2:
    st.header("Additional Skills")
    st.write('🚀 Manajemen Proyek')
    st.write('📊 Implementasi ERP')
    st.write('🐍 Python')
    st.write('🔍 C++')
    st.write('🌐 HTML, CSS, Bootstrap')
    st.write('📦 Odoo & Database')

col1,col2=st.columns(2)
with col1:
    st.write('\n')
    st.subheader("Experience & Qulifications")
    st.write(
        """
        - ✔️ Business Needs Analysis - Accounting and Finance
        - ✔️ Business Needs Analysis - Supply Chain 
        - ✔️ Create a Blueprint Project document and manage changes in the document. 
        - ✔️ Manage time analysis of problems, solutions, and user responses • Business Needs Analysis - Manufacturing
        - ✔️ Designing the system according to the Blueprint 
        - ✔️ Plan go-live and daily activities 
        - ✔️ Create training plans, and train end users 
        - ✔️ Lead a small team to conduct training and provide solutions to users 
        - ✔️ Implement dynamic team collaboration
        """
        )

with col2:
    st.write('\n')
    st.subheader("Education")
    st.image("https://2.bp.blogspot.com/-iDlW9RScnac/UN1qh7gTdjI/AAAAAAAAAEE/lrgWyDhOWXU/s320/STMIK+IKMI+warna+by+farhan.jpg", width=100)  # Ganti dengan URL ikon sekolah
    st.markdown("### Universitas STMIK IKMI Kota Cirebon")
    st.write("**2021 - 2023**")
    st.markdown('<img src="https://static.vecteezy.com/system/resources/previews/010/165/394/non_2x/rpl-letter-technology-logo-design-on-white-background-rpl-creative-initials-letter-it-logo-concept-rpl-letter-design-vector.jpg" width="100" height="100"> ', unsafe_allow_html=True)
    st.write("**Rekayasa Perangkat Lunak**")

st.write('---')
st.subheader("Certifications")
col1,col2=st.columns(2)
with col1:
    st.markdown("📜 Database Design and programin with sql  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("📊 Database Programing Oracel  "'<a href="" target="_blank" download><img src="" width="16"> </a>', unsafe_allow_html=True)
    st.markdown("🐍Belajar Dasar Data Science  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("🌐 Memulai Pemrograman dengan Haskell  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("🚀 Belajar Dasar Structured Query Language (SQL)  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("🔍Belajar Dasar-Dasar DevOps  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("👨‍💻Belajar Dasar Git dengan GitHub  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("📧Belajar Dasar Pemrograman JavaScript  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("📸 Cloud Practitioner Essentials (Belajar Dasar AWS Cloud)   "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("📅 Belajar Machine Learning untuk Pemula "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)

with col2:
    st.markdown("🔗Memulai Dasar Pemrograman untuk Menjadi Pengemban Software  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("🗂️Memulai Pemrograman Dengan Dart  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("📰Belajar Dasar Visualisasi Data  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("📅 Belajar Prinsip Pemrograman SOLID "'<a href="" target="_blank" download><img src="" width="16"> </a>', unsafe_allow_html=True)
    st.markdown("📚Belajar Dasar Pemrograman Web  "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("📋Memulai Pemrograman Dengan Python "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("🎯 Program SIB : ERP Pada Industri Kecil dan Menegah   "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("📫HIT Bootcamp in ERP Programing "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)
    st.markdown("📝 Python Fundamental for Data Science "'<a href="" target="_blank" download><img src="" width="16"></a>', unsafe_allow_html=True)


st.write('---')



