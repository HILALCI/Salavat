import pandas as pd
from datetime import datetime
import streamlit as st


def guncelle(eklenecek):
    data = pd.read_csv("salavat.csv")
    salavat = data.Salavat_Sayisi[0]
    toplam = salavat + eklenecek
    data.Salavat_Sayisi = toplam
    zaman = datetime.now()
    data.Guncellenen_Tarih = datetime.strftime(zaman,"%D; %X")
    data.to_csv("salavat.csv", index=False)
    st.write("Salavat eklendi.")


def hedef(hedefim):
    data = pd.read_csv("salavat.csv")
    toplam = data.Salavat_Sayisi[0]

    if hedefim > toplam:
        kalan = hedefim - toplam
        st.write(f"\nSalavat hedefine kalan = {kalan}")
        
    
    elif hedefim < toplam:
        fazla = toplam - hedefim
        st.write(f"Hedefi tamamladın tebrikler.\nSalavat hedefinin fazlası = {fazla}")
    
    else:
        st.write("Hedefi tamamladın tebrikler.\nSalavat sayısını siteye ekleyebilirsin.")


def sifirla(kalsin=False):
    data = pd.read_csv("salavat.csv")
    salavat = data.Salavat_Sayisi[0]
    if kalsin:
        if hedefim < salavat:
            data.Salavat_Sayisi = salavat - hedefim
            zaman = datetime.now()
            data.Guncellenen_Tarih = datetime.strftime(zaman,"%D; %X")
            data.to_csv("salavat.csv", index=False)
            st.write("Salavat sayısı sıfırlandı.")

        else:
            st.write("Salavat hedefine henüz ulasılmadı.")
            st.write("Tamamen sıfırlamak için kutucuğun işaretini kaldırınız.")
    
    else:
        data.Salavat_Sayisi = 0
        zaman = datetime.now()
        data.Guncellenen_Tarih = datetime.strftime(zaman,"%D; %X")
        data.to_csv("salavat.csv", index=False)
        st.write("Salavat sayısı sıfırlandı.")




st.set_page_config(
    page_title="Salavat"
)

eklenecek = st.number_input('Eklenecek Salavat Sayısı', min_value=1)

if st.button('Ekle'):
    guncelle(eklenecek)


hedefim = st.selectbox(
    'Hedefiniz',
    (100, 300,500,1000,5000,10000, 20000, 50000, 100000)
)

if st.button('Hedefime Kalan'):
    hedef(hedefim)


kabul = st.checkbox("Hedef fazlası kayıtlı kalsın.")

if st.button('Sıfırla'):
    if kabul:
        sifirla(kalsin=True)
    
    else:
        sifirla()

kaydedilenler = pd.read_csv("salavat.csv")
st.write(kaydedilenler)