import webview

def open_browser():
    url = "http://www.example.com"
    webview.create_window("Simple Web Browser", url)
    webview.start()

if __name__ == "__main__":
    open_browser()
