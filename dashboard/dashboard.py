import streamlit as st 
import pandas as pd
import calendar as calendar
import matplotlib.pyplot as plt
import seaborn as sns

# Oleh Muhammad Dava Pasha (Dicoding)

day_raw = pd.read_csv('./data/day.csv')
months = calendar.month_name[1:]

# Mengkonversi data raw date ke format panda untuk lebih gampang diolah
day_raw['dteday'] = pd.to_datetime(day_raw['dteday'])

# Mengestrak hari, bulan dan tahun dari dteday
day_raw['day'] = day_raw['dteday'].dt.day
day_raw['month'] = day_raw['dteday'].dt.month
day_raw['year'] = day_raw['dteday'].dt.year

# Ubah nomer cuaca ke tulisan agar lebih gampang dipahami
day_raw['weathersit'] =  day_raw['weathersit'].replace(1, 'Cerah').replace(2, 'Mendung').replace(3, 'Gerimis').replace(4, 'Deras')

st.title('Dashboard Bike Sharing')
st.caption('Oleh Muhammad Dava Pasha (Dicoding)')

# Fixed section

jumlah_perbulan = day_raw.groupby(by='mnth')['cnt'].sum().reset_index()
line_tab, bar_tab = st.tabs(["Grafik Garis", "Grafik Batang"])

with line_tab:
    st.line_chart(jumlah_perbulan, x='mnth', y='cnt', x_label='Bulan', y_label='Jumlah')

with bar_tab:
    st.bar_chart(jumlah_perbulan, x='mnth', y='cnt', x_label='Bulan', y_label='Jumlah')


# Interaktif section

option = st.selectbox(
    'Pilih grafik penyewaan sepeda untuk bulan?',
    months,
)

line_tab, bar_tab = st.tabs(["Grafik Garis", "Grafik Batang"])

month_index = months.index(option) + 1
month_result = day_raw.loc[day_raw['mnth'] == month_index]

with line_tab:
    st.line_chart(month_result, x='day', y='cnt', x_label='Hari', y_label='Jumlah')

with bar_tab:
    st.bar_chart(month_result, x='day', y='cnt', x_label='Hari', y_label='Jumlah')

option = st.selectbox(
    'Pilih grafik penyewaan sepeda untuk cuaca?',
    ('Cerah', 'Gerimis', 'Mendung'),
)

weather_result = day_raw[day_raw['weathersit'] == option].groupby(by='mnth')['cnt'].sum().reset_index()

line_tab, bar_tab = st.tabs(["Grafik Garis", "Grafik Batang"])

with line_tab:
    st.line_chart(weather_result, x='mnth', y='cnt', x_label='Bulan', y_label='Jumlah')

with bar_tab:
    st.bar_chart(weather_result, x='mnth', y='cnt', x_label='Bulan', y_label='Jumlah')