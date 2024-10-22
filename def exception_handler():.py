def exception_handler():
    try:
        print("Hello"+ name)
    except TypeError as e:
        print("TypeError occured! You can't add an integer and a string.")
    except NameError as e:
        print("NameError occured! The variable 'name' is not defined.")
    
    try:
        sample_list = [1, 2, 3, 4, 5]
        print(sample_list[5])
        sample_list.append(4)
        sample_list.not_a_method()
    
    except IndexError as e:
        print("IndexError! The index '5' is out of range.")
    except AttributeError as e:
        print("AttributeError occured! 'sample_list' has not such method or attribute.")
    
    try:
        my_dict = {'Car': 'Porsche', 'Horse Power':700}
        print(my_dict['car'])
    except KeyError as e:
        print("Key Occured! The key 'car' is not in the dictionary.")