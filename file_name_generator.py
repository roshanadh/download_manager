from os import path

# generate new file name
def gen_new_file_name(file_name):
	# append _new to file name before extension
	extension = file_name.split(".")[-1]
	file_name_before_ext = file_name.replace(f".{extension}", "")
	file_name_before_ext += "_new"

	file_name = file_name_before_ext + f".{extension}"
	return file_name
