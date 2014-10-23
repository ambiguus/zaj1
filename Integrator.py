def function(x):
 return 3
class Integrator:
 integral = 0
 def __init__(self):
  print("tworze")
 def integrate(self, N, f, a, b):
  print(integral)

class RectangleIntegrator(Integrator):
 def integrate(self, N, f, a, b):
  l = ((b-a)/N)
  integral = 0
  for i in range(N):
   a1 = l*i;
   b1 = l*(i+1)
   integral += f(l*(2*i+1)/2)*l
  print(integral)

class TrapesoidIntegrator(Integrator):
 def integrate(self, N, f, a, b):
  l = ((b-a)/N)
  integral = 0
  for i in range(N):
   a1 = l*i;
   b1 = l*(i+1)
   integral += (f(a1)+f(b1))*l/2
  print(integral)

class SimpsonIntegrator(Integrator):
 def integrate(self, N, f, a, b):
  l = ((b-a)/N)
  integral = 0
  for i in range(N):
   a1 = l*i;
   b1 = l*(i+1)
   integral += (f(a1)+4*f((a1+b1)/2)+f(b1))*l/6
  print(integral)
