import streamlit as st;from pytube import YouTube
def download_video(video_url, download_path):
    try:
        st.info("Téléchargement en cours...");yt = YouTube(video_url)
        ys = yt.streams.get_highest_resolution();ys.download(download_path)
        st.success("Téléchargement terminé avec succès!")
    except Exception as e: st.error(f"Une erreur s'est produite: {str(e)}")
# Interface utilisateur Streamlit
st.title("Téléchargeur de vidéos YouTube")
# Zone de saisie pour l'URL de la vidéo
video_url = st.text_input("Entrez l'URL de la vidéo YouTube:")
if st.button("Télécharger"):
    if video_url: download_video(video_url, ".")  # Spécifiez le chemin où vous souhaitez enregistrer la vidéo
    else:st.warning("Veuillez saisir l'URL de la vidéo.")
