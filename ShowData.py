import os
if __name__ == "__main__":
    for (root,dirs,files) in os.walk('Data', topdown=True):
        for f in files:		
        		print (os.path.join(root,f))