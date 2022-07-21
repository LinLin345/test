data = []
with open("reviews.txt", "r") as r:
	for review in r:
		data.append(review)
print(data[0])
