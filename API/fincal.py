"""
Finanaical Calculators
Users can find the Missng information
Things such as Inrest Rate, Monthly payment and Total with Intrest

"""


from datetime import datetime, timedelta

class FinancialCalculator:


    """Personal Loan return loanTermMonths, totalInterest, endDate"""
    @staticmethod
    def personalloanCal(loanAmount,interestRate, monthlyPayment)-> int:
        try:
            totalInterest = 0
            loanTermMonths = 0
            

            while loanAmount > 0:
                loanTermMonths += 1
                monthlyInterest = loanAmount * interestRate / 12 / 100
                totalInterest += monthlyInterest
                loanAmount -= (monthlyPayment - monthlyInterest)

                endDate = datetime.now() + timedelta(days=loanTermMonths * 30)

            return loanTermMonths, totalInterest, endDate

        except Exception as e:
           return "Error", e

  
    """Car Loan Calculators-- return Monthly Payment, totalCost, endDate"""
    @staticmethod
    def carLoanCalculator(purchasePrice, loanRate, loanLife)->int:
        try:
            monthlyInterestRate = loanRate / 12 / 100
            totalPayments = loanLife * 12
            monthlyPayment = (purchasePrice * monthlyInterestRate) / (1 - (1 + monthlyInterestRate) ** -totalPayments)
            totalCost = monthlyPayment * totalPayments
            endDate = datetime.now() + timedelta(days=loanLife * 30)

            return monthlyPayment, totalCost, endDate

        except Exception as e:
            return "Error", e

    

    """Mortgage Calculators--- Return Monthly Payment, Total Cost"""
    @staticmethod
    def mortgageCalculator(mortgageRate,mortgageLife,mortgageAmount)-> int:
        try:
            monthlyInterestRate = mortgageRate / 12 / 100
            totalPayments = mortgageLife * 12
            monthlyPayment = (mortgageAmount * monthlyInterestRate) / (1 - (1 + monthlyInterestRate) ** -totalPayments)
            totalCost = monthlyPayment * totalPayments

            return monthlyPayment, totalCost

        except Exception as e:
            return "Error", e


    




if __name__ == "__main__":
    calculator = FinancialCalculator()

    