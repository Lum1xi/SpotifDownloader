from colorama import Fore, Style
from time import sleep
from os import system,name
from downloader import download


print(Fore.CYAN + Style.BRIGHT + "SpotifyDownloader by Lum1xi" + Style.RESET_ALL)
print(Fore.CYAN + "GitHub: https://github.com/Lum1xi" + Style.RESET_ALL)
sleep(0.5)

def main():
    print("\n\n")
    while True:
        print("Menu:")
        print("1. Download a song/playlist/album")
        print("2. Exit")
        try:
            choice = int(input("Enter your choice (1/2): "))
            if choice not in [1, 2]:
                continue
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter 1 or 2." + Style.RESET_ALL)
            continue
        system('cls' if name == 'nt' else 'clear')
        if choice == 1:
            url = input("Enter the Spotify URL: ")
            if not url:
                print(Fore.RED + "URL cannot be empty." + Style.RESET_ALL)
                continue
            result = download(url)
            if result is None:
                print(Fore.RED + "Download failed or no action taken." + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"Success: {result}" + Style.RESET_ALL)
        elif choice == 2:
            print(Fore.CYAN + "Exiting the program. Goodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()