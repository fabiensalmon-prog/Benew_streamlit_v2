
import streamlit as st
from data.utils import render_section, t, guard


st.sidebar.title("Benew")
st.sidebar.page_link("app.py", label=t("menu_home"))
st.sidebar.page_link("pages/00_Login.py", label=t("menu_login"))
st.sidebar.page_link("pages/01_Persona.py", label=t("menu_persona"))
st.sidebar.page_link("pages/10_Banking.py", label=t("menu_banking"))
st.sidebar.page_link("pages/20_Insurance.py", label=t("menu_insurance"))
st.sidebar.page_link("pages/30_Healthcare.py", label=t("menu_healthcare"))
st.sidebar.page_link("pages/40_Taxation.py", label=t("menu_taxation"))
st.sidebar.page_link("pages/50_Housing.py", label=t("menu_housing"))
st.sidebar.page_link("pages/60_Transport.py", label=t("menu_transport"))
st.sidebar.page_link("pages/70_Work.py", label=t("menu_work"))
st.sidebar.page_link("pages/80_Life.py", label=t("menu_life"))
st.sidebar.page_link("pages/90_Tools.py", label=t("menu_tools"))

guard()
render_section("housing")

st.subheader(t("quiz"))
with st.form("house_quiz"):
    budget = st.number_input(t("budget"), min_value=0, value=800, step=50)
    garant = st.radio("Garant en France ?", [t("yes"),t("no")], horizontal=True)
    duration = st.radio(t("duration"), [t("short"),t("long")], horizontal=True)
    submitted = st.form_submit_button(t("see_rec"))
if submitted:
    out = []
    if garant == t("no"): out.append("Sans garant : Studapart, Garantme, Visale.")
    if budget < 700: out.append("Cibler colocation & résidences étudiantes (CROUS).")
    if duration == t("short"): out.append("Baux mobilité (1–10 mois) ou résidences temporaires.")
    out.append("Comparer : Leboncoin, SeLoger. Dossier complet (ID, revenus).")
    st.success(" • ".join(out))
