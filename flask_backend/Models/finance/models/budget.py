class BudgetCalculator:
    def __init__(self, industry, revenue):
        self.industry = industry
        self.revenue = revenue
        self.benchmarks = {}

    def set_benchmarks(self, marketing, research_and_development, operating_expenses, debt_repayment):
        self.benchmarks = {
            "marketing": marketing,
            "research_and_development": research_and_development,
            "operating_expenses": operating_expenses,
            "debt_repayment": debt_repayment
        }
    def calculate_budget(self):
        budget = {}
        for category, benchmark in self.benchmarks.items():
            budget[category] = self.revenue * benchmark            
        return budget
    
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or value > 1:
                print("Please enter a value between 0 and 1.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a decimal value.")
"""
function checks the input is a decimal between 0 and 1 and will prompt if invalid
"""

def get_industry_input():
    while True:
        industry = input("Enter industry: ")
        if industry.strip() == "":
            print("Please enter a valid industry.")
        else:
            return industry

"""
checks its not an empty string
"""

def get_revenue_input():
    while True:
        try:
            revenue = float(input("Enter revenue: "))
            if revenue < 0:
                print("Please enter a non-negative revenue value.")
            else:
                return revenue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
"""
checks its not negative
"""

def main():
    industry = get_industry_input()
    revenue = get_revenue_input()

    calculator = BudgetCalculator(industry, revenue)

    marketing = get_float_input("Enter marketing benchmark (as a decimal): ")
    research_and_development = get_float_input("Enter research and development benchmark (as a decimal): ")
    operating_expenses = get_float_input("Enter operating expenses benchmark (as a decimal): ")
    debt_repayment = get_float_input("Enter debt repayment benchmark (as a decimal): ")

    calculator.set_benchmarks(marketing, research_and_development, operating_expenses, debt_repayment)

    print(calculator.calculate_budget())

if __name__ == "__main__":
    main()


"""
#example usage
Enter industry: Technology
Enter revenue: 100000
Enter marketing benchmark (as a decimal): 0.15
Enter research and development benchmark (as a decimal): 0.10
Enter operating expenses benchmark (as a decimal): 0.20
Enter debt repayment benchmark (as a decimal): 0.05

"""