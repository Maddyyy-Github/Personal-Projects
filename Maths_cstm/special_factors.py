input_number = 0
while input_number == 0:
    try:
        input_number = int(input("Enter a number: "))
    except:
        print("Oops! Something went wrong with your input!\n Try again...")

class CheckNumSpec():
    def __init__(self):
        self.very_spec = "\nThat's special, a little too much! \nBecause it's factors add up to itself \n&\n(According to me) It only has 1 factor, itself."
        self.spec = "\nThe given number is special.\nBecause the given number's factors add up to that number!"
        self.not_spec = "\nOkay, nothing much -_-"

    def check_num_spec(self, input_number):
        """type 1: input a number, check whether it is a special guy"""

        #The reason we need to filter out '0' is that it can cause problem during 0 division error.
        if input_number == 0:
            return self.very_spec
            #reason I say 0 does have a factor is because 0*0 (both are integers) = 0
            #All other integers multiplied ny 0 also give 0, but they aren't smaller than 0!
        else:
            #Listing all the factors
            factor_list = []
            for number in range(1, (input_number+1)):
                if input_number%number == 0:
                    factor_list.append(number)

            #Summing the factors (excluding the number itself) up
            factor_sum = 0
            for factor in factor_list[:-1]:
                factor_sum += factor
            #returning results
            if factor_sum == factor_list[-1]:
                return self.spec
            else:
                return self.not_spec


    def check_spec_num_in_r(self, range_max, range_min=1):
        """Type #2 input a range / maximum number of a range and find out all the special numbers in range"""
        flag = True
        special_numbers = []
        spec_id = [self.spec, self.very_spec]
        not_spec_id = [self.not_spec]
        for number in range(range_min, range_max):
            if self.check_num_spec(number) in spec_id :
                special_numbers.append(number)
            elif self.check_num_spec(number) in not_spec_id:
                pass
            else:
                flag = False
        return_mssg = ""

        if flag:
            if len(special_numbers) == 0:
                return_mssg = "There are no special numbers"
            if len(special_numbers) == 1:
                return_mssg = f"{special_numbers[0]} was the only special number we could find."
            if len(special_numbers) > 1:
                return_mssg = "The following are the special numbers we could find: "
                for special_num in special_numbers :
                    return_mssg += "\n" + str(special_num)

        return return_mssg





            
            
special_num_check = CheckNumSpec()
print(special_num_check.check_spec_num_in_r(input_number))
        





