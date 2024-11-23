class LoanCalculator:
    """Clase para calcular cuotas de préstamos."""
    def calculate_monthly_payment(self, principal, interest_rate, months):
        """Calcula la cuota mensual usando fórmula de amortización."""
        monthly_rate = interest_rate / 12 / 100
        payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
        return payment
