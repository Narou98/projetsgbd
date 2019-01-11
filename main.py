import json
#import lxml
import svgwrite
import xml.etree.cElementTree as ET

def extractDataFromFile(cheminFichier):
    f = open(cheminFichier)
    strData = f.read()
    return strData

def parseJSON(data):
    jsonData = json.loads(data)
    return jsonData

def isJSONvalid(data):
    try:
        jsonData = json.loads(data)
        return True
    except:
        return False


def parsefile(file):
    parser = make_parser(  )
    parser.setContentHandler(ContentHandler(  ))
    parser.parse(file)
    

def xml_validator(file):
    try:
        parsefile(file)
        return True
    except Exception as e:
        print "le fichier ", file, "Le format XML n'est pas bonne"
        print("Voici l'erreur: %s" % e)
        return False


def parseJSON(filePath):
    file = open(filePath)
    data = file.read()
    j = json.loads(data)
    return j


def getEntites(fichier):
    files = ET.ElementTree(file = fichier)
    root = files.getroot()
    entites = {}
    for nodes in root.iter('complexType') :
        for child in nodes:
            if child.tag == "sequence": # permet de verifier si c'est une classe
                entites.update({nodes.attrib['name']:{'attributs':{}}}) #inserer le nom dans entites en initialisants ses attibuts a vide
                for attribut in child:
                    entites[nodes.attrib['name']]['attributs'].update({attribut.attrib['name']:attribut.attrib['type']}) 

    return entites


def getHeritEntites(fichier):
    files = ET.ElementTree(file = fichier)
    root = files.getroot()
    class_herit = {}
    for nodes in root.iter('complexType') :
        for child in nodes:
            if child.tag == "complexContent":    

                for attribut in child:
                    elem = attribut.find('element') #recuperer verifier s'il a un enfant de type <element>
                    if elem != None: 
                        class_herit.update({nodes.attrib['name']:{'attributs':{}}}) #inserer le nom dans class_herit{}
                        for element in attribut:
                            class_herit[nodes.attrib['name']]['attributs'].update({element.attrib['name']:element.attrib['type']}) #recuperer l'ensemble des ses attributs

                    else: 
                        class_herit.update({nodes.attrib['name']:{'attributs':{}}})
                        class_herit[nodes.attrib['name']]['attributs'] = {} #afficher de quelle classe elle herite
    return class_herit

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

def getStereotypes(fichier):
    files = ET.ElementTree(file = fichier)
    root = files.getroot()
    stereotypes = {}
    for nodes in root.iter('complexType') :
        for child in nodes:
            if child.tag == "simpleContent": #verifier si c'est une classe permet de declarer un type de donnees
                stereotypes.update({nodes.attrib['name']:{'attributs':{}}})
                for attributs in child:
                    for attribut in attributs:
                        stereotypes[nodes.attrib['name']]['attributs'].update({attribut.attrib['name']:attribut.attrib['type']}) #recuperer l'ensemble des ses attributs

    return stereotypes


def getRelations(fichier):
    files = ET.ElementTree(file = fichier)
    root = files.getroot()
    relations = {}
    for nodes in root.iter('complexType') :
        for child in nodes:
            if child.tag == "relation": # permet de verifier si c'est une classe
                relations.update({child.attrib['name']:{'multiplicite':{}}}) #inserer le nom dans entites en initialisants ses attibuts a vide
                for attribut in child:
                    for seq in attribut:
                        relations[child.attrib['name']]['multiplicite'].update({seq.attrib['name']:(seq.attrib['minOccurs'],seq.attrib['maxOccurs'])})
    return relations



#Main

myJsonData = getEntites("input.xml")
relations = getRelations("input.xml")
listEntites = []

for i in myJsonData:
    for key in myJsonData[i].keys():
       listEntites.append(key)

#print(listEntites)

svg_document = svgwrite.Drawing(filename = "svgFile.svg",
                                debug = True)
i=0
entityCoordsList = []
for entite in myJsonData:
    listAttributs = []
    for key in myJsonData[entite]['attributs']:
        listAttributs.append(key)
        print('\t\t' + key)

    nbAttributs = len(myJsonData[entite]['attributs'])
    print(entite)
    for j in range(nbAttributs):
        for key in myJsonData[entite]['attributs']:
            print('\t\t')
    if (i % 2 == 0):
        # Creation du rectangle contenant les infos de l'entite
        svg_document.add(svg_document.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))
        entityCoords = {
            "nomEntite": entite,
            "coordX": 10,
            "coordY": i*150 + 10
        }
        entityCoordsList.append(entityCoords)

        svg_document.add(svg_document.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))

        svg_document.add(svg_document.text(entite,
            insert=(20, i*150 + 30),
            stroke='none',
            fill="rgb(42, 42, 42)",
            font_size='15px',
            font_weight="bold")
        )


        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                insert=(20, i*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    else:
        # Creation du rectangle contenant les infos de l'entite
        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))

        entityCoords = {
            "nomEntite": listEntites[i],
            "coordX": 400,
            "coordY": (i - 1)*150 + 10
        }
        entityCoordsList.append(entityCoords)

        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))

        # Affichage du nom de l'entite
        svg_document.add(svg_document.text(entite,
            insert=(410, (i - 1)*150 + 30),
            stroke='none',
            fill="rgb(42, 42, 42)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                insert=(410, (i - 1)*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    i+=1




# print(svg_document.tostring())
l = 0;
print(relations)
for i in relations:
    # Recuperations des differentes associations
    #nbAssocs = len(relations[i]['multiplicite']['associations'])
    for j in relations[i]['multiplicite']:

        # for key in myJsonData[i][listEntites[i]]['relations']['associations'][j].keys():
        #     listAssocs.append(key)
        #     print(key)
        nomAutreEntite = relations[i]['multiplicite'][j][0]
        cardDeb = relations[i]['multiplicite'][j][0]
        cardFin = relations[i]['multiplicite'][j][1]
        nomAssoc = j
        
        for k in range(len(entityCoordsList)):
            print(i)
            print(j)
            print(entityCoordsList[k])
            print(nomAutreEntite)
            if j==entityCoordsList[k]["nomEntite"]:
                debutLigneX = entityCoordsList[k]['coordX'] + 150
                debutLigneY = entityCoordsList[k]['coordY'] + 65
                finLigneX = entityCoordsList[k]['coordX'] +230
                finLigneY = entityCoordsList[k]['coordY'] + 65

                svg_document.add(svg_document.line(
                    (debutLigneX, debutLigneY),
                    (finLigneX, finLigneY),
                    stroke_width = "2",
                    stroke="rgb(15, 15, 15)"))

                # Affichage de la cardinalite depart
                svg_document.add(svg_document.text(cardDeb,
                    insert=(debutLigneX + 10, debutLigneY - 10),
                    stroke='none',
                    fill="rgb(15, 15, 15)",
                    font_size='15px',
                    font_weight="bold")
                )

                # Affichage de la cardinalite arrivee
                svg_document.add(svg_document.text(cardFin,
                    insert=(finLigneX - 30, finLigneY - 10),
                    stroke='none',
                    fill="rgb(15, 15, 15)",
                    font_size='15px',
                    font_weight="bold")
                )

                # Affichage du nom de l'association
                svg_document.add(svg_document.text(nomAssoc,
                    insert=((finLigneX - debutLigneX) / 2 + debutLigneX, finLigneY - 10),
                    stroke='none',
                    fill="rgb(15, 15, 15)",
                    font_size='15px',
                    font_weight="bold")
                )

svg_document.save()
