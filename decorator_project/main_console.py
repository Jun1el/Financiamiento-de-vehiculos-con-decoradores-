from vehicles.base_vehicle import BaseVehicle
from vehicles.decorators import AirConditioning, LeatherSeats, SoundSystem
from finance.loan import LoanCalculator
from finance.decorators import log_execution, trace_execution , log_user_interaction

# Parte 1: Vehículo con Accesorios
print("=== Personalización del Vehículo ===")
base_vehicle_cost = 20000
vehicle = BaseVehicle(base_vehicle_cost)
vehicle = AirConditioning(vehicle)
vehicle = LeatherSeats(vehicle)
vehicle = SoundSystem(vehicle)

print("Descripción:", vehicle.get_description())
print("Costo total:", vehicle.get_cost())

# Parte 2: Calculadora de Préstamos con Logs y Trace
@log_execution
@trace_execution
@log_user_interaction
def calculate_loan():
    calculator = LoanCalculator()
    return calculator.calculate_monthly_payment(20000, 5, 60)

print("\n=== Cálculo de Préstamo ===")
payment = calculate_loan()
print(f"Cuota mensual: {payment:.2f}")
