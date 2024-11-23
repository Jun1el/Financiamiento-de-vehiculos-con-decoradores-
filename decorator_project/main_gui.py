import tkinter as tk
from tkinter import ttk
from vehicles.base_vehicle import BaseVehicle
from vehicles.decorators import AirConditioning, LeatherSeats, SoundSystem
from finance.loan import LoanCalculator
from finance.decorators import log_user_interaction, log_execution, trace_execution

class LoanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Préstamos con Vehículo")
        self.root.geometry("500x400")

        # Variables de entrada
        self.principal_var = tk.StringVar()
        self.rate_var = tk.StringVar()
        self.months_var = tk.StringVar()
        self.vehicle_cost_var = tk.StringVar(value="0")  # Costo del vehículo base
        self.result_var = tk.StringVar()
        self.total_var = tk.StringVar()
        self.interest_var = tk.StringVar()

        # Variables para decoradores
        self.air_conditioning_var = tk.BooleanVar()
        self.leather_seats_var = tk.BooleanVar()
        self.sound_system_var = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        # Sección de préstamo
        ttk.Label(self.root, text="Monto del Préstamo:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.principal_var).grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Tasa de Interés (% anual):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.rate_var).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Plazo (meses):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.months_var).grid(row=2, column=1, padx=10, pady=5)

        # Sección del vehículo
        ttk.Label(self.root, text="Costo del Vehículo Base:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.vehicle_cost_var).grid(row=3, column=1, padx=10, pady=5)

        # Opciones de decoradores
        ttk.Label(self.root, text="Adiciones al Vehículo:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        ttk.Checkbutton(self.root, text="Aire Acondicionado (+2000)", variable=self.air_conditioning_var).grid(row=5, column=0, padx=20, pady=5, sticky="w")
        ttk.Checkbutton(self.root, text="Asientos de Cuero (+3000)", variable=self.leather_seats_var).grid(row=6, column=0, padx=20, pady=5, sticky="w")
        ttk.Checkbutton(self.root, text="Sistema de Sonido (+1200)", variable=self.sound_system_var).grid(row=7, column=0, padx=20, pady=5, sticky="w")

        # Botón para calcular
        ttk.Button(self.root, text="Calcular", command=self.calculate).grid(row=8, column=0, columnspan=2, pady=10)

        # Resultados
        ttk.Label(self.root, text="Cuota Mensual:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(self.root, textvariable=self.result_var).grid(row=9, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Total a Pagar:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(self.root, textvariable=self.total_var).grid(row=10, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Intereses Totales:").grid(row=11, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(self.root, textvariable=self.interest_var).grid(row=11, column=1, padx=10, pady=5)
    @log_execution
    @trace_execution
    @log_user_interaction
    def calculate(self):
        try:
            # Obtener valores de entrada
            principal = float(self.principal_var.get())
            rate = float(self.rate_var.get())
            months = int(self.months_var.get())
            vehicle_cost = float(self.vehicle_cost_var.get())

            # Crear el vehículo base
            vehicle = BaseVehicle(vehicle_cost)

            # Aplicar decoradores según las selecciones
            if self.air_conditioning_var.get():
                vehicle = AirConditioning(vehicle)
            if self.leather_seats_var.get():
                vehicle = LeatherSeats(vehicle)
            if self.sound_system_var.get():
                vehicle = SoundSystem(vehicle)

            # Actualizar el costo del préstamo con el costo total del vehículo
            principal += vehicle.get_cost()

            # Calcular cuota mensual
            calculator = LoanCalculator()
            monthly_payment = calculator.calculate_monthly_payment(principal, rate, months)

            # Calcular totales
            total_payment = monthly_payment * months
            interest = total_payment - principal

            # Mostrar resultados
            self.result_var.set(f"{monthly_payment:.2f}")
            self.total_var.set(f"{total_payment:.2f}")
            self.interest_var.set(f"{interest:.2f}")

            return monthly_payment
        
        except ValueError:
            self.result_var.set("Error")
            self.total_var.set("Revisar")
            self.interest_var.set("Entradas")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoanApp(root)
    root.mainloop()
