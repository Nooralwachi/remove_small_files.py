import os
def remove_small_files(dir_name):
	files=[]
	cwd=os.getcwd()
	for file in os.listdir(dir_name):
		size= os.path.getsize(dir_name +'/'+ file)
		files.append([file,size])
	sorted_files =sorted(files, key = lambda x:x[0])
	for file in sorted_files:
		print(f'{file[0]} {file[1]/1000:.1f}KB')
	for file in sorted_files:
		if file[1] < 3000:
			os.remove(dir_name +'/'+ file[0])
			print(f'{file[0]} removed! ')
	

remove_small_files('test_dir')
