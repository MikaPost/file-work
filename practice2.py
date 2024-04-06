def get_content(fname):
	with open(fname) as f:
		return f.readlines()

def write_into_file(fname, ml):
	with open(fname, "w") as f:
		for line in ml:
			f.write(line)

def main():
	fname = "names.txt"
	cnt = get_content(fname)
	cnt.sort(key=len, reverse=True)
	outfile = "result.txt"
	write_into_file(outfile, cnt)


if __name__ == "__main__":
	main()
