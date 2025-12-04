import streamlit as st
import pandas as pd

from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

df_users = pd.read_csv("users.csv")

img_home ="https://gifdb.com/images/high/standing-ovation-crowd-applause-oscar-awards-ai72icmh1ac7apdz.gif"
img_1 = "https://s1.qwant.com/thumbr/474x355/0/8/71a93663bbffe0d65f3d9d8b92e2033c77ceb78585261049a5ed29f6097c33/OIP.xG6quNdG9X8OoE1CgnDahwHaFj.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%2Fid%2FOIP.xG6quNdG9X8OoE1CgnDahwHaFj%3Fpid%3DApi&q=0&b=1&p=0&a=0"
img_2 = "https://s2.qwant.com/thumbr/474x567/e/d/48d5ac5fb66e50007f96e86ba4ae651952a3e533768005808374125d65b9b7/OIP.0_TlzpQBXZ9IyKkLwbXgaAHaI3.jpg?u=https%3A%2F%2Ftse3.explicit.bing.net%2Fth%2Fid%2FOIP.0_TlzpQBXZ9IyKkLwbXgaAHaI3%3Fpid%3DApi&q=0&b=1&p=0&a=0"
img_3 = "https://s2.qwant.com/thumbr/474x433/7/a/d76922c54100378aebd714c14f893f9ff2bf04f3742ba1853580a4cca1c204/OIP.Vms_4S5fk9Van2jd7B0DDgHaGx.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%2Fid%2FOIP.Vms_4S5fk9Van2jd7B0DDgHaGx%3Fpid%3DApi&q=0&b=1&p=0&a=0"
col1, col2, col3 = st.columns(3)

# Données utilisateurs 
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': df_users.loc[0,"name"],
            'password': df_users.loc[0,"password"],
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

def accueil():

    with st.sidebar:
    # Afficher le menu
        selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )
    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
        st.image(img_home)
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")
        
        with col1:
            st.header("Balance")
            st.image(img_1)

        with col2:
            st.header("Discovery")
            st.image(img_2)

        with col3:
            st.header("Joy")
            st.image(img_3)


if st.session_state["authentication_status"]:
    accueil()

    # Le bouton de déconnexion
    authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')



