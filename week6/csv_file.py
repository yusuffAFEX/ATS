import csv
with open('new_flie.csv', "w") as f:
    filenames = ['Name', 'Weight', 'Height', 'Age']
    writer = csv.DictWriter(f, filenames)
    print(writer)
    writer.writeheader()
