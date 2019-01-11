"""def get_commande():
	commande = input('>>>')
	return commande"""
"""def split_commande(commande):
		liste=commande.split(" ")
		return liste"""
def spit_url(url):
	extension = url.split("/")
	l=len(extension)
	file=extension[l-1]
	return file
def test_input_file(argv):
	if len(argv)>2:
		if argv[2] == 'xml':
			if len(argv)==8:
				if argv[4]=='-f':
					extension = argv[5].split(".")
					#print(extension[0],extension[1])
					if len(extension)==2:
						if extension[1] != 'xml':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						return False
				if argv[4]=='-h':
					extension = argv[5].split("/")
					l=len(extension)
					file=extension[l-1]
					file1=file.split('.')
					if len(file1)==2:
						if file1[1] != 'xml':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
			if len(argv)==7:
				if argv[3]=='-f':
					extension = argv[4].split(".")
				#print(extension[0],extension[1])
					if len(extension)==2:
						if extension[1] != 'xml':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
				if argv[3]=='-h':
					extension = liste[4].split("/")
					l=len(extension)
					file=extension[l-1]
					file1=fic.split('.')
					if len(file1)==2:
						if file1[1] != 'xml':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
		if argv[2] == 'json':
			if len(argv)==8:
				if argv[4]=='-f':
					extension = argv[5].split(".")
					#print(extension[0],extension[1])
					if len(extension)==2:
						if extension[1] != 'json':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						return False
				if argv[4]=='-h':
					extension = argv[5].split("/")
					l=len(extension)
					file=extension[l-1]
					file1=file.split('.')
					if len(file1)==2:
						if file1[1] != 'json':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
			if len(argv)==7:
				if argv[3]=='-f':
					extension = argv[4].split(".")
				#print(extension[0],extension[1])
					if len(extension)==2:
						if extension[1] != 'json':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
				if argv[3]=='-h':
					extension = argv[4].split("/")
					l=len(extension)
					file=extension[l-1]
					file1=file.split('.')
					if len(file1)==2:
						if file1[1] != 'json':
							print('Erreur fichier entree:format xml attendu or format '+extension[1]+' entree')
							return False
						else:
							return True
					else:
						print 'format fichier d\'entree invalide'
						return False
		else:
			print('Erreur fichier d\'entree')
			return False
def test_output_file(argv):
	if len(argv)==7 or len(argv)==8:
		extension=argv[len(agrv)-1].split(".")
		if len(extension)==2:
			if extension[1]=='svg':
				return True
			else:
				print('Erreur fichier de sortie:format svg attendu or format '+extension[1]+' entree')
				return False
		else:
			print('Erreur fichier de sortie')
			return False
def test_commande(argv):
	if len(argv) == 8:
		if argv[0]=='XJ_Convertor':
		 	if argv[1]=='-i':
		 		if argv[3]=='-t':
		 			if argv[4]=='-f' or argv[4]=='-h':
		 				if argv[6]=='-o':
		 					return True
		 				else:
		 					print 'Erreur commande'
		 					return False
		 			else:
		 				print 'Erreur commande'
		 				return False
		 		else:
		 			print 'Erreur commande'
		 			return False
		 	else:
		 		print 'Erreur commande'
		 		return False
		else:
			print 'Erreur commande'
		 	return False
	if len(agrv)==7:
		if argv[0]=='XJ_Convertor':
		 	if argv[1]=='-i':
		 		if argv[3]=='-f' or argv[3]=='-h':
		 			if argv[5]=='-o':
		 				return True
		 			else:
		 				print 'Erreur commande'
		 				return False
		 		else:
		 			print 'Erreur commande'
		 			return False
		 	else:
		 		print 'Erreur commande'
		 		return False
		else:
			print 'Erreur commande'
		 	return False
	else:
		print 'Erreur commande'
		return False