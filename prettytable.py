import operator
from prettytable import PrettyTable


table = PrettyTable(["Movie", "year", "Rating"])
table.add_row(["Goodfellas","1990", "8.7"])
table.add_row(["Casablanca", "1942", "8.5"])
table.add_row(["Thor","2017", "8.2"])
table.add_row(["Downsizing", "2017", "7.6"])
table.add_row(["Inception", "2010", "8.8"])
table.add_row(["Chicago", "2015", "8.1"])
print table.get_string(sort_key=operator.itemgetter(1, 0), sortby="Rating")