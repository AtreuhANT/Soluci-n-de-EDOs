# Solucion-de-EDOs

La ecuación original es:

$$\frac{d^2x}{dt^2} - \mu(1 - x^2)\frac{dx}{dt} + x = 0$$

Definiendo la velocidad como 
$v = \frac{dx}{dt}$ , obtenemos el siguiente sistema de ecuaciones diferenciales de primer orden:

$$\frac{dx}{dt} = v$$

$$\frac{dv}{dt} = \mu(1 - x^2)v - x$$

Q1: Intervalo de mayores aceleraciones y reflejo en pendientesAl analizar los resultados de la Gráfica 1, la estructura experimenta las mayores aceleraciones en los tramos donde la curva de velocidad 
$v(t)$
presenta sus pendientes más pronunciadas, dado que por definición 
$a(t) = \frac{dv}{dt}$
.

Intervalo Crítico: Esto ocurre periódicamente cuando el desplazamiento 
$x(t)$ 
cruza por cero (
$x \approx 0$
). En este punto, el amortiguamiento no lineal se vuelve fuertemente negativo, inyectando energía momentánea al sistema. En la gráfica temporal, se refleja en una caída o subida casi vertical y abrupta de la curva de velocidad, mientras que la curva de desplazamiento 
$x(t)$ 
cambia radicalmente de concavidad (punto de inflexión con pendiente máxima).

Q2: Significado físico de la convergencia al Ciclo LímiteEn un oscilador clásico con amortiguamiento lineal positivo, la energía se disipa continuamente y la trayectoria en el espacio de fases "muere" en el origen 
$(0,0)$ 
(reposo absoluto).

Significado Físico: Que converja hacia un Ciclo Límite significa que el amortiguamiento es no lineal y auto-regulado. Cuando las oscilaciones son muy grandes (
$|x| > 1$
), el término 
$\mu(1-x^2)$ 
se vuelve negativo, actuando como un amortiguador convencional que disipa energía. Cuando las oscilaciones son pequeñas (
$|x| < 1$
), el término se vuelve positivo, actuando como una fuente que inyecta energía al sistema. El ciclo límite representa el balance termodinámico exacto donde la energía disipada en una parte del ciclo es igual a la energía absorbida en la otra, garantizando un estado de vibración constante y autosostenido frente al sismo.

Q3: Prueba de Estabilidad Numérica (
$h = 0.5\,\text{s}$ y $h = 1.0\,\text{s}$
)

Al incrementar el paso de integración a 
$h = 0.5\,\text{s}$ y $h = 1.0\,\text{s}$
, se observa en la consola un fenómeno de divergencia numérica catastrófica (los valores de 
$x$
y 
$v$ 
escalan exponencialmente hacia el infinito NaN o inf en pocas iteraciones).

Justificación de la falla de RK4: El método RK4 es un método explícito que posee una región de estabilidad absoluta limitada en el plano complejo. La ecuación de van der Pol es un sistema stiff (rígido) debido a los cambios abruptos de velocidad que introduce el término no lineal 
$\mu(1-x^2)v$
. Al utilizar un paso 
$h$ 
demasiado grande (muestreo temporal sub-dimensionado), el algoritmo es incapaz de capturar las rápidas variaciones de la derivada en las zonas de alta pendiente. Matemáticamente, el error local de truncamiento (
$O(h^5)$
) se propaga y magnifica en lugar de atenuarse, sacando al vector de estado fuera de la región estable del método y destruyendo la convergencia de la aproximación numérica.
