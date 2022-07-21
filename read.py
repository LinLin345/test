data = []
count = 0
with open("reviews.txt", "r") as r:
	for review in r:
		data.append(review)
		count += 1
		if count % 1000 == 0:
			print(count)
print(data[0])
