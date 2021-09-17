"""
Tecnológico de Monterrey
Semana Tec 2021
Herramientas Computacionales: El Arte de la Programación

Equipo:
Ricardo Núñez Alanis
Cristian Leilael Rico Espinosa
"""

import subprocess

def menu():
    print("*****************************************************************")
    print("1. Snake.")
    print("2. Simon Says.")
    print("3. Memory Game.")
    print("4. Pong.")
    print("5. Exit.")
    print("*****************************************************************")
    
    
def main():      
    continua=True
    while continua:
        menu()
        opcion=int(input("Choose a game: "))

        if opcion == 1:
            subprocess.run(['python', 'snake.py'])


        elif opcion == 2:
            subprocess.run(['py', 'simonsays.py'])

 
        elif opcion == 3:
            print("Thank you for playing")


        elif opcion == 4:
            print("Thank you for playing")
 

        elif opcion == 5:
            
            print("Thank you for playing")
            continua = False
        

        else:
            print("Invalid Option")

            
main()
