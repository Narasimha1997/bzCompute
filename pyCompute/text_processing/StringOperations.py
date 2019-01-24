from pyCompute.text_processing.graph import *
import numpy
import re


class split(Operation):

    def __init__(self, input_x, delimiter, name) :

        super().__init__(inputs = [input_x, delimiter], name = name)
    
    def compute(self, input_x, delimiter):

        self.values = [input_x, delimiter]

        return input_x.split(delimiter)
    
class re_match(Operation):

    def __init__(self, input_x, re, name) :

        super().__init__(inputs = [input_x, re], name = name)

    def compute(self, input_x, re_) :

        self.values = [input_x, re_]

        return re.findall(re_, input_x)

class histogram(Operation):

    def __init__(self, input_x, name):

        super().__init__(inputs = [input_x], name = name)
    
    def compute(self, input_x):

        self.values = [input_x]

        #compute histogram :
        words  = set(input_x.split(" "))

        hist_ = {}

        tokens = input_x.split(" ")

        for word in words : 

            hist_[word] = tokens.count(word)
        
        return hist_

class histogram_ignore_case(Operation):

    def __init__(self, input_x, name):

        super().__init__(inputs = [input_x], name = name)
    
    def compute(self, input_x):

        self.values = [input_x]

        #print(input_x)

        input_x = input_x.lower()

        #compute histogram :
        words  = set(input_x.split(" "))

        hist_ = {}

        tokens = input_x.split(" ")

        for word in words : 

            hist_[word] = tokens.count(word)
        
        return hist_


class concatenate(Operation):

    def __init__(self, input_x, input_y, name):

        super().__init__(inputs = [input_x, input_y], name = name)
    
    def compute(self, input_x, input_y):

        self.values = [input_x, input_y]

        return input_x + input_y


class substrings(Operation) :

    def __init__(self, input_x, name) :

        super().__init__(inputs = [input_x], name = name)

    def compute(self, input_x):

        self.values = [input_x]

        length = len(input_x)
        return [input_x[i:j+1] for i in range(length) for j in range(i,length)]

class array_histogram(Operation):

    def __init__(self, input_x, name):

        super().__init__(inputs = [input_x], name = name)
    

    def compute(self, input_x):

        self.values = [input_x]

        hist_ = {}

        words = set(input_x)


        for word in words :

            hist_[word] = input_x.count(word)
        
        return hist_

class array_split(Operation) :

    def __init__(self, input_x, delimiter, name) :

        super().__init__(inputs = [input_x, delimiter], name = name)

    def compute(self, input_x, delimiter) :

        self.values = [input_x, delimiter]
        split_tokens = []
        for token in input_x  :
            words = token.split(delimiter)
            split_tokens += words
        return split_tokens



class custom_op(Operation):

    def __init__(self, op_func, name,  *args, **kwargs):

        super().__init__(inputs = [*args], name = name)
        self.op_func = op_func
        self.kwargs = kwargs
    
    def compute(self, *args) :

        self.values = [*args]

        return self.op_func(*args, **self.kwargs)



class read_csv(Operation):

    def __init__(self, filename,convert_to_float = True, first_row_header = False, as_x_y = False) :

        super().__init__(inputs = [filename], name = name)

        self.as_np_array = as_np_array
        self.convert_to_float = convert_to_float
        self.first_row_header = False
        self.as_x_y = as_x_y
    
    def as_array(self, data) :
        if not self.first_row_header and not self.as_x_y : 

            return numpy.array(data) if self.convert_to_float else numpy.array(data, dtyle = 'float32')
        
        elif self.first_row_header and not self.as_x_y :
            data = numpy.array(data)
            return {"header" : data[0], "data" : data[1 : ]}
        
        elif not self.first_row_header and self.as_x_y : 
            data = numpy.array(data)
            return (data[:,0:-1], data[:, -1])
        
        elif self.first_row_header and self.as_x_y:
            data = numpy.array(data)
            return {
                "header" : data[0],
                "data" : (data[1 : , 0:-1], data[1 : , -1])
            }

    def compute(self, filename) :

        data = open(filename, 'r').readlines()

        if self.as_np_array : 
            return self.as_array(data)

        else: return  self.as_normal_array(data)
