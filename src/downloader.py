# to make requests to the URL
import requests
# to parse URLs
from urllib.parse import urlparse
from os import path, getcwd, mkdir
import sys

from .file_name_generator import gen_new_file_name
class Downloader:
	url = ""
	domain = ""
	base_download_path = f"{getcwd()}/downloads"
	full_download_path = ""

	def __init__(self, url):
		print("Preparing to download...\n")
		self.url = url
		self.create_download_path()
		self.gen_full_download_path()

	# make request to the URL and download object
	def download(self):		
		try:
			r = requests.get(self.url, stream=True)
			if r.status_code == 200:
				with open(self.full_download_path, "wb") as f:
					f.write(r.raw.read())
				print(f"File downloaded: {self.full_download_path}\n")
			else:
				print("Error while fetching data; HTTP status {r.status_code}\n")
		except:
			print(f"Some error occurred while trying to download from URL: {self.url}\n", sys.exc_info()[0])

	# create download directory
	def create_download_path(self):
		# get domain from URL; e.g., www.youtube.com
		domain = urlparse(self.url).netloc
		keys = domain.split(".")
		domain = "-".join(keys)
		self.domain = domain

		download_path = f"{getcwd()}/downloads/{domain}"
		if not path.exists(download_path):
			mkdir(download_path)

		self.base_download_path = download_path		

	# generate full download path
	def gen_full_download_path(self):
		url = self.url
		file_name = url.split("/")[-1]

		full_download_path = self.base_download_path + f"/{file_name}"

		# check if file already exists
		while path.exists(full_download_path):
			file_name = gen_new_file_name(file_name)
			full_download_path = self.base_download_path + f"/{file_name}"

		self.full_download_path = full_download_path
