def eval_loop():
    while True:
        prompt = input("What would you like to evaluate?: ")
        if prompt == 'done':
            print(f"The last evaulation gave us {evaluated}")
            break
        evaluated = (eval(prompt))
        print(eval(prompt))
        

eval_loop()