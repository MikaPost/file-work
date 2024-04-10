def get_content(fname):
    with open(fname) as f:
        return f.read()

def create_list_of_names(cnt):
    ml = {}
    for i in cnt:
        if i.is:
            if i in ml:
                ml[i] += 1
            else:
                ml[i] = 1
    return ml

def write_into_file(ml, fname):
    with open(fname, "w") as f:
        for el in ml:
            f.write(el[0] + ": " + str(el[1]) + "\n")




def main():
    cnt = get_content("a.txt")
    names_list = create_list_of_names(cnt)
    ml = list(names_list.items())
    ml.sort(key=lambda x: x[1], reverse=True)
    write_into_file(ml, "resuli2.txt")




if __name__ == "__main__":
    main()
