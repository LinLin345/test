data = []
count = 0
with open("reviews.txt", "r") as r:
	for review in r:
		data.append(review)
		count += 1
		if count % 1000000 == 0:
			print(count)
#print(data[0])

# word count
wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 
# print(wc)

#for loop print word_count
for word in wc:
	if wc[word] > 1000000:
 		print(word,wc[word])
print(len(wc))

# search word by user input_word
while True:
	search_world = input("Please inpput search word:")
	if search_world == "q":
		break
	if search_world in wc:
 		print(search_world,wc[search_world])
	else:
		print("There is no search word")		
print('Thank you useing this search tool')
# # count average len of reviews
# sum_len = 0
# for d in data:
# 	sum_len += len(d)
# print(sum_len/len(data))

# # filter reviews : chose len small than 100
# newdata = []
# for d in data:
# 	if len(d) < 100:
# 		newdata += d
# print("There is ", len(newdata), "small than 100")

# # filter reviews : chose including "good" in reviews
# good = []
# for d in data:
# 	if "good" in d:
# 		good.append(d)
# print("There are all", len(good), "including good")
# print(good[1])

# #清单快写
# good = [d for d in data if "good" in d]
# print(good)

# bad = ['bad' in d for d in data]