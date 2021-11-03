# Functions Challenge 35: Loan Calculator App
from matplotlib import pyplot


def get_loan_info():
    loan = {}
    loan['principal'] = float(input("\nEnter the loan amount: "))
    loan['rate'] = float(input("Enter the interest rate: ")) / 100
    loan['monthly payment'] = float(input("Enter the desired monthly payment amount: "))
    loan['money paid'] = 0
    return loan


def show_loan_info(loan, number):
    print("\n----Loan information after" + str(number) + "months----")
    for key, value in loan.items():
        print(key.title() + ":" + str(value))


def collect_interest(loan):
    loan["principal"] = loan["principal"] + loan["principal"]*loan["rate"]/12


def make_monthly_payment(loan):
    loan["principal"] = loan["principal"] - loan["monthly payment"]
    if loan["principal"] > 0:
        loan["money paid"] += loan["monthly payment"]
    else:
        loan["money paid"] += loan["monthly payment"] + loan["principal"]
        loan["principal"] = 0


def summarize_loan(loan, number, initial_principal):
    print("\nCongratulations! You paid off your loan in " + str(number) + " months!")
    print("Your initial loan was " + str(initial_principal) + " at a rate of " + str(100*loan["rate"]) + "$.")
    print("Your monthly payment was $" + str(loan["monthly payment"]))
    print("You spent " + str(round(loan['money paid'], 2)) + " total.")
    print("You spent " + str(round(loan['money paid'] - initial_principal, 2)) + " on interest!")


def create_graph(data, loan):
    x_values = []
    y_values = []
    for x in data:
        x_values.append(x[0])
        y_values.append(x[1])
    pyplot.plot(x_values, y_values)
    pyplot.title(str(100 * loan['rate']) + "% Interest" + " With $" + str(loan['monthly payment']) + " Monthly Payment")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")
    pyplot.show()


print("Welcome to the Loan Calculator App")

month_number = 0
loan_ = get_loan_info()
starting_principal = loan_['principal']
data_to_plot = []
show_loan_info(loan_, month_number)

input("Press 'Enter' to begin paying off your loan.")

while loan_['principal'] > 0:
    if loan_['principal'] > starting_principal:
        break

    month_number += 1
    collect_interest(loan_)
    make_monthly_payment(loan_)
    data_to_plot.append((month_number, loan_['principal']))
    show_loan_info(loan_, month_number)


if loan_["principal"] <= 0:
    summarize_loan(loan_, month_number, starting_principal)
    create_graph(data_to_plot, loan_)
else:
    print("\nYou will NEVER pay off your loan!!!")
    print("You cannot get ahead of the interest! :-(")
