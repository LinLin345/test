data = []
count = 0
with open("reviews.txt", "r") as r:
	for review in r:
		data.append(review)
		count += 1
		if count % 1000 == 0:
			print(count)
print(data[0])

# count average len of reviews
sum_len = 0
for d in data:
	sum_len += len(d)
print(sum_len/len(data))