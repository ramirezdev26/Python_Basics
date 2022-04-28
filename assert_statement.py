def divisors(num):
   divisors = [i for i in range(1, num +1) if num % i == 0]
   return divisors

def run():
      num = input("Ingresa un numero: ")
      assert num.isnumeric(), "Debes ingresar un numero"
      assert int(num) > 0, "Debes ingresar un numero positivo"
      print(divisors(int(num)))
      print("Termino mi programa")

if __name__ == '__main__':
    run()