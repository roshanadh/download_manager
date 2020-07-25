from src.downloader import Downloader


def begin_download(download_link):
	d = Downloader(download_link)
	# validate url
	d.download()


def main():
	# download_link = "https://pngimg.com/uploads/google/google_PNG19640.png"
	# download_link = "https://cdn.pixabay.com/photo/2020/06/02/12/12/sample-5250731_1280.png"

	while True:
		download_link = input("Type in the download link: \n")
		begin_prompt = input(f"Begin downloading {download_link} ? y/n ")

		if begin_prompt.lower() == "y":
			begin_download(download_link)

		elif begin_prompt.lower() == "n":
			continue
		else:
			print("Invalid input\n")
			continue

if __name__ == "__main__":
	main()
