#Bulls & Cows Game 
def generator():
    a= str(random.randint(0,9))
    b= str(random.randint(0,9))
    c= str(random.randint(0,9))
    d= str(random.randint(0,9))
    rand_numb= a+ b + c + d 
    return(rand_numb)


def game():
    random_number= generator()
    attemps = 0 
    boolean = True 
    print(random_number)
    while boolean:
        A= 0 
        B= 0
        my_input= input("Please input 4 digits: ")

        for i in range(0,4):
            if my_input[i]== random_number[i]:
                A +=1

            elif my_input[i] in random_number:
                B +=1
            else: 
                pass

        print(f"{A} A (Bulls) {B} B (Cows)")

        if A== 4:
            print("You Win!!!")
            break
        else: 
            pass
game()
            
