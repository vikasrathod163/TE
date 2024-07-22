import random


class ExpertSystem:
    def __init__(self, symptoms, diseases):
        self.symptoms = symptoms
        self.diseases = diseases
        self.current_symptom = None
        self.current_disease = None


    def start(self):
        self.current_symptom = random.choice(self.symptoms)
        print("What is the severity of your {}? (1-10)".format(self.current_symptom))
        severity = int(input())


        if severity > 5:
            self.current_disease = self.diseases[self.current_symptom]
            print("You may have {}.".format(self.current_disease))
        else:
            print("You probably don't have {}.".format(self.current_disease))


        self.ask_next_question()


    def ask_next_question(self):
        if self.current_disease is not None:
            print("Do you have any other symptoms? (y/n)")
            answer = input()


            if answer == "y":
                self.current_symptom = random.choice(self.symptoms)
                print("What is the severity of your {}? (1-10)".format(self.current_symptom))
                severity = int(input())


                if severity > 5:
                    self.current_disease = self.diseases[self.current_symptom]
                    print("You may have {}.".format(self.current_disease))
                else:
                    print("You probably don't have {}.".format(self.current_disease))


                self.ask_next_question()
            else:
                print("Thank you for using the expert system.")
        else:
            print("I'm sorry, I can't help you with your diagnosis.")


if __name__ == "__main__":
    symptoms = ["fever", "cough", "sore throat", "runny nose", "headache"]
    diseases = {
        "fever": "flu",
        "cough": "cold",
        "sore throat": "strep throat",
        "runny nose": "allergies",
        "headache": "migraine"
    }


    expert_system = ExpertSystem(symptoms, diseases)
    expert_system.start()
