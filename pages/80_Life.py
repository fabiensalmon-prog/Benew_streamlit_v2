
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
render_section("life")

st.subheader(t("quiz"))
with st.form("life_quiz"):
    mobile = st.selectbox("Opérateur mobile", ["Peu importe","Orange","Free","SFR","Bouygues"])
    fiber = st.radio("Internet fixe ?", [t("yes"),t("no")], horizontal=True)
    submitted = st.form_submit_button(t("see_rec"))
if submitted:
    steps = ["Acheter une carte SIM (sans engagement).","Ouvrir un compte bancaire.","Souscrire assurance habitation si location."]
    if fiber == t("yes"):
        steps.append("Tester éligibilité fibre et souscrire box (Orange/Free/SFR/Bouygues).")
    st.success(" • ".join(steps))
