def format_name(fname, lname):
    title_fname=fname.title()
    title_lname=lname.title()
    return f"{title_fname} {title_lname}"

print(format_name("Nguyen le", "MINH"))