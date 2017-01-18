import csv


def printCSV(myList = []):
	with open('print.csv', 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(myList)

def printToScreen():
	with open('print.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=' ', quotechar=',')
		for row in reader:
			print (', '.join(row))

if __name__ == "__main__":
	myList = [('smith, bob', 2), ('carol', 3), ('ted', 4), ('alice', 5)]
	printCSV(myList)
	printToScreen()
