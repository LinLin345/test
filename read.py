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

# filter reviews : chose len small than 100
newdata = []
for d in data:
	if len(d) < 100:
		newdata += d
print("There is ", len(newdata), "small than 100")

# filter reviews : chose including "good" in reviews
good = []
for d in data:
	if "good" in d:
		good.append(d)
print("There are all", len(good), "including good")
print(good[1])