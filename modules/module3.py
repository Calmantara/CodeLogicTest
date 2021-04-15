# Module 3 Class
# __author__ = Calmantara
# created = 15th April 2021
# skill test purpose

class Module3:
    def __init__(self):
        '''
            Class represents third solution
        '''
        pass

    def parse_string(self, string: str) -> list:
        '''
            Function to parse string with space into list
        '''
        return string.split(" ")

    def get_length(self, string: str) -> int:
        '''
            Function to get string length
        '''
        return len(string)

    def is_word_valid(self, string: str) -> bool:
        '''
            Function to get whether string is valid or not
        '''
        return True if string != "" and string != " " else False

    def check_string(self, string: str, num: int) -> list:
        '''
            Function to return all words
            that the length matches with num 
        '''
        arr_string = self.parse_string(string=string)
        result = []

        for word in arr_string:
            if(self.get_length(string=word) == num and
               self.is_word_valid(string=word)):
                # append valid word to result
                result.append(word)

        return result
