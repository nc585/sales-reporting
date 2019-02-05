# print("SALES REPORT (MONTH)")

#month # define month

import csv

units_sold = [] # TODO: read from csv file

csv_file_path = "sales-201710.csv" # a relative filepath

with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    for row in reader:
        #d = dict(row)
        d = {"date": row["date"], "product": row["product"], "unit price": row["unit price"], "units sold": row["units sold"], "sales price": row["sales price"]}
        #print(type(d), d["name"], d["price"])
        units_sold.append(d["units sold"])
        unit_sold = d["units sold"]
        running_units_sold = units_sold + unit_sold 

print(running_units_sold)
#date,product,unit price,units sold,sales price

print("SALES REPORT", "(", "month", ")")
print("TOTAL SALES: ")