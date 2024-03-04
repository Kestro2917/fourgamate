import math
import decimal
def main():
	f=open("fgrv_whole.txt","r")
	arr = []
	dic = []
	s_e = 0
	for line in f:
		line = line.rstrip("\n")
		arr = line.split("\t")
		#print(len(arr))
		sum_=0
		for i in arr[1:17]:
			sum_ = sum_ + int(i)
		#print(sum_)
		entropy = 0
		for j in arr[1:17]:
			if int(j) > 0:
				#print(int(j))
				x = float(decimal.Decimal(int(j))/sum_)
				#print(x)
				entropy = entropy + x*math.log(1/x,2)
				#print(entropy)
		#print(entropy)
		s_e = s_e + entropy
	print(s_e)		
								
		#print(sum)
		#dic[int(arr[0])] = arr[1:16]
		#print(arr)
	#print(dic)

if __name__ == "__main__":
	main()
