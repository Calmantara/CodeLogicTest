# Module 1 Class
# __author__ = Calmantara
# created = 15th April 2021
# skill test purpose

class Module1:
    def __init__(self):
        '''
            Class represents first solution
        '''
        pass

    def substract_num(self,
                      num1: int,
                      num2: int) -> int:
        '''
            Function to substract two integer
        '''
        return num1 - num2

    def get_length(self,
                   arr: list) -> int:
        '''
            Funtion to get length of array
        '''
        return len(arr)

    def check_array(self,
                    arr: list) -> list:
        '''
            Function to return all numbers in list
            that does not return <0
        '''

        arr_length = self.get_length(arr=arr)
        new_list = []

        # looping for each array element
        for i in range(arr_length):
            is_valid = True
            for j in range(arr_length):
                if(i == j):
                    # check the element not
                    # substract with itself
                    continue
                is_valid = False if self.substract_num(num1=arr[i],
                                                       num2=arr[j]) < 0 else is_valid
            # check if array is valid or not
            if(is_valid):
                new_list.append(arr[i])

        return new_list
