def Fun1():
    tea_order = "green tea"
    def Fun2():
        nonlocal tea_order
        tea_order = "black tea"
        print(tea_order)
    Fun2()
    print(f"After calling Fun2: {tea_order}")


Fun1()