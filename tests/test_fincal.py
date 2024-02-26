"""
Implement UnitTesting using Pytest 

"""

import pytest
from datetime import datetime, timedelta
import os
import sys
import random

"""LinuX Sytem having problems with Imports for other dir"""

current_dir = os.path.dirname(__file__)
api_dir = os.path.abspath(os.path.join(current_dir, '..', 'API'))
sys.path.append(api_dir)

#Import the file for testing
from fincal import FinancialCalculator


class TestFinancialCalculator:

    @pytest.fixture
    def calculator(self):
        return FinancialCalculator()


    def testPersonalLoanCal(self, calculator):
        loanAmount = random.randint(1,10000)
        interestRate = random.randint(1,10)
        monthlyPayment =random.randint(1,10000)
        result = calculator.personalloanCal(loanAmount, interestRate, monthlyPayment)
        assert isinstance(result, tuple)
        assert len(result) == 3
        loanTermMonths, totalInterest, endDate = result
        assert loanTermMonths > 0
        assert totalInterest > 0
        assert isinstance(endDate, datetime)

    def test_car_loan_calculator(self, calculator):
        purchasePrice = random.randint(100,10000)
        loanRate = random.randint(1,10)
        loanLife = random.randint(1,20) 
        result = calculator.carLoanCalculator(purchasePrice, loanRate, loanLife)
        assert isinstance(result, tuple)
        assert len(result) == 3
        monthlyPayment, totalCost, endDate = result
        assert monthlyPayment > 0
        assert totalCost > 0
        assert isinstance(endDate, datetime)

    def test_mortgage_calculator(self, calculator):
        mortgageRate = random.randint(1,10000)
        mortgageLife =random.randint(1,10)
        mortgageAmount =random.randint(1,10000)
        result = calculator.mortgageCalculator(mortgageRate, mortgageLife, mortgageAmount)
        assert isinstance(result, tuple)
        assert len(result) == 2
        monthlyPayment, totalCost = result
        assert monthlyPayment > 0
        assert totalCost > 0




