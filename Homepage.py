# homepage.py
import streamlit as st

def homepage():
    # Set the title of the homepage
    st.markdown('<div style="text-align:center; font-size:46px; font-weight:bold; margin-bottom:25px;">Selamat Datang di Sistem Prediksi Pinjaman Pribadi Kami!</div>', unsafe_allow_html=True)

    # sidebars
    st.sidebar.header("Menu")
    st.sidebar.page_link("https://streamlit.io/gallery", label="Chatbot")
    st.sidebar.page_link("pages/pinjaman.py", label="Prediksi Kelayakan Pinjaman")


    # Create columns
    col1, col2 = st.columns([1, 2])

    with col1:
        # Add an image
        st.image('images/chatbot.png', use_column_width=True)


    with col2:
        # Add some text
        st.markdown('<div style="text-align:justify; margin-top:40px;">Platform ini dirancang khusus untuk staf bank guna mempermudah proses pengajuan pinjaman. Dengan teknologi prediksi canggih dan dukungan chatbot interaktif, kami membantu Anda dalam mengevaluasi kelayakan pinjaman dengan lebih efisien dan akurat. Mari tingkatkan produktivitas dan pelayanan dengan alat inovatif kami!</div>', unsafe_allow_html=True)

    # Add a header
    st.markdown('<div style="text-align:center; font-size:30px; font-weight:bold; margin-bottom:25px; margin-top:35px;">Prediksi Akurat, Proses Cepat, Keputusan Tepat</div>', unsafe_allow_html=True)


    # Create columns
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.image('images/chatbotinformasi.png', use_column_width=True)
        st.markdown('<div style="text-align:center; font-size:20px; font-weight:bold; margin-bottom:25px; margin-top:25px;">Chatbot Informasi</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center">Chatbot yang mampu menjawab pertanyaan umum terkait proses pengajuan pinjaman, interpretasi hasil prediksi, dan prosedur lain yang relevan.</div>', unsafe_allow_html=True)

    with col2:
        st.image('images/predictive.png', use_column_width=True)
        st.markdown('<div style="text-align:center; font-size:20px; font-weight:bold; margin-bottom:18px;">Prediksi Kelayakan Pinjaman</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center">Sistem menganalisis data yang dimasukkan menggunakan model machine learning yang telah dilatih sebelumnya untuk memprediksi kelayakan pinjaman.</div>', unsafe_allow_html=True)

    with col3:
        st.image('images/analytics.png', use_column_width=True)
        st.markdown('<div style="text-align:center; font-size:20px; font-weight:bold; margin-bottom:25px; margin-top:25px;">Pelaporan dan Analisis</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center">Menghasilkan laporan periodik dan analisis mendalam mengenai tren pengajuan pinjaman dan kinerja model prediksi.</div>', unsafe_allow_html=True)

    # Add a header
    st.markdown('<div style="text-align:center; font-size:30px; font-weight:bold; margin-bottom:25px; margin-top:35px;">Gunakan Fitur Kami, Raih Hasil Terbaik!</div>', unsafe_allow_html=True)

    # Add some text
    st.markdown('<div style="text-align:center; margin-bottom:25px;">Berikut adalah beberapa fitur utama yang kami tawarkan untuk memudahkan pekerjaan Anda dan meningkatkan efisiensi dalam pengelolaan pinjaman pribadi.</div>', unsafe_allow_html=True)


    # Create columns
    col1, col2 = st.columns([1, 2])

    with col1:
        # Use st.image to display the image
        st.image('images/technology.png', use_column_width=True)
    
        # Add some space below the image using st.markdown and HTML
        st.markdown('<div style="margin-bottom:25px; width:2px;"></div>', unsafe_allow_html=True)

        # # Add an image
        # st.image('<div style= margin-bottom:25px;">images/technology.png</div>', use_column_width=True)

    with col2:
        
        st.markdown('<div style="text-align:justify; margin-bottom:10px; margin-top:5px; margin-left:10px;">Chatbot yang dapat merespons pertanyaan-pertanyaan mengenai proses pengajuan pinjaman.</div>', unsafe_allow_html=True)
        st.page_link("https://streamlit.io/gallery", label="Chatbot")

        st.markdown('<div style="text-align:justify; margin-bottom:10px; margin-top:18px; margin-left:10px;">Prediksi Kelayakan Pinjaman menampilkan hasil prediksi apakah pemohon layak mendapatkan pinjaman atau tidak.</div>', unsafe_allow_html=True)
        st.page_link("pages/pinjaman.py", label="Prediksi Kelayakan Pinjaman")


if __name__ == "__main__":
    homepage()
