import streamlit as st

st.set_page_config(page_title="Makerspace Dashboard", layout="wide")


if "tab" not in st.session_state:
    st.session_state["tab"] = "This is the Main Controllstation"

st.markdown(
    "<div style='text-align: right;'><img src='assets/logo.png'",
    unsafe_allow_html=True
)

if st.session_state["tab"] == "This is the Main Controllstation":
    #st.image("logo.png", use_container_width=False, caption="Powered by HellionCorp")
    st.markdown("""
        <style>
        .stApp {
            background-color: #000000;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: #2e2e2e;
        }
        </style>
    """, unsafe_allow_html=True)


st.sidebar.markdown("# Alle Features")

st.sidebar.markdown("---")

if st.sidebar.button("🧠 KI-Assistent", type="tertiary"):
    st.session_state.tab = "KI-Assistent"

if st.sidebar.button("📊 Monitoring", type="tertiary"):
    st.session_state.tab = "Monitoring"

if st.sidebar.button("🗂️ Dateisysteme", type="tertiary"):
    st.session_state.tab = "Dateisysteme"

st.sidebar.markdown("---")

if st.sidebar.button("🛠️ Makerspace", type="tertiary"):
    st.session_state.tab = "Hier sind die Makerspacesysteme angezeigt"

if st.sidebar.button("📦 Inventar", type="tertiary"):
    st.session_state.tab = "Inventarliste"

if st.sidebar.button("📁 Projektesammlung", type="tertiary"):
    st.session_state.tab = "Projektesammlung"

st.sidebar.markdown("---")

if st.sidebar.button("👤️BenutzerKonto", type="tertiary"):
    st.session_state.tab = "Dein Benutzer Konto"

if st.sidebar.button("⚙️Einstellungen", type="tertiary"):
    st.session_state.tab = "Einstellungen"


st.title(st.session_state.tab)



if st.session_state.tab == "KI-Assistent":
    st.write("Hier kommt dein KI-Interface hin.")
elif st.session_state.tab == "Dateisysteme":
    st.write("Hier kommt dein Dateimanager.")
elif st.session_state.tab == "Monitoring":
    st.write("Hier kommt dein Dashboard.")
elif st.session_state.tab == ("BenutzerKonto"):
    st.write("Hier kommt dein Dashboard.")
elif st.session_state.tab == ("Einstellungen"):
    st.write("Hier kommt dein Dashboard.")
elif st.session_state.tab == ("Makerspace"):
    st.write("Hier kommt dein Dashboard.")
elif st.session_state.tab == ("Inventar"):
    st.write("Hier kommt dein Dashboard.")
elif st.session_state.tab == ("Projektesammlung"):
    st.write("Hier kommt dein Dashboard.")
