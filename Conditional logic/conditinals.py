is_true = True
is_false = False

if is_true:
    print("Yup! It's true")
elif is_false:
    print("No! It's false")
else:
    print("IDK")
    
if is_true and is_true:
    print("Yup! It's true");
elif is_false and is_false:
    print("No! It's false");
elif is_true and is_false:
    print("Combination of true and false")
elif is_true or is_false:
    print("Combination of true or false")
elif is_true and not is_false:
    print("Truee!!")