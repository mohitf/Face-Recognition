from functions import *
import time
import math

hist = []

def save_histogram(dir):
	for file1 in os.listdir(dir):
		for file2 in os.listdir(dir+'/'+file1):
			ans = histogram(dir+'/'+file1+'/'+file2)
			ans.append(file1)
			hist.append(ans)

def difference(arr1,arr2):
	ans = 0
	for i in range(256):
		ans += int(abs(arr1[i]-arr2[i]))
	return ans

def getmax(dict):
	tans = 0
	id = 0
	for key in dict:
		if dict[key] > tans:
			tans = dict[key]
			id = key
	return id

def find_results(dir):

	tot = 0
	cor = 0
	f1 = open('predictions.txt','w')
	f2 = open('accuracy.txt','w')

	for file1 in os.listdir(dir):

		tot1 = 0
		cor1 = 0
		f1.write(file1+'\n')
		f2.write(file1+' ')

		for file2 in os.listdir(dir+'/'+file1):
			ans = histogram(dir+'/'+file1+'/'+file2)
			tans = 1000000000
			id = 0
			for j in range(len(hist)):
				temp = difference(ans,hist[j])
				if temp < tans:
					tans = temp
					id = hist[j][256]

			if file1 == str(id):
				cor += 1
				cor1 += 1

			tot += 1
			tot1 += 1
			f1.write(file1+' '+str(id)+'\n')

		f1.write('\n')
		f2.write(str(((cor1+0.0)/tot1)*100)+'\n'+'\n')

		print file1+' '+str(((cor1+0.0)/tot1)*100)+'\n'


	print ((cor+0.0)/tot)*100

t = time.time()
save_histogram('./Train')
# print time.time()-t

print

t = time.time()
find_results('./Test')
# print time.time()-t