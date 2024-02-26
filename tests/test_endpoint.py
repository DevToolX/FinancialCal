import os
import sys
import json
import pytest
from unittest.mock import patch

# Append API directory to sys path
current_dir = os.path.dirname(__file__)
api_dir = os.path.abspath(os.path.join(current_dir, '..', 'API'))
sys.path.append(api_dir)

# Import the FinanceCallApi class from endpoints module
from endpoints import FinanceCallApi

class TestFinanceAPI:
    
    """
    Fixture to create a test client for the Flask application.
    """
    @pytest.fixture
    def client(self):

        app = FinanceCallApi().app.test_client()
        return app

    
    """
    Test function to check the /personalloan endpoint.

    It mocks the personal loan calculation function and tests
    if the endpoint returns the expected data.
    """
    
    @patch('endpoints.FinancialCalculator.personalloanCal')
    def test_personal_loan(self, mock_personal_loan_cal, client):
    
        mock_personal_loan_cal.return_value = {
            'monthlyPayment': 200,
            'totalInterest': 1526.57
        }
        data = {
            "loanAmount": 10000,
            "interestRate": 5,
            "monthlyPayment": 200
        }
        response = client.post('/personalloan', json=data)
        assert response.status_code == 200
        result = json.loads(response.data.decode())
        assert result['monthlyPayment'] == 200
        assert result['totalInterest'] == 1526.57

        
    """
    Test function to check the /mortgageloan endpoint.

    It mocks the mortgage calculation function and 
    tests if the endpoint returns the expected data.
    """

    @patch('endpoints.FinancialCalculator.mortgageCalculator')
    def test_mortgage(self, mock_mortgage_calculator, client):
      
        mock_mortgage_calculator.return_value = {
            'monthlyPayment': 1013.37,
            'totalInterest': 164813.42
        }
        data = {
            "mortgageRate": 4.5,
            "mortgageLife": 30,
            "mortgageAmount": 200000
        }
        response = client.post('/mortgageloan', json=data)
        assert response.status_code == 200
        result = json.loads(response.data.decode())
        assert result['monthlyPayment'] == 1013.37
        assert result['totalInterest'] == 164813.42

    """
    Test function to check the /carloan endpoint.

    It mocks the car loan calculation function 
    and tests if the endpoint returns the expected data.
    """

    @patch('endpoints.FinancialCalculator.carLoanCalculator')
    def test_car_loan(self, mock_car_loan_calculator, client):
  
        mock_car_loan_calculator.return_value = {
            'monthlyPayment': 454.23,
            'totalInterest': 2525.79
        }
        data = {
            "purchasePrice": 25000,
            "loanRate": 3.5,
            "loanLife": 5
        }
        response = client.post('/carloan', json=data)
        assert response.status_code == 200
        result = json.loads(response.data.decode())
        assert result['monthlyPayment'] == 454.23
        assert result['totalInterest'] == 2525.79
