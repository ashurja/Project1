# Jamshed Ashurov
# 09/12/2017
# Chatbot.py
# This program creates a chatbot
print("Hello there! My name is CarBot.")
name = input("What is your name ?")
print("Hello", name, "it is great to meet you!")
place = input(name+", "+"where are you from?")
print(place, "sounds like a pleasant place to grow up. Hmmmm, what else can I ask you... oh!")
number = input("What is your favorite number?")
my_number = 7
the_difference = int(number) / my_number
print("Your favorite number", number, "is {0:.2f}".format(the_difference)+" times as big as my favorite number", my_number)
car = input("What is your favorite car?")
print("Wow, I have always wanted a", car, "as well.")
cost = float(input("How much does "+car+" cost?"))
interest_rate = input("What is a reasonable yearly interest rate on a beautiful car like that?")
years_loan = int(input("And if you had to take out a loan to buy the "+car+","  
                                                                           " how many years would you take the "
                                                                           "loan out for?"))
# The following lines calculate the monthly and the total payment.
rate = float(interest_rate) / 1200
number_monpay = float(years_loan * -12)
month_payment = float(rate * cost) / float(1-(1+rate)**number_monpay)
totalyear_cost = month_payment * float(-1 * number_monpay)
print("If you bought the "+car+", " 
                               "you would have a monthly payment of $ {0:.2f}".format(month_payment)+", " 
                               "hopefully that is reasonable for your budget. "
                               "That's a total of $ {0:.2f}".format(totalyear_cost)+"! "
                               "I hope you can make the purchase! "
                               "Anyways, I gotta go. It's been nice chattin' with ya " + name+" :)")
