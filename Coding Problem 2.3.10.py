can_afford = True
destination_is_safe = True
educational_value = True
relatives_nearby = True
is_international = True
have_passport = True
afraid_to_fly = True
have_a_car = False
is_a_beach = False
is_warm = False
has_skiing = False
is_a_city = False
is_off_peak = False
has_attraction = True

#With long, long problems like this, your best bet is to break it down into smaller,
#more easily resolvable decisions. For example, in my approach, we first examine
#whether we have the means to pay for the trip:
can_pay_myself = can_afford and destination_is_safe
parents_will_pay = destination_is_safe and (educational_value or relatives_nearby)
can_pay = can_pay_myself or parents_will_pay

#Then, we examine whether we're permitted to go on the trip:
can_go_international = is_international and have_passport and not afraid_to_fly
can_go_domestic = not is_international and (have_a_car or not afraid_to_fly)
can_go = can_go_international or can_go_domestic

#Then, we examine whether we WANT to go on the trip:
want_to_go_beach = is_a_beach and is_warm
want_to_go_skiing = has_skiing and not is_warm
want_to_go_city = is_a_city and (is_off_peak or has_attraction)
want_to_go = want_to_go_beach or want_to_go_skiing or want_to_go_city

#We only go on the trip if we can pay, if we can go, and if we want to go,
#so at the end we just make sure those three things are true:
result = can_pay and can_go and want_to_go
print(result)
