import streamlit as st
import pandas as pd

def run():
    # Custom CSS for Navigation Bar and Style
    st.markdown("""
        <style>
        .nav-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #000000;
        }
        .nav-item {
            margin-right: 20px;
            font-weight: bold;
            cursor: pointer;
        }
        .user-info {
            display: flex;
            align-items: center;
        }
        .settings-btn {
            margin-left: 15px;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    # Navigation Bar
    st.markdown("""
        <div class="nav-bar">
            <div>
                <span class="nav-item">Company Title</span>
                <span class="nav-item">Main Page</span>
                <span class="nav-item">Enter Data</span>
                <span class="nav-item">Dashboard</span>
            </div>
            <div class="user-info">
                <img src="assets/icons8-user-48.png" alt="User" style="width: 30px; height: 30px;">
                <span>User Name</span>
                <span class="settings-btn">Settings</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.title("Data Entry for Automation")

    # Initialize session state for DataFrame
    if 'data_df' not in st.session_state:
        st.session_state.data_df = pd.DataFrame()

    with st.form(key='entry_form'):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            kalip_performansa_alinsin_mi = st.selectbox("KALIP PERFORMANSA ALINSIN MI", ["EVET", "HAYIR"])
            numune_durumu = st.selectbox("NUMUNE DURUMU", ["ONAYLI", "ONAYSIZ"])
            sira_no = st.number_input("Sıra No", min_value=1)
            proje_turu = st.text_input("PROJE TÜRÜ")
            musteri_firma_adi = st.text_input("Müşteri Firma Adı")

        with col2:
            referans_no = st.text_input("Referans No")
            parca_adi = st.text_input("Parça Adı")
            malzeme = st.text_input("Malzeme")
            malzeme_turu = st.selectbox("Malzeme türü", ["PLASTİK", "KAUÇUK", "SİLİKON", "METAL", "DİĞER"])
            sertlik_shorea = st.number_input("Sertlik ShoreA ±", min_value=0, max_value=100)

        with col3:
            net_gr = st.number_input("Net (Gr)", format="%.2f")
            brut_gr = st.number_input("Brüt (Gr)", format="%.2f")
            kalip_tipi = st.selectbox("Kalıp Tipi", ["PRES", "ENJEKSİYON", "DÖKÜM", "DİĞER"])
            kalip_ve_goz_sayisi = st.text_input("Kalıp ve Göz Sayısı")
            numune_verilecek_tarih = st.date_input("Numune Verilecek Tarih")

        with col4:
            numune_sayisi = st.number_input("Numune Sayısı (Ad.)", min_value=0)
            numune_cikis_tarihi = st.date_input("Numune Çıkış Tarihi")
            sonuc = st.selectbox("Sonuç (Ret/Kabul)", ["Ret", "Kabul"])
            numunelendirme_sayisi = st.number_input("Numunelendirme Sayısı", min_value=0)
            yapilan_degisiklikler = st.text_area("Yapılan Değişiklikler ve Açıklamalar")

        submit_button = st.form_submit_button(label='Add')

        if submit_button:
            new_data = {
                "KALIP PERFORMANSA ALINSIN MI": kalip_performansa_alinsin_mi,
                "NUMUNE DURUMU": numune_durumu,
                "Sıra No": sira_no,
                "PROJE TÜRÜ": proje_turu,
                "Müşteri Firma Adı": musteri_firma_adi,
                "Referans No": referans_no,
                "Parça Adı": parca_adi,
                "Malzeme": malzeme,
                "Malzeme türü": malzeme_turu,
                "Sertlik ShoreA ±": sertlik_shorea,
                "Net (Gr)": net_gr,
                "Brüt (Gr)": brut_gr,
                "Kalıp Tipi": kalip_tipi,
                "Kalıp ve Göz Sayısı": kalip_ve_goz_sayisi,
                "Numune Verilecek Tarih": numune_verilecek_tarih.strftime('%Y-%m-%d'),
                "Numune Sayısı (Ad.)": numune_sayisi,
                "Numune Çıkış Tarihi": numune_cikis_tarihi.strftime('%Y-%m-%d'),
                "Sonuç (Ret/Kabul)": sonuc,
                "Numunelendirme Sayısı": numunelendirme_sayisi,
                "Yapılan Değişiklikler ve Açıklamalar": yapilan_degisiklikler
            }
            new_entry_df = pd.DataFrame([new_data])
            st.session_state.data_df = pd.concat([st.session_state.data_df, new_entry_df], ignore_index=True)

            st.table(st.session_state.data_df)

if __name__ == "__main__":
    run()
