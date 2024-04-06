def get_content(fname):
	with open(fname) as f:
		return f.readlines()

def create_person_dict(n, s):
	tmp = {}
	tmp["name"] = n
	tmp["surname"] = s
	return tmp
	

def create_list_of_names(content):
	ml = []
	for line in content:
		name, surname = line.split()
		ml.append(create_person_dict(name, surname))
	return ml

def write_into_file(fname, ml):
	with open(fname, "w") as f:
		for person in ml:
			data = list(person.values())
			line = " ".join(data)
			f.write(line + "\n")

def main():
	cnt = get_content("names.txt")
	names_list = create_list_of_names(cnt)
	names_list.sort(key=lambda x: x["name"])
	outfile = "result.txt"
	write_into_file(outfile, names_list)


if __name__ == "__main__":
	main()
