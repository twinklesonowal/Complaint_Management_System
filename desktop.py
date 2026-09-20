import threading
import time
import webview

from app import create_app


# -------------------------------------
# Create Flask Application
# -------------------------------------
app = create_app()


# -------------------------------------
# Run Flask Server
# -------------------------------------
def start_flask():
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=False
    )


# -------------------------------------
# Start Flask in Background
# -------------------------------------
flask_thread = threading.Thread(
    target=start_flask,
    daemon=True
)

flask_thread.start()


# -------------------------------------
# Wait for Flask to Start
# -------------------------------------
time.sleep(2)


# -------------------------------------
# Create Desktop Window
# -------------------------------------
webview.create_window(
    title="NHPC Complaint Management System",
    url="http://127.0.0.1:5000",
    width=1400,
    height=900,
    min_size=(1200, 700),
    resizable=True,
    text_select=True
)


# -------------------------------------
# Start Desktop Application
# -------------------------------------
webview.start()