def personal_info():
    yes = set(['yes', 'y', 'ye'])
    no = set(['no', 'n'])
    answerAge = input("What is your age? ")
    while len(answerAge) < 1 or answerAge.isnumeric() == False:
        answerAge = input("Please type only numbers and then hit 'ENTER': no letters, symbols, or spaces. ")
        return answerAge
        
    answerWeight = input("What is your weight in pounds? ")
    while len(answerWeight) < 1 or answerWeight.isnumeric() == False:
        answerWeight = input("Please type only numbers and then hit 'ENTER': no letters, symbols, or spaces. Don't worry. You do not need to re-enter your age. ")
            
    answerHeightFeet = input("Now, let's discuss your height. " + "\n" + "Please enter your height in 'feet' first and then hit 'ENTER'. We will ask about 'inches' afterwards. Feet: ")
    while len(answerHeightFeet) < 1 or answerHeightFeet.isnumeric() == False:
        answerHeightFeet = input("Please enter only the requested value, and don't worry. Your previously submitted data are saved in this session. ")
            
    answerHeightInches = input("Inches: ")
    while len(answerHeightInches) < 1 or answerHeightInches.isnumeric() == False:
        answerHeightInches = input("Please enter only the requested value. Note that your previously submitted data are saved in this session. ")

    print("So you are " + answerAge + " years old, your weight is " + str(answerWeight) + " pounds, and your total height is " + str(answerHeightFeet) + " feet and " + str(answerHeightInches) + " inches. ")

    answerAge = int(answerAge)
    answerWeight = int(answerWeight)
    answerHeightFeet = int(answerHeightFeet)
    answerHeightInches = int(answerHeightInches)

    def total_height(feet, inches):
        customerHeight = 12 * feet + inches
        return customerHeight        
    # convert height-inches input to inches.
        

    customer_total_height = total_height(answerHeightFeet, answerHeightInches)

    def BMI(weight,height):
        customer_BMI = (weight/(height ** 2)) * 703
        return customer_BMI
        
    customer_BMI = BMI(answerWeight,customer_total_height)
    customer_BMI_hundred = customer_BMI * 100
    customer_BMI_hundred = int(customer_BMI_hundred)
    customer_BMI_hundred = customer_BMI_hundred/100

    # slice int(customer_BMI) to two decimal points. 
    user_BMI = input("We have calculated your Body Mass Index. It is " + str(customer_BMI_hundred) + ". Would you like a personalized detail about your BMI? ").lower()

    if user_BMI in no:
        print("That is fine. Let's move on.")
    elif user_BMI in yes:
        print("Here is more detail about your health." )
        if customer_BMI <= 18.5:
            print("You are at the lower end of the spectrum for you are underweight since normal BMI is between 18.5 to 24.9." + "\n" + "You need to eat more and gain weight. ")
        elif customer_BMI > 18.5 and customer_BMI <= 24.9:
            print("You are at the medium spectrum of BMI: you have normal weight as normal BMI is between 18.5 to 24.9." + "\n" + "Congratulations, and keep it up! ")
        elif customer_BMI > 25 and customer_BMI <= 29.9:
            print("Your BMI is high: this means you are overweight. Normal BMI is between 18.5 to 24.9." + "\n" + "Please look into changing your diet and your lifestyle. ")
        else:
            print("Your BMI is very-high, which means you are obese. Normal BMI is between 18.5 to 24.9." + "\n" + "Please look into changing your diet and your lifestyle and see a dietitian or a doctor if needing an assistance. ")
    else:
        while (user_BMI not in no) or (user_BMI not in yes):
            user_BMI = input("Please type YES or NO. ").lower()
            if user_BMI in no:
                print("That is fine. Let's move on. We will now discuss your symptoms. ")
                break
            if user_BMI in yes:
                print("Here is more detail about your health." )
                if customer_BMI <= 18.5:
                    print("You are at the lower end of the spectrum for you are underweight. Normal BMI is between 18.5 to 24.9." + "\n" + "You need to eat more and gain weight. ")
                elif customer_BMI > 18.5 and customer_BMI <= 24.9:
                    print("You are at the medium spectrum of BMI: you have normal weight as normal BMI is between 18.5 to 24.9." + "\n" + "Congratulations, and keep it up! ")
                elif customer_BMI > 25 and customer_BMI <= 29.9:
                    print("Your BMI is high: this means you are overweight. Normal BMI is between 18.5 to 24.9." + "\n" + "Please look into changing your diet and your lifestyle. ")
                else:
                    print("Your BMI is very-high, which means you are obese. Normal BMI is between 18.5 to 24.9." + "\n" + "Please look into changing your diet and your lifestyle and see a dietitian or a doctor if needing an assistance. ")
                break
 
     
 
def clinic():
        print("Welcome to your personalized online clinic." + "\n" + "We will go through a series of questions to check your symptoms, but first, I will need to ask you some personal questions.")

        yes = set(['yes', 'y', 'ye'])
        no = set(['no', 'n'])
        
        patient_consent = input("Would this be OK with you? ").lower() 
        if patient_consent in no:
            print("OK, that's fine. Let's move on and discuss your symptoms. ")
            patient_consent in no
        elif patient_consent in yes: 
            print("OK, let's begin with your age. ")
            personal_info()
            
        else:
            while patient_consent not in yes or patient_consent not in no: 
                patient_consent = input("Please type YES or NO: ").lower()
                if patient_consent in no:
                    print("OK. Let's move on and discuss your symptoms. ")
                    break
                if patient_consent in yes:
                    print("OK, let's begin with your age. ")         
                    personal_info()
                    break
# If-then statements above made more compact by avoiding repetitions.             
        
 
        print("\n" + "Now, we have a series of questions to ask about your health. ")
        fever = ['sweating', 'shivering', 'headache', 'muscle aches', 'loss of appetite', 'dehydration', 'general weakness', 'hallucinations', 'confusion', 'irritability', 'convulsions', 'dehydration'];
        yes = set(['yes', 'y', 'ye'])
        no = set(['no', 'n'])
        patient_consent2 = input("Would it be OK if I show you a list of symptoms? You can then determine whether or not you have them. ").lower()
        if patient_consent2 in no:
            patient_response01 = input("That's fine. What symptoms do you have? ")
            print("It seems that we do not have enough resources to help you further. Please go to a local clinic or try to get some rest. ")
            print("Good bye!")
            patient_consent2 in no
            return patient_consent2
        elif patient_consent2 in yes:
            print("Great. First, take a look at this list: ")
            for i in range(len(fever)):
                print(fever[i])
            yes = set(['yes', 'y', 'ye'])
            no = set(['no', 'n'])
            patient_fever_response = input("Do you have any of these symptoms? ").lower()
            if patient_fever_response in no:
                patient_response01 = input("That's fine. What symptoms do you have? ")
                print("It seems that we do not have enough resources to help you further. Please go to a local clinic or try to get some rest. ")
                print("Good bye!")
                patient_consent2 in no
                return patient_consent2
            if patient_fever_response in yes:
                print("It is possible that you have the flu. Please go to a local clinic for further assistance. ")
                patient_fever_response in yes
                return patient_fever_response

        else:
            while (patient_consent2 not in yes) or (patient_consent2 not in no):
                patient_consent2 = input("Please type YES or NO: ").lower()
                if patient_consent2 in no:
                    patient_response01 = input("That's fine. What symptoms do you have? ")
                    print("It seems that we do not have enough resources to help you further. Please go to a local clinic or try to get some rest. ")
                    print("Good bye!")
                    break
                if patient_consent2 in yes:
                    print("Great. First, take a look at this list: ")
                    for i in range(len(fever)):
                        print(fever[i])  
                    patient_fever_response = input("Do you have any of these symptoms? ").lower()
                    if patient_fever_response in no:
                        patient_response01 = input("That's fine. What symptoms do you have? ")
                        print("It seems that we do not have enough resources to help you further. Please go to a local clinic or try to get some rest. ")
                        print("Good bye!")
                        patient_fever_response in no
                        return patient_fever_response
                    elif patient_fever_response in yes:
                        print("It is possible that you have the flu. Please go to a local clinic for further assistance. ")
                        patient_fever_response in yes
                        return patient_fever_response
                    else:
                         print("We cannot understand you. Please go to a local clinic for further assistance. ")
                         break
clinic()


