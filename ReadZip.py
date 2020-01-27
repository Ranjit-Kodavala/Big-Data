try:		
	zipSourcePath1 = 'ZIPSOURCE/zipFIle/'
	xmlFilePath = 'ZIPAR/Archive//Archive/'

	  
	  zipFiles = os.listdir(zipSourcePath1) 
	  if  len(zipFiles120) == 0:
		  print("Folder is Empty")
	  for filename in zipFiles120:
		with gzip.open(zipSourcePath1+filename, 'rb') as f_in120:
		  with open(xmlFilePath+filename+".xml", 'wb') as f_out120:          
			shutil.copyfileobj(f_in, f_out)                
  except Exception as e:
	 print(" Not Found:"+str(e))
