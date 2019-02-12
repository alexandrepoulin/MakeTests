##need to modify files
import os

##needed to scramble multiple choice answers
import random
from itertools import permutations

#################################
#################################
############ Inputs #############
#################################
#################################


## Which test you want to make
testNumber = 5
prefix= "1004W17"
shortPrefix="W17"
MondayDate = [16,30,13,27,13]
monthCount = [0,0,1,1,2] ##example 8 = September, 0 = January
year = 2017
isLeapYear= False

numberOfMC = 18*4
numberOfBoard = 2
classProblems = 20
testProblems = 18

## List of class problems for each test
classProblemNums =[["21-3","21-6","21-10","21-13","21-17","21-21","21-24","21-28","21-38","21-62","22-8","22-9","22-11","22-22","22-24","22-26","22-31","22-36","22-52","22-54"],
                    ["23-2","23-14","23-20","23-22","23-26","23-30","23-34","23-36","23-44","23-46","24-4","24-8","24-14","24-16","24-19","24-26","24-36","24-44","24-76","24-88"],
                    ["25-10","25-14","25-22","25-32","25-34","25-46","26-10","26-20","26-24","26-26","26-46","26-64","27-32","27-40","27-42","27-46","27-54","27-58","27-64","27-68"],
                    ["28-4","28-6","28-10","28-18","28-28","28-36","28-44","28-46","28-50","28-60","29-10","29-12","29-16","29-18","29-36","29-40","29-44","29-48","29-52","29-62"],
                    ["30-12","30-14","30-18","30-20","30-22","30-34","30-38","30-54","30-62","30-70","31-10","31-12","31-18","31-20","31-32","31-34","31-42","31-44","31-60","31-80"]]


##Path to the directory
pathToDirectory=r'C:\Users\AlexandrePoulin\Documents\PHYS-1004\TutorialTests\2017 tests'

##Lab times
##section B = A+9, if G,G=B+9 (maybe TODO for G?)
amNoonPm = ["8:35-11:25","11:35-14:25","14:35-17:25"]
sectionTimes={1:amNoonPm[2],2:amNoonPm[2],3:amNoonPm[0],4:amNoonPm[1],5:amNoonPm[0],6:amNoonPm[0],7:amNoonPm[0],8:amNoonPm[2],9:amNoonPm[0],
              10:amNoonPm[2],11:amNoonPm[2],12:amNoonPm[0],13:amNoonPm[1],14:amNoonPm[0],15:amNoonPm[0],16:amNoonPm[0],17:amNoonPm[2],18:amNoonPm[0]} 
sectionDaysPastMonday={1:9 ,2:11,3:8 ,4:8 ,5:7 ,6:9 ,7:10,8:7 ,9:11,
                       10:2,11:4,12:1,13:1,14:0,15:2,16:3,17:0,18:4} 



#################################
#################################
########## constants ############
#################################
#################################

## keys for the days of the sections
keys = sectionDaysPastMonday.keys()

##names and numbers for dates and times
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
days = ["Monday", "Tuesday","Wednesday","Thursday","Friday"]
daysInMonth=[31,29 if isLeapYear else 28,31,30,31,30,31,31,30,31,30,31]

##spelling of numbers
byOne = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
byTen = ["zero","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

##number to word
def ntow(x):
    if x>=100:
        print("Input greater than 100: " + str(x))
        return "Error"
    if x<=19:
        return  byOne[x]
    else:
        answer = byTen[x//10]
        if x%10 != 0:
            answer +=byOne[x%10]
        return answer

##generate all acceptable permutations of the answers so that the
##answer is not in the same position
listOfPerms = list(permutations([1,2,3,4,5],5))
acceptable = [x for x in filter(lambda k: k[0]!=1 and k[1]!=2 and k[2]!=3 and k[3]!=4 and k[4]!=5,listOfPerms)]

classProblemfileNames= [x for x in map(lambda k: k[:2]+"_P"+k[3:]+"_sol",classProblemNums[testNumber-1])]
classProblemfileNamesProb= [x for x in map(lambda k: k[:2]+"_P"+k[3:]+"_prob",classProblemNums[testNumber-1])]
classProblemCommand= [x for x in map(lambda k: '\\'+ntow(int(k[:2]))+"P"+ntow(int(k[3:5])).title()+k[5:],classProblemNums[testNumber-1])]

testProblemfileNames= ["custom_"+str(testNumber)+"_"+str(x)+"_sol" for x in range(1,19)]
testProblemfileNamesProb= ["custom_"+str(testNumber)+"_"+str(x)+"_prob" for x in range(1,19)]
testProblemCommand= ['\\customT'+ntow(testNumber)+"P"+ntow(x) for x in range(1,19)]


#################################
#################################
#### Make Replacement Text ######
#################################
#################################


def dateFormat(A):
    return (days[sectionDaysPastMonday[A]%7] + ", "+ months[monthCount[testNumber-1] + (0 if (MondayDate[testNumber-1]+sectionDaysPastMonday[A])<=daysInMonth[monthCount[testNumber-1]] else 1)] + " " +
                str(MondayDate[testNumber-1]+sectionDaysPastMonday[A] - (0 if (MondayDate[testNumber-1]+sectionDaysPastMonday[A])<=daysInMonth[monthCount[testNumber-1]] else daysInMonth[monthCount[testNumber-1]])) +
                ", " + str(year)+", " + sectionTimes[A]+(" [A"+str(A) if A<=9 else " [B"+str(A-9))+"]")
dateSection=r"% Tutorial Section Dates, Times, and Names "+'\n'+ "".join([r"\addTutorialLabel{" + dateFormat(x) + r"}"   +'\n' for x in keys])


def makePerSection(section,version,end):
    text=""
    text += "%=======================\n"
    text+= "% Tutorial Section "+str(section)+" (Version "+str(version+1)+")\n"
    text+= "%=======================\n"
    text+=r"\renewcommand{\currentTutorial} 		{\getTutorialLabel{"+str(section)+"} ("+str(version+1)+")}\n"
    text+=r"\input{../TutorialTemplates/TopOfPage1alt} ~\\ ~\\"+"\n"
    for i in range(2):
        text+=r"\renewcommand{\test"+ntow(testNumber)+"MC"+ntow(18*i+section+36*version)
        text+=r" } 				{(2) "+str(i+1)+r".}	\input{../TextbookProblems/Test"+str(testNumber)
        text+=r"_Problems/"+("Solutions" if end== "sol" else "Problems")+r"/MultipleChoice/Test"+str(testNumber)+"_MC"+str(18*i+section+36*version)+"_"+end+r"}  \vspace{0.3cm} "+(r"~\\" if i == 0 else "")+" \n"
    text+=r"\clearpage"+"\n"
    text+=r"\input{../TutorialTemplates/TopOfPage2} ~\\ ~\\"+"\n"

    text+=r"\renewcommand{"+testProblemCommand[section-1]
    text+=r" } 				{(6) 1.}	\input{../TextbookProblems/Test"+str(testNumber)
    text+=r"_Problems/"+("Solutions" if end== "sol" else "Problems")+r"/testProblems/"+(testProblemfileNames[section-1] if end == "sol" else testProblemfileNamesProb[section-1])+r"}  \vspace{0.3cm} "+" \n"
    text+=r"\clearpage" + "\n"
    return text

solSectionTest= "".join([makePerSection(s,v,"sol") for s in keys for v in range(2)])
probSectionTest= "".join([makePerSection(s,v,"prob") for s in keys for v in range(2)])

def makeClassQuestions():
    text=""
    for i in range(len(classProblemfileNames)):
        text+=r"\newcommand{"+classProblemCommand[i]
        text+=r" } 				{"+classProblemNums[testNumber-1][i]+r".}	\input{../TextbookProblems/Test"+str(testNumber)
        text+=r"_Problems/Solutions/LongProblems/"+classProblemfileNames[i]+r"}  \vspace{0.3cm} "+(r"~\\" if i != classProblems else "")+" \n"
        text+=r"\pagebreak" + " \n"+ " \n"
    return text

def makeClassProbList():
    text=""
    temp=len(classProblemNums[testNumber-1])>>1
    for i in range(temp):
        text+=r"$\bullet$ "+classProblemNums[testNumber-1][i]+r"  \hspace{1cm} &$\bullet$ " + classProblemNums[testNumber-1][i+temp]+(r"\\ "+'\n' if i != temp-1 else "")
    return text

newCommandMCSection =  "% Multiple Choice Problems \n"+"".join([r"\newcommand{\test"+ntow(testNumber)+"MC"+ntow(n)+r"} 			{(2) 1.}	"+"\n" for n in range(1,1+numberOfMC)])
newCommandLPSection =  "% Long Problems \n"+"".join([r"\newcommand{"+n+r"} 			{(6) 1.}	"+"\n" for n in testProblemCommand])
probList=makeClassProbList()

onBoardReplacement = r"\newcommand{\BlackBoardA} {\textbf{Problem:}}		\input{../TextbookProblems/Test"+str(testNumber)+r"_Problems/Solutions/BlackboardProblems/BlackBoard1.tex} 	\vspace{0.3cm}   \pagebreak" + "\n"
onBoardReplacement+= r"\newcommand{\BlackBoardB} {\textbf{Problem:}}		\input{../TextbookProblems/Test"+str(testNumber)+r"_Problems/Solutions/BlackboardProblems/BlackBoard2.tex} 	\vspace{0.3cm}   \pagebreak" + "\n"

newCommandClass=makeClassQuestions()



#################################
#################################
#### scramble and make prob #####
#################################
#################################


##takes a long problem and removes the solution, generating a new file
def solToProbNotMC(filein,fileout):
    found = False
    for line in filein:
        if "% SOLUTION" in line:
            found = True
            break
        fileout.write(line)
    return found
        

##takes a multiple choice and removes the solution, generating a new file
def solToProbMC(filein,fileout):
    found = False
    for line in filein:
        if r"\input{../TutorialTemplates/" in line:
            fileout.write(r"\input{../TutorialTemplates/BoxNOAnswer}"+"\n")
            found = True
        else:
            fileout.write(line)
    return found

##helper function for scrambleAnswers which helps with some inconsistant formating
def fixAnswer(a,pos):
    answer = ""+a
    letters = {1:'a',2:'b',3:'c',4:'d',5:'e'}
    if pos==5:
        if a[0]!='e':
            answer=answer[:-3]+answer[-1:]
    if pos!=5:
        if a[0]=='e':
            if "\\\\" in answer:
                answer=answer[:-1]+answer[-1]
            else:
                answer=answer[:-1]+"\\\\"+answer[-1]
    answer=letters[pos]+answer[1:]
    return answer
        
##takes a multiple choice file, scrambles the answers and generates a new file
def scrambleAnswers(infile,outfile,probnum):
    inAnswers = False
    answerLines = []
    scrambledNumbers=random.choice(acceptable)
    numbers = {"BoxAnswerA":1,
               "BoxAnswerB":2,
               "BoxAnswerC":3,
               "BoxAnswerD":4,
               "BoxAnswerE":5}
    keys = list(numbers.keys())
    keys.sort()
    redo=False
    for line in infile:
        if r"\testoneMC" in line:
            outfile.write(r"\testoneMC"+ntow(probnum)+'\n')
            continue
        if inAnswers:
            if r"\end{minipage}" in line:
                inAnswers=False
                answersScrambled=[fixAnswer(answerLines[scrambledNumbers[j]-1],j+1) for j in range(len(scrambledNumbers))]
                for na in answersScrambled:
                    outfile.write(na)
            else:
                answerLines.append(line)
        if not inAnswers:
            if "BoxAnswer" in line:
                realAnswerPos=numbers[line[28:38]]
                newAnswerPos = scrambledNumbers.index(realAnswerPos)
                newline = line[:28]+keys[newAnswerPos]+line[38:]
                outfile.write(newline)
            else:
                outfile.write(line)   
        if "% MULTIPLE CHOICE OPTIONS" in line:
            inAnswers = True



##create new multiple choice questions by scrambling the answers
for i in range(1,1+int(numberOfMC/2)):
    mcOld=open(pathToDirectory+r"\TextbookProblems\Test"+str(testNumber)+r"_Problems\Solutions\MultipleChoice\Test"+str(testNumber)+"_MC" + str(i)+"_sol.tex","r")
    mcNew=open(pathToDirectory+r"\TextbookProblems\Test"+str(testNumber)+r"_Problems\Solutions\MultipleChoice\Test"+str(testNumber)+"_MC" + str(i+36)+"_sol.tex","w")
    scrambleAnswers(mcOld,mcNew,i+36)
    mcOld.close()
    mcNew.close()

           
## change the sols to prob for the in long problems
for i in range(1,1+testProblems):
    mcOld=open(pathToDirectory+r"\TextbookProblems\Test"+str(testNumber)+r"_Problems\Solutions\testProblems"+'\\'+testProblemfileNames[i-1]+ r".tex","r")
    mcNew=open(pathToDirectory+r"\TextbookProblems\Test"+str(testNumber)+r"_Problems\Problems\testProblems"+'\\' +testProblemfileNamesProb[i-1]+ r".tex","w")
    succ = solToProbNotMC(mcOld,mcNew)
    if not succ:
        print("ERROR: % SOLUTION tag not found in " + testProblemfileNames[i-1]+ r".tex")
    mcOld.close()
    mcNew.close()

    
## change the sols to prob for the multiple choice questions
for i in range(1,1+numberOfMC):
    mcOld=open(pathToDirectory+r"\TextbookProblems\Test"+str(testNumber)+r"_Problems\Solutions\MultipleChoice\Test"+str(testNumber)+"_MC" + str(i)+"_sol.tex","r")
    mcNew=open(pathToDirectory+r"\TextbookProblems\Test"+str(testNumber)+r"_Problems\Problems\MultipleChoice\Test"+str(testNumber)+"_MC" + str(i)+"_prob.tex","w")
    succ = solToProbMC(mcOld,mcNew)
    if not succ:
        print("ERROR: answer in MC tag not found in " + "Test"+str(testNumber)+"_MC" + str(i)+"_sol.tex")
    mcOld.close()
    mcNew.close()


#################################
#################################
### actually make replacement ###
#################################
#################################


##takes an input file, generates an output file with the expressions replaced
def replaceAll(filein,fileout,searchExp,replaceExp):
    if len(searchExp) != len(replaceExp):
        print("ERROR: search and replace different lengths. Returning.")
        return
    for line in filein:
        for i in range(len(searchExp)):
            line = line.replace(searchExp[i],replaceExp[i])
        fileout.write(line)

oldpath = pathToDirectory+r'/'+shortPrefix+r'_test_template'
newpath = pathToDirectory+r'/'+shortPrefix+r'_test_'+str(testNumber)
if not os.path.exists(newpath): os.makedirs(newpath)

fpot=open(oldpath+r'/1004W15_test1_perSection_problems_test.tex',"r")
fpnt=open(newpath+r'/'+prefix+r'_test'+str(testNumber)+'_perSection_problems_test.tex',"w")

fsot=open(oldpath+r'/1004W15_test1_perSection_solutions_test.tex',"r")
fsnt=open(newpath+r'/'+prefix+r'_test'+str(testNumber)+'_perSection_solutions_test.tex',"w")

fsoc=open(oldpath+r'/1004W15_test1_perSection_solutions_class.tex',"r")
fsnc=open(newpath+r'/'+prefix+r'_test'+str(testNumber)+'_perSection_solutions_class.tex',"w")

fTSo=open(oldpath+r'/tutorialSectionsThisTest.tex',"r")
fTSn=open(newpath+r'/tutorialSectionsThisTest.tex',"w")

fbo=open(oldpath+r'/1004W15_test1_blackboard_solutions.tex',"r")
fbn=open(newpath+r'/'+prefix+r'_test'+str(testNumber)+'_blackboard_solutions.tex',"w")
numbers=["zero","one","two","three","four","five","six","seven","eight","nine"]

replaceAll(fpot,
           fpnt,
           ["testone","Test1","%newCommandLPSection","%newCommandMCSection","%probSectionTest"],
           ["test"+str(numbers[testNumber]),"Test"+str(testNumber),newCommandLPSection,newCommandMCSection,probSectionTest])
replaceAll(fsot,
           fsnt,
           ["testone","Test1","%newCommandLPSection","%newCommandMCSection","%solSectionTest"],
           ["test"+str(numbers[testNumber]),"Test"+str(testNumber),newCommandLPSection,newCommandMCSection,solSectionTest])
replaceAll(fsoc,
           fsnc,
           ["testone","Test1","%newCommandClass","%probList"],
           ["test"+str(numbers[testNumber]),"Test"+str(testNumber),newCommandClass,probList])
replaceAll(fTSo,
           fTSn,
           [r"%dateSection", r"\newcommand{\testNumber} {1}"],
           [dateSection,r"\newcommand{\testNumber} {"+str(testNumber)+"}"])

replaceAll(fbo,
           fbn,
           ["%onBoardReplacement"],
           [onBoardReplacement])



fpot.close()
fpnt.close()
fsot.close()
fsnt.close()
fsoc.close()
fsnc.close()
fTSo.close()
fTSn.close()
fbo.close()
fbn.close()

