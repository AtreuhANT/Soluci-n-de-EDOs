import numpy as np
import matplotlib.pyplot as plt

def vander_pol_system(t: float, state: np.ndarray, mu: float) -> np.ndarray:
    try:
        x = state[0]
        v = state[1]
        dxdt = v
        dvdt = mu * (1.0 - x**2) * v - x
        return np.array([dxdt, dvdt], dtype=float)
    except Exception as e:
        raise ValueError(f"Error al evaluar el sistema diferencial: {e}")
def rk4_step(f, t: float, state: np.ndarray, h: float, mu: float) -> np.ndarray:
    k1 = f(t, state, mu)
    k2 = f(t + h/2.0, state + (h/2.0) * k1, mu)
    k3 = f(t + h/2.0, state + (h/2.0) * k2, mu)
    k4 = f(t + h, state + h * k3, mu)
    return state + (h / 6.0) * (k1 + 2.0*k2 + 2.0*k3 + k4)
def run_simulation(t0: float, tf: float, h: float, init_state: list, mu: float):
    steps = int(np.round((tf - t0) / h))
    t_array = np.linspace(t0, tf, steps + 1)
    state_matrix = np.zeros((steps + 1, 2), dtype=float)
    state_matrix[0] = np.array(init_state, dtype=float)
    current_state = state_matrix[0].copy()
    for i in range(steps):
        current_state = rk4_step(vander_pol_system, t_array[i], current_state, h, mu)
        state_matrix[i + 1] = current_state
    return t_array, state_matrix[:, 0], state_matrix[:, 1]
def print_data_table(t: np.ndarray, x: np.ndarray, v: np.ndarray, num_iterations: int = 10):
    print("=" * 65)
    print(f"      TABLA DE DATOS DE SIMULACIÓN (Primeras {num_iterations} iteraciones)")
    print("=" * 65)
    print(f"{'Iteración':<10}{'Tiempo (s)':<15}{'Desplazamiento x(t)':<22}{'Velocidad v(t)':<18}")
    print("-" * 65)
    for i in range(num_iterations):
        print(f"{i:<10}{t[i]:<15.3f}{x[i]:<22.6f}{v[i]:<18.6f}")
    print("-" * 65)
    print(f"      ESTADOS FINALES (Últimas 2 iteraciones)")
    print("-" * 65)
    for i in range(len(t) - 2, len(t)):
        print(f"{i:<10}{t[i]:<15.3f}{x[i]:<22.6f}{v[i]:<18.6f}")
    print("=" * 65 + "\n")

def plot_results(t: np.ndarray, x: np.ndarray, v: np.ndarray, title_suffix: str = ""):
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t, x, 'b-', label='Desplazamiento x(t)', linewidth=2)
    plt.plot(t, v, 'r--', label='Velocidad v(t)', linewidth=1.5)
    plt.title(f'Gráfica 1: Evolución Temporal {title_suffix}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud Estado')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, v, 'g-', label='Trayectoria de fase', linewidth=1.5)
    plt.scatter(x[0], v[0], color='blue', zorder=5, label=f'Inicio ({x[0]}, {v[0]})')
    plt.title(f'Gráfica 2: Espacio de Fases {title_suffix}')
    plt.xlabel('Desplazamiento x')
    plt.ylabel('Velocidad v')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    MU = 1.5
    T0 = 0.0
    TF = 20.0
    H_BASE = 0.05
    INITIAL_STATE = [2.0, 0.0]
    print("Iniciando simulación numérica principal con h = 0.05 s...")
    t, x, v = run_simulation(T0, TF, H_BASE, INITIAL_STATE, MU)
    print_data_table(t, x, v, num_iterations=10)
    plot_results(t, x, v, title_suffix="(h = 0.05 s)")
    for h_test in [0.5, 1.0]:
        print(f"Ejecutando prueba de estabilidad con h = {h_test} s...")
        try:
            t_test, x_test, v_test = run_simulation(T0, TF, h_test, INITIAL_STATE, MU)
            print_data_table(t_test, x_test, v_test, num_iterations=5)
            if np.all(np.isfinite(x_test)) and np.max(np.abs(x_test)) < 1e5:
                plot_results(t_test, x_test, v_test, title_suffix=f"(h = {h_test} s)")
            else:
                print(f"--> [ALERTA] Divergencia numérica extrema detectada con h = {h_test} s (Valores tienden a Infinito).\n")
        except Exception as e:
            print(f"Error durante la ejecución con h = {h_test}: {e}\n")
