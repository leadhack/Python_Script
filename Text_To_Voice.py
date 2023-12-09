#pip install gTTs
from gtts import gTTS
import os

# Votre texte à transformer en voix
texte = "Découvrez la puissance de la technologie vocale avec gTTS et Python!"

# Créez un objet gTTS
tts = gTTS(text=texte, lang='fr', slow=False)

# Sauvegardez le fichier audio
tts.save("description_audio.mp3")

# Lancez le lecteur audio pour écouter la description
os.system("start description_audio.mp3")

