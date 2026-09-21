class AssignmentSubmission:
    def __init__(self, studentName: str, studentID: str, assignmentTitle: str, dueDate, grade: float = 0.0, isSubmitted: bool = False):
        self.studentName = studentName
        self.studentID = studentID
        self._assignmentTitle = assignmentTitle
        self._dueDate = dueDate
        self.__grade = grade
        self.__isSubmitted = isSubmitted
        self.__submittedFiles: list[str] = []

    def statusReport(self):
        if self.__submittedFiles == []:
            return (f"ID: {self.studentID} | Name: {self.studentName} | Status: Missing | Grade: Not Graded")
        elif self.__grade == 0.0:
            return (f"ID: {self.studentID} | Name: {self.studentName} | Status: Submitted {self.__submittedFiles} | Grade: Not Graded")
        else:
            return (f"ID: {self.studentID} | Name: {self.studentName} | Status: Submitted {self.__submittedFiles} | Grade: {self.__grade}")

    def viewFiles(self):
        if self.__submittedFiles == []:
            return (f"[WARNING] No files for {self.studentName}")
        else:
            return self.__submittedFiles

    def assignGrade(self,assignGrade = 0.0): #, checkSubmissionStatus,  getGrade
            if self.__submittedFiles == []:
                print(f"[WARNING] Cannot grade. No assignment submitted for {self.studentName}")
                
            else:
                self.__grade = assignGrade
                self.__isSubmitted = True
                print(f"The Grade {self.__grade} officially assigned to {self.studentName}.")
        

    def addFile(self, addFile):
        if self.__submittedFiles.count(addFile) > 0:
                    print(f"[WARNING] {self.studentName} has already submitted {addFile}.")
        else:
            self.__submittedFiles.append(addFile)
            print(f"[SUCCESS] {self.studentName} attached: {addFile}. Total files: {len(self.__submittedFiles)}")  

        

    def removeFile(self, removeFile):
        if self.__isSubmitted == True:
            print(f"[WARNING] {self.studentName} cannot remove files. Assignment already graded.")
        elif self.__submittedFiles.count(removeFile) == 0:
            print(f"[WARNING] {self.studentName} has not submitted {removeFile}.")
        else:
            self.__submittedFiles.remove(removeFile)
            print(f"[SUCCESS] {self.studentName} removed: {removeFile}. Total files: {len(self.__submittedFiles)}")
        
            

        

    


print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(studentName="Alex Gonzaga", studentID="pshs-1090-x", assignmentTitle="CS-101", dueDate="2026-10-01")
student2 = AssignmentSubmission(studentName="Adelle", studentID="pshs-1920-x", assignmentTitle="CS-103", dueDate="2026-10-01")
student3 = AssignmentSubmission(studentName="Juan dela Cruz", studentID="pshs-1033-x", assignmentTitle="CS-101", dueDate="2026-10-01")
student4 = AssignmentSubmission(studentName="Maria Santos", studentID="pshs-1044-x", assignmentTitle="CS-101", dueDate="2026-10-01")
student5 = AssignmentSubmission(studentName="Jose Reyes", studentID="pshs-1055-x", assignmentTitle="CS-101", dueDate="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List --- ")
student1.addFile("main.py")
student1.addFile("report.pdf")
student1.assignGrade(95)
print(f"Alex's Files: {student1.viewFiles()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.addFile("wrong_homework.docx")
student2.removeFile("wrong_homework.docx")
student2.addFile("correct_project.py")
student2.assignGrade(88)
print(f"Adelle's Files: {student2.viewFiles()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.addFile("script.py")
student3.addFile("script.py") # Should trigger private duplicate check
print(f"Juan's Files: {student3.viewFiles()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.addFile("exam_answers.pdf")
student4.assignGrade(75)
student4.removeFile("exam_answers.pdf") # Blocked by grading status
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.addFile("draft.txt")
student5.removeFile("draft.txt")
student5.assignGrade(100) # Should fail because list is empty
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.statusReport())
print(student2.statusReport())
print(student3.statusReport())
print(student4.statusReport())
print(student5.statusReport())
