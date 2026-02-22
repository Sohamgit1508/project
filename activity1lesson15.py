def total_calc(total_amount,tip): 
    total=total_amount*(1+0.1*tip)
    total=round(total,2)
    print(f"please pay ${total}")
total_calc(1000,20)