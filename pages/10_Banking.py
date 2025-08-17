
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
render_section("banking")

st.subheader(t("quiz"))
with st.form("bank_quiz"):
    profile = st.selectbox(t("profile"), [t("student"),t("worker"),t("family"),t("entrepreneur"),t("retiree")])
    papers = st.radio(t("papers"), [t("yes"),t("no")], horizontal=True)
    fx = st.radio(t("fx"), [t("yes"),t("no")], horizontal=True)
    branch = st.radio(t("branch"), [t("yes"),t("no")], horizontal=True)
    submitted = st.form_submit_button(t("see_rec"))
if submitted:
    rec = []
    if papers == t("no"):
        rec.append("N26 / Revolut / Wise — ouverture rapide, justificatifs allégés.")
    if profile == t("entrepreneur"):
        rec.append("Qonto / Shine / BNP Pro — comptes pro adaptés.")
    if fx == t("yes"):
        rec.append("Revolut / Wise — frais FX bas et cartes multi-devises.")
    if branch == t("yes"):
        rec.append("BNP / Crédit Agricole / Société Générale — réseau d'agences.")
    if not rec:
        rec.append("Boursorama / Hello bank! — frais bas en ligne.")
    st.success(" • ".join(rec))
