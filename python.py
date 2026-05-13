from ev3dev2.motor import LargeMotor, OUTPUT_A , OUTPUT_C, SpeedPerce
from ev3dev2.sensor import INPUT_1 , INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound 
# TODO: add code here

sound = Sound()
sound.speak('welcome to the E V 3 dev project! ')

arquivo log_ = open ('/home/robot/ex' , 'a')

motor_esquerdo = LargeMotor(OUTPUT_B)
motor_direito = LargeMotor(OUTPUT_C)


sonar  = UltrasonicSensor(INPUT-4)
sonar.mode = 'US-DIST-CM'

#DISTANCIA QUE A EXECUÇAO OCORRE
distancia_alvo = 10.0

# MEDE A DISTANCIA DO OBSTACULO
while True:

distancia = sonar.distance_centimeters

if distancia > 40:
    motor_esquerdo.on(SpeedPercent(100))
    motor_direito.on(SpeedPercent(100))

    arquivo_log.write("100")
    arquivo_log.write("\n")
elif abs(distancia - distancia_alvo) <=40 and abs(distancia - distancia_alvo) >=0.1:
    maximo= 30
    erro =100*abs(distancia - distancia_alvo)/maximo
    if distancia - distancia_alvo >=0:
            sinal= -1
else:
            sinal= -1
        erro+ erro * sinal
motor_esquerdo.on(speedPercent(erro))
motor_direito.on(speedPercent(erro))
arquivo_log.write(str(erro))
arquivo_log.write("|n")
else:

motor_esquerdo.stop()
motor_direito.stop()
sound.beep()
arquivo_log.write("cheguei")
arquivo_log.write("\n")
break

