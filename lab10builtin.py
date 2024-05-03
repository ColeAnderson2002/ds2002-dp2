#!/usr/bin/env python3

# def throw_me_an_error():
#   val1 = 14
#   val2 = 0
#   return val1 / val2

# throw_me_an_error()

def throw_me_another_error():
    val1 = 20
    val2 = 0
    try:
        result = val1 / val2
        print(result)
        return result
    except Exception as e:
        print('Type of Error: ' + str(e))

throw_me_another_error()



    
        
