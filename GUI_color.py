import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QColor
from pytube import YouTube
from moviepy.editor import AudioFileClip

class DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('YouTube Audio Downloader')
        self.setGeometry(100, 100, 400, 150)
        # Establecer el color de fondo del widget principal a negro
        self.setStyleSheet("background-color: #072E33;")

        layout = QVBoxLayout()

        self.url_label = QLabel("URL del video de YouTube:")
        # Establecer el tamaño de la fuente y el color del texto del QLabel
        self.url_label.setStyleSheet("font-size: 20px; color: white;")
        self.url_input = QLineEdit()
        self.download_button = QPushButton("Descargar Audio")
        # Establecer el color de fondo del botón a celeste
        self.download_button.setStyleSheet("background-color: lightblue;")

        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.download_button)

        self.download_button.clicked.connect(self.download_audio)

        self.setLayout(layout)

    def download_audio(self):
        url = self.url_input.text()

        try:
            yt = YouTube(url)
            audio = yt.streams.filter(only_audio=True).first()
            audio_path = audio.download()
            audio_clip = AudioFileClip(audio_path)
            audio_clip.write_audiofile(audio_path[:-4] + '.mp3')
            audio_clip.close()
            print("Descarga exitosa del audio en formato MP3!")
        except Exception as e:
            print("Ocurrió un error durante la descarga del audio:", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    downloader = DownloaderApp()
    downloader.show()
    sys.exit(app.exec_())
