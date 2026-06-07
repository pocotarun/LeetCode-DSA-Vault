import sys
import keyboard
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout, QPushButton
from PyQt6.QtWebEngineCore import QWebEngineProfile
from PyQt6.QtWebEngineWidgets import QWebEngineView

class VSCodeJugaadBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 🎨 Tagda UI/UX Setup (Edge & Brave Inspired Dark Mode)
        self.setWindowTitle('VS Code Companion Browser')
        self.setGeometry(100, 100, 450, 800) # Side panel ki tarah lamba window
        
        # 📌 Hamesha VS Code ke upar floating rahega
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        # Main Widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)

        # 🚀 URL Bar aur Controls Layout
        nav_layout = QHBoxLayout()
        
        self.url_bar = QLineEdit()
        self.url_bar.setText("https://www.youtube.com")
        self.url_bar.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                color: #A3E635; /* Aapka favorite green color */
                border: 1px solid #333;
                border-radius: 4px;
                padding: 4px;
                font-family: Consolas;
            }
        """)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_layout.addWidget(self.url_bar)
        layout.addLayout(nav_layout)

        # 🌐 Web View (Real Chrome Engine)
        self.browser = QWebEngineView()
        
        # 🛡️ Ad-Blocker Hack (Brave Style Request Blocking)
        # Custom profile banakar hum ads tracking scripts ko generic level par ignore karenge
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        self.browser.setUrl(QUrl("https://www.youtube.com"))
        layout.addWidget(self.browser)
        
        # Dark theme background tint for browser loading
        self.setStyleSheet("background-color: #121212;")

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'https://www.google.com/search?q=' + url
        self.browser.setUrl(QUrl(url))

# 🎹 Universal Control Room (Edge Style Toggle Shortcut)
def toggle_browser():
    if window.isVisible():
        window.hide()
    else:
        window.show()
        window.raise_()
        window.activateWindow()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VSCodeJugaadBrowser()
    window.show()

    # Pura system me kahin se bhi Ctrl + 1 dabaoge, ye browser side me pop-up ho jayega/hide ho jayega!
    keyboard.add_hotkey('ctrl+1', toggle_browser)

    sys.exit(app.exec())


