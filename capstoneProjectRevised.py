#Abigail Andre-St Fleur
#11/24/25
#Major Indecision Capstone project
import math

def main():
    #print a menu with 2 options (run a freshman survey or view a research summary)
    print("Would like to a) Run a freshman survery or b) Exit the program : ")
    #ask the user which option they’d like to do
    choice = input("Would like to a) Run a freshman survery or b) Exit the program: ")
    genEds = []
    textBooks = []
    fieldTrips = []
    labEquipment = []
    labSpace = []
    teachersNeeded = []
    totalFreshman = 0
    # list to hold amount of students who have already taken a course
    alrTaken = []
    # variable to hold the student teacher ratio
    studentTeacher = 0
    
    #FUNCTIONS
    #for when no choice is actually selected
	def noChoice(choice):
		while(choice != 'a' and choice != 'b' and choice != 'c'):
			choice = input("What you entered is not an option. Would like to a) Run a freshman survery again b) Exit the program or c) View the research summary again: ") 
    	return choice
	#create function (avgRequirement) to find avg of students who have met requirements in each subject
    def avgRequirement(estimated, total):
        needToTake = 0
        #subtracts the estimated number of freshman who have completed a gen ed requirement from the total number of freshman in the incoming class
        needToTake = int(total) - int(estimated)
            
        #returns the estimated total of freshman who still need to take a course/ gen ed
        return needToTake
    
	#based on function avgRequirement make another function (resources) used determine what number of resources are needed for the students who are taking the gen ed courses
    def resources(course, estimated, total):
            
        books = 0
        trips = 0
        labEquip = 0
        labspa = 0
        
        
        #uses the function avgRequirement to determine how many students need to take course
        studentsNeeding = avgRequirement(estimated, total)
        
        #using that number, you extract what resources are needed for that course based on the list made containing required resources
        #courseNumber is gonna be used as the reference number for each course
        #the course number is based of its index in the gen ed list
        courseNumber = genEds.index(course)
        
        if(textBooks[courseNumber] == 'y'):
            books = studentsNeeding
        if(labEquipment[courseNumber] == 'y'):
            labEquip = studentsNeeding
        if(fieldTrips[courseNumber] == 'y'):
            trips = studentsNeeding * 100
            # making $100 like the avgerage cost for one student to go on a field trip
        if(labSpace[courseNumber] == 'y'):
            labspa = studentsNeeding * 150
            # making 150 sq ft the average needed per student in a lab
        
        #returns the resources needed in a cute print statement
        return ("The course " + str(course) + " requires: \nTextbooks: " + str(books) + "\nLab Equipment: " + str(labEquip) + " units \nTrips: $" + str(trips) + "\nLab Space: " + str(labspa) + " sq ft")
    
    #based on avgRequirement make another function (classSections) used to determine the number of teachers needed for each subject based on the school's teacher:student ratio
    def classSections():
        teachers = []
         
        #uses the function avgRequirement to determine how many students need to take a course
        for classes in genEds:
            studentsNeeding = avgRequirement(alrTaken[genEds.index(classes)], totalFreshman)
            
            #uses that number to then determine how many teachers are needed for each course
            teachers.append(int(studentsNeeding)/int(studentTeacher))
        return teachers
	
	#if the user picks freshman survey
    choice = noChoice(choice)
	while(choice == 'a'):
        #Ask how many people there are in the incoming freshman class to the college
        totalFreshman = int(input("How many people are the in the incoming freshman class? "))
        
        #ask how many of the incoming freshman class have college credits from high school (Such as AP, IB, dual enrollment courses, etc.)
        collegeCredit = int(input("What is the estimate for total students who already have college credits from high school (Like AP, IB, dual enrollment courses, etc.) "))
        
        #ask what are the college's gen ed requirements (english, writing, foreign language, etc.)
        addClass = input("Do you have a general education requirement course to add y or n? ")
        while(addClass == 'y'):
        
            #add the gen eds to a list
            className = input("What is the name of the general education course? ")
            genEds.append(className)
            addClass = input("Do you have another general education requirement course to add y or n? ")

        #ask what resources their gen ed courses need (textbooks, field trips, lab equipment, lab space)
        for classes in genEds:
            #ask what resources are needed for each individual gen ed course
            #(Whether it requires a textbook, lab space, lab equipment, or special software)
            textbook = input("Does " + classes + " require a textbook y or n? ")
            fieldtrips = input("Does " + classes + " require field trips y or n? ")
            labspace = input("Does " + classes + " require lab space y or n? ")
            labequipment = input("Does " + classes + " require lab equipment y or n? ")
            
            #Store the resource stuff in separate lists that follow the same order as the list of course names
            textBooks.append(textbook)
            fieldTrips.append(fieldtrips)
            labSpace.append(labspace)
            labEquipment.append(labequipment)
            
        #ask to estimate how many freshman have already met each individual requirement
        for classes in genEds:
            taken = input("About how many incoming freshman have already taken " + classes + "? ")
            alrTaken.append(taken)
        
        #ask what is the student teacher ratio
        studentTeacher = int(input("What is the average student teacher ratio for large lecture halls (writing 100 in the box means 100 students per teacher) "))
        
        #based on classSections calculate how many teachers are needed
        teachersNeeded = classSections()
        
        #determine how much lab space is needed
        
        print("Thank you for completing the freshman survey for your incoming freshman class") 

        #take the user back to the main menu
        choice = input("Would like to a) Run a freshman survery again b) Exit the program or c) View the research summary: ")
		
    #If the user picks view research summary
    choice = noChoice(choice)
	while(choice == 'c'):

        #Print out the subject name, amount of students needing the course, amount of class sections required, amount of teachers, required and the resources needed for every gen ed course in the list. Then print the total amount of teachers needed across all subjects
        for classes in genEds:
            print(classes + " CourseNumber: " + classes[0:2] + str(genEds.index(classes)))
            print(resources(classes, alrTaken[genEds.index(classes)], totalFreshman))
            print("The course requires " + str(round(teachersNeeded[genEds.index(classes)]) + 1) + " teachers and class sections")
            print("Of the freshman class containing " + str(totalFreshman) + " students, " + str(alrTaken[genEds.index(classes)]) + " have already taken this course or it's equivalent")
            print("Of the freshman class containing " + str(totalFreshman) + " students, " + str(totalFreshman - int(alrTaken[genEds.index(classes)])) + " still need to take this course")
        #Using the calculations done by avgRequirement, resources, and classSections then output the data for about how much the school will need in terms of course resources, teachers, and class sections for the majority of their incoming freshman class.
        
        #Take the user back to the main menu
        choice = input("Would like to a) Run a freshman survery again b) Exit the program or c) View the research summary again: ")
		break
    
	choice = noChoice(choice)
	#if the user chooses to exit the program
	while(choice == 'b'):
        print("Thank you for contributing to your freshman class research and hope you gained helpful insight as to what you'll need for the upcoming school year")
        break
	
    #End program
main()

