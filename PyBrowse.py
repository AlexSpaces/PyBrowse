import webview
import tkinter as tk

def open_browser():
    url = url_entry.get()
    webview.create_window("PyBrowse", url)
    webview.start()

if __name__ == "__main__":
    root = tk.Tk()
    root.title(" URL Input")

    url_label = tk.Label(root, text="Enter URL:")
    url_label.pack()

    url_entry = tk.Entry(root)
    url_entry.pack()

    open_button = tk.Button(root, text="Open Browser", command=open_browser)
    open_button.pack()

    root.mainloop()
