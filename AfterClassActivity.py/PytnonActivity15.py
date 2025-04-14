def bill(waiter_tip,total_bill):
    food=total_bill*(1+0.01*waiter_tip)
    food=round(food,2)
    print(food)
bill(20, 290)

    
    
