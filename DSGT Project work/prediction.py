from matplotlib import pyplot as plt
import webbrowser

#chrome_path = 'C:/Users/Shubham/AppData/Local/Programs/Python/Python36/chromedriver.exe'
f = open("register.txt", "a")
print("                                                -- Weclcome -- ")
print("")
print("* Enter your details * ")
m_name = input("Enter your name -> ")
age = input("Enter your age -> ")
symptoms = input("Enter the symptomes->")
#print(symptoms) 
f.write("Name" + ":" + str(m_name)+"\n")
f.write("Age" + ":" + str(age) + "\n")
f.write("symptoms" + ":" + str(symptoms) + "\n")  
print("")
 
def string1(val) :
    li = list(val.split(" "))
    return li

inputValueArr = string1(symptoms)    
#inputValueArr = ['cough', 'fever', 'sore throat']
list = [['Influenza', 'cough', 'headache', 'sore throat'],
        ['Food Poisoning', 'weakness', 'fever','sore throat','headache'],
        ['Diarrhea','watery stool','vomiting','abdominal cramps','belly pain']]


def predict() :	
	global Diseasepredict
	value = 0
	inputVal = 0
	countArr = []
	diseaseList = []
	for i in range(3) :
		for inputVal in inputValueArr :
			#print(inputVal)
			if inputVal in list[i] :
				value = value+1

		countArr.append(value)
		value = 0
	print(countArr)
	MaxSymtomsCount = max(countArr)
	print(MaxSymtomsCount)
	indexCount = countArr.index(MaxSymtomsCount)
	Diseasepredict= list[indexCount][0] 
	print('Disease : ', Diseasepredict)
	f.write("Disease Prescribed" + ":" + str(Diseasepredict)+ "\n"+"\n")
	f.close()
	for i in range(3) :
		diseaseList.append(list[i][0])

	plt.title('Prbability')	
	plt.xlabel('Disease')
	plt.ylabel('count')

	plt.bar([diseaseList[0],diseaseList[1],diseaseList[2]],[countArr[0],countArr[1],countArr[2]])
	plt.show()

def medicines() :
	url = 'https://www.1mg.com/otc/bakson-s-b1-influenza-fever-drop-otc387989?gclid=EAIaIQobChMI5NHAubfh4QIVzROPCh0wUgdaEAYYASABEgKKD_D_BwE'
	url1 = 'https://www.tandfonline.com/doi/full/10.3109/10717544.2011.635721'
	url2 = 'https://www.blinkhealth.com/tamiflu'
	url3 = 'https://www.1mg.com/drugs/crotorax-cream-148065?gclid=EAIaIQobChMItpDX1eri4QIVxhaPCh0MZgDAEAQYASABEgIx2_D_BwE'
	url4 = 'https://www.amazon.com/Pepto-Bismol-Original-Symptom-Including-Diarrhea/dp/B000GCJXIW'

	print("                                    ** SUGGESTED TREATMENT AND MEDICINES **               ")
	print("")
	if(Diseasepredict == "Influenza") :
		print("** Suggestions **")
		print("> Get a flu shot." )
		print("> Practice good health habits.")
		print("> Try flu antiviral drugs.")
		print("> Maintain your immune system " )
		print("")
		print("** Medicines **")
		print("Rapivab")
		print("Relenza")
		print("Oseltamivir phosphate")
		print("-----------------------------------------------------------------")
		ch = int(input("1.visit website 2.stop"))
		if(ch == 1) :
			webbrowser.open(url)
		
					

	elif(Diseasepredict == "Food Poisoning") :
		print("** Suggestions **")
		print("> Drink plenty of liquids")
		print("> Ensure fluid intake even if vomiting persists")
		print("> Start with blander foods(cereal, rice, toast and bananas)")
		print("** Medicines **")
		print("Ioperamide")
		print("Metoclopramide")
		print("Chlorpromazine")
		print("-----------------------------------------------------------------")
		ch = int(input("1.visit website 2.stop"))
		if(ch == 1) :
			webbrowser.open(url1)


	elif(Diseasepredict == "lung problems")	:
		print("** Suggestions **")
		print("> Don't Smoke")
		print("> Avoid Exposure to Indoor Pollutants That Can Damage Your Lungs")
		print("> Minimize Exposure to Outdoor Air Pollution")
		print("> Get Regular Healthcare")
		print("** Medicines **")
		print("Anticholinergics")
		print("Steroid Pills")
		print("Inhaled Steroids")
		print("-----------------------------------------------------------------")
		ch = int(input("1.visit website 2.stop"))
		if(ch == 1) :
			webbrowser.open(url2)

	elif(Diseasepredict == "skin problems") :
		print("** Suggestions **")
		print("> Protect yourself from the sun")	
		print("> Treat your skin gently")
		print("> Eat a healthy diet")	
		print("** Medicines **")
		print("Clotrimazole")
		print("ketoconazole")
		print("terbinafine")
		print("-----------------------------------------------------------------")
		ch = int(input("1.visit website 2.stop"))
		if(ch == 1) :
			webbrowser.open(url3)
	elif(Diseasepredict == "Diarrhea") :
		print("** Suggestions **")
		print("> Avoid milk or milk-based products, alcohol, apple juice, and caffeine")
		print("> Avoid eating food from street vendors")
		print("> Never eat raw or undercooked meat or seafood")
		print("** Medicines **")
		print("loperamide")
		print("bismuth subsalicylate")
		print("Kaopectate")
		print("Pepto-Bismol")
		print("-----------------------------------------------------------------")
		ch = int(input("1.visit website 2.stop"))
		if(ch == 1) :
			webbrowser.open(url4)
			

	else :
		print("No drugs found")	



#plt.plot(['cough', 'fever', 'sore throat'],[countArr[0], countArr[1], countArr[2])


	#plt.bar([diseaseList[0],diseaseList[1]],[countArr[0],countArr[1]])


symptoms_a = []
symptoms_b = []
symptoms_c = []

commonsymptomes_ab = []
commonsymptomes_bc = []
commonsymptomes_ac = []
commonsymptomes_abc = []

 
 

def patient() :
	AB = 0
	BC = 0
	AC = 0
	ABC = 0
	#T = input("Enter the total number of researchers -> ")
	na = int(input("Enter total nubmer of symptoms of disease Food Poisoning ->"))
	for i in range(na) :
		str_a = input("Enter the symptom of disease Food Poisoning ->")
		symptoms_a.append(str_a)
	print(symptoms_a)

	nb = int(input("Enter total nubmer of symptoms for disease Diarrhea ->"))
	for i in range(nb) :
		str_b = input("Enter the symptom of disease Diarrhea ->")
		symptoms_b.append(str_b)
	print(symptoms_b)	
	
	nc = int(input("Enter total nubmer of symptoms for disease Influenza ->"))
	for i in range(nc) :
		str_c = input("Enter the symptom of disease Influenza ->")
		symptoms_c.append(str_c)
	print(symptoms_c)

	for i in range(na) :
		for j in range(nb) :
			if(symptoms_a[i] == symptoms_b[j]) :
				AB = AB+1
				commonsymptomes_ab.append(symptoms_a[i])

	for i in range(nb) :
		for j in range(nc) :
			if(symptoms_b[i] == symptoms_c[j]) :
				BC = BC+1
				commonsymptomes_bc.append(symptoms_b[i])

	for i in range(na) :
		for j in range(nc) :
			if(symptoms_a[i] == symptoms_c[j]) :
				AC = AC+1
				commonsymptomes_ac.append(symptoms_a[i])			

	for i in range(na) :
		for j in range(nb) :
			for k in range(nc) :
				if(symptoms_a[i] == symptoms_b[j] and symptoms_b[j] == symptoms_c[k] and symptoms_a[i] == symptoms_c[k]) :
					ABC = ABC + 1
					commonsymptomes_abc.append(symptoms_a[i])

	totalSymptomsCount = na+nb+nc-AB-BC-AC+ABC	
	print("------------------------------------>>>>>>>>>>>>>>>>-----------------------------------------")
	print("")			
	print("Number of symptomes that are common in Food Poisoning and Diarrhea : ", AB)
	print("Common symptoms between Food Poisoning and Diarrhea                :", commonsymptomes_ab)
	print("")
	print("--------------------------------------------------------------------------------------------")
	
	print("Number of symptomes that are common in Diarrhea and Influenza : ", BC)
	print("Common symptoms between Diarrhea and Influenza                :", commonsymptomes_bc)
	print("")
	print("--------------------------------------------------------------------------------------------")

	print("Number of symptomes that are common in Food Poisoning and Influenza : ", AC)
	print("Common symptoms between Food Poisoning and Influenza :", commonsymptomes_ac)
	print("")
	print("---------------------------------------------------------------------------------------------")

	print("Number of symptomes that are common in Food Poisoning, Diarrhea and Influenza : ", ABC)
	print("Common symptoms between Food Poisoning, Diarrhea and Influenza :", commonsymptomes_abc)
	print("")
	print("----------------------------------------------------------------------------------------------")

	print("Total count of symptoms : ", totalSymptomsCount)
	print("")
	print("_________________________________________________________________________________________________")
	



def register() :
	print("********************* Enter your details *********************")
	global name
	global age
	global blood_group
	global gender
	name = input("Enter your name -> ")
	age = input("Enter your age -> ")
	gender = input("Enter Gender -> ")
	
	blood_group = input("Enter blood group ->")

def anasthesia() :
	register()
	print(name)
	weight = float(input("Enter your weight in kg->"))
	lbs = weight*2.205
	print("Weight in lbs --> ", lbs)
	Atropine = 0.02*lbs
	Acepromazine = 0.125*lbs
	Ketamine = 5*lbs
	Propofol = 3*lbs
	print("                                    >> Patient Report <<           ")
	print("")
	print("Name        :", name)
	print("Age         :", age)
	print("Blood Group :", blood_group)
	print("Gender      :", gender)
	print("Weight      :", weight)

	print("------------------------------------------------------")
	print("| Atropine     : ",Atropine, "mg                       ")
	print("| Acepromazine : ",Acepromazine, "mg                   " )
	print("| Ketamine     : ",Ketamine, "mg                       " )
	print("| Propofol     : ",Propofol, "mg                       " )
	print("-------------------------------------------------------")



from collections import namedtuple,deque
import webbrowser

g_c=0

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')
Vertex = namedtuple('Vertex', 'vertex , website')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    global g_c
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path
def test() :
	url1 = 'https://www.suryahospital.net/'
	url2 = 'http://www.accordhospitals.com/accordsdh/'
	url3 = 'https://www.rankahospital.com/'
	url4 = 'https://sahyadrihospital.com'
	url5 = 'https://www.cloudninecare.com'
	l=["a","b","c","d","e"] #hospital
	w=["Accord hospitals","Ranka Hospital","Surya Hospital","Sahyadri Hospital","Cloud Nine Care"] #websites
	graph = Graph([
	    (l[0], l[1], 6),  (l[0], l[2], 9),  (l[0], l[3], 14), (l[1], l[2], 10),
	    (l[1], l[3], 15), (l[2], l[3], 11), (l[2], l[4], 2),  (l[3], l[4], 8)])
	m=int(input('Enter your choice'))
	print(graph.dijkstra(l[0], l[m]))#change here
	print(w[m])
	if(w[m] == "Surya Hospital") :
	    webbrowser.open(url1)

	if(w[m] == "Accord hospitals") :
	    webbrowser.open(url2)
	    
	if(w[m] == "Ranka Hospital") :
	    webbrowser.open(url3)    

	if(w[m] == "Sahyadri Hospital") :
	    webbrowser.open(url4)   

	if(w[m] == "Cloud Nine Care") :
	    webbrowser.open(url5)   

	


print("                                                  * Health Service and Monitoring *           ")
while True:
	print("")
	print("1.Predict the disease")
	print("2.Show the medicines")
	print("3.Inference Engine")
	print("4.Prescribe Anasthesia drugs with quantity")
	print("5.Find shortest hospital")
	print("6.Stop")
	choice = input("> Enter your choice")

	if(choice == '1' ):
		predict()
	if(choice == '2'):
		medicines()	
	if(choice == '3'):
		patient()	
	if(choice == '4'):
		anasthesia()
	if(choice == '5') :
		test()
	if(choice == '6') :
		break		
































	#['eating or weight problems', 'W', 'fever'],
        #['lung problems','cough with blood','shortness of breath'],
        #['skin problems','redness of face','moles on skin'],

'''
	f.write("Name : ")
	f.write(name)
	f.write("Age :")
	f.write(age)
	#f.write("weight :", weight)
	#f.write("blood_group :", blood_group)
	f.write("************************************************************")
register()	

f.close()'''



'''def calc() :
	for i in range(na) :
		for j in range(nb) :
			if(symptoms_a[i] == symptoms_b[j]) :
				CA = CA+1

	for i in range(nb) :
		for j in range(nc) :
			if(symptoms_b[i] == symptoms_c[j]) :
				CB = CB+1
	print("na & nb : ", CA)
	print("bn & nc :", CB)

calc()	'''			

				








