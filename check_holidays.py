import streamlit as st
import holidays
from datetime import date

st.title("📅 Vérifier si un jour est férié")

pays_disponibles = {
    "Maroc": "MA",
    "France": "FR",
    "USA": "US",
    "Espagne": "ES"
}

pays_nom = st.selectbox(
    "Choisir un pays :",
    list(pays_disponibles.keys()),
    key="pays_select"
)

jour_x = st.date_input(
    "Choisir une date :",
    value=date.today(),
    key="date_input"
)

if st.button("Vérifier", key="btn_check"):
    # ✅ Correction ici
    jours_feries = holidays.CountryHoliday(pays_disponibles[pays_nom])

    if jour_x in jours_feries:
        st.success(f"✅ Oui, férié : {jours_feries[jour_x]}")
    else:
        st.error("❌ Non, pas férié")