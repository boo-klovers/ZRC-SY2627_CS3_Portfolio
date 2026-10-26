class Patient:
    def __init__(self, name, billAmount):
        self._name = name
        self._billAmount = billAmount

    @property
    def billAmount(self):
        return self._billAmount

    @billAmount.setter
    def billAmount(self, newBillAmount):
        if newBillAmount > 0:
            self._billAmount = newBillAmount
        else:
            print("You cant have a negative bill lmao")

    @property
    def name(self):
        return f'Patient Name: {self._name}'

    @name.setter
    def name(self, newName):
        if not newName.isdigit():
            self._name = newName
        else:
            print("Your name cant be a number lmao")

    def calculateBillAmount(self):
        print(f'Final Bill: ₱{self._billAmount:.2f}\n')

class SeniorPatient(Patient):
    def __init__(self, name, billAmount):
        super().__init__(name, billAmount)

    def calculateBillAmount(self):
        finalBill = self.billAmount * 0.80
        print(f'Final Bill: ₱{finalBill:.2f}\n')

class PhilHealthPatient(Patient):
    def __init__(self, name, billAmount):
        super().__init__(name, billAmount)

    def calculateBillAmount(self):
        finalBill = self.billAmount * 0.85
        print(f'Final Bill: ₱{finalBill:.2f}\n')

patient = Patient("Juan Del Cruz", 15000)
senior = SeniorPatient("Maria Santos", 15000)
philH = PhilHealthPatient("Pedro Reyes", 15000)

patients = [patient, senior, philH]

for patient in patients:
    print(patient.name)
    print("Original Bill:", f'₱{patient.billAmount:.2f}')
    patient.calculateBillAmount()
