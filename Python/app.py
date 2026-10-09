
import webbrowser as wb 
while True:
    url = input("Enter the URL: ")
    def open_web(url):
        wb.open(url)
    if __name__ == "__main__":
        open_web(url)