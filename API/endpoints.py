from flask import Flask, request, jsonify
from fincal import FinancialCalculator

class FinanceCallApi:
    def __init__(self):
        """
        Initialize the FinanceCallApi class.
        """
        self.app = Flask(__name__)
        self.set_routes()

    def set_routes(self):
        """
        Set the routes for the Flask application.
        """
        self.app.errorhandler(404)(self.errorpage)
        self.app.route("/", methods=['GET'])(self.index)
        self.app.route("/personalloan", methods=['POST'])(self.personalLoan)
        self.app.route("/mortgageloan", methods=['POST'])(self.mortgage)
        self.app.route("/carloan", methods=['POST'])(self.carloan)


    """
    Error handler for 404 Not Found.
    Need better error handling --need to be review
    """
    def errorpage(self, error):
        return "Endpoint doesn't exist", 404 




    def index(self):
        return "Welcome to Financial Calculator API"

    """Personal Loan return loanTermMonths, totalInterest, endDate"""
    def personalLoan(self):
      
        data = request.json
        if data:
            loanAmount = data.get('loanAmount')
            interestRate = data.get('interestRate')
            monthlyPayment = data.get('monthlyPayment')
            result = FinancialCalculator.personalloanCal(loanAmount, interestRate, monthlyPayment)
            return jsonify(result)
        else:
            return jsonify({"error": "No data provided"}), 400


    """Mortgage Calculators--- Return Monthly Payment, Total Cost"""
    def mortgage(self):
     
        data = request.json
        if data:
            mortgageRate = data.get('mortgageRate')
            mortgageLife = data.get('mortgageLife')
            mortgageAmount = data.get('mortgageAmount')
            result = FinancialCalculator.mortgageCalculator(mortgageRate, mortgageLife, mortgageAmount)
            return jsonify(result)
        else:
            return jsonify({"error": "No data provided"}), 400

    
    """Car Loan Calculators-- return Monthly Payment, totalCost, endDate"""
    def carloan(self):
       
        data = request.json
        if data:
            purchasePrice = data.get('purchasePrice')
            loanRate = data.get('loanRate')
            loanLife = data.get('loanLife')
            result = FinancialCalculator.carLoanCalculator(purchasePrice, loanRate, loanLife)
            return jsonify(result)
        else:
            return jsonify({"error": "No data provided"}), 400

if __name__ == '__main__':
    #Create an Instance for the class 
    finance_api = FinanceCallApi()
    #on deployment, want to specify the Port- 5000
    finance_api.app.run(debug=True)
