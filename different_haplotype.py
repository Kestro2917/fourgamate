def main():
	f = open("fgrv_whole.txt","r")
	arr = []
	sum_ = 0
	for line in f:
		line = line.rstrip("\n")
		arr = line.split("\t")
		#print(arr)
		counter_ = 0
		for i in arr[1:17]:
			if int(i)>1:
				#print(i)
				counter_ += 1
		#print(counter_)			
		sum_ = sum_ + counter_
	print(sum_)
if __name__ == "__main__":
	main()
