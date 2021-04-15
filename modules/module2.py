# Module 2 Class
# __author__ = Calmantara
# created = 15th April 2021
# skill test purpose

class Module2:
    def __init__(self):
        '''
            Class represents second solution
        '''
        pass

    def devide_num(self,
                   num1: int,
                   num2: int) -> int:
        '''
            Function to devide two integer
            return exact integer num
        '''
        if num2 == 0:
            raise ValueError("Cannot devide by zero")
        return num1 / num2

    def get_length(self,
                   arr: list) -> int:
        '''
            Funtion to get length of array
        '''
        return len(arr)

    def check_array(self,
                    arr: list,
                    num: int) -> list:
        '''
            Function to return all numbers in list
            that does not return <0
        '''

        arr_length = self.get_length(arr=arr)
        new_list = []

        # looping for each array element
        for i in range(arr_length):
            is_valid = False
            for j in range(arr_length):
                if(i == j):
                    # check the element not
                    # devide with itself
                    continue
                try:
                    print(self.devide_num(num1=arr[i],
                                          num2=arr[j]), num)
                    is_valid = True if self.devide_num(num1=arr[i],
                                                       num2=arr[j]) == num else is_valid

                except:
                    print("Cannot devide by zero")
            # check if array is valid or not
            if(is_valid):
                new_list.append(arr[i])

        return new_list
