import wiringpi as pi

OUTPUT_PIN=23

pi.wiringPiSetupGpio()
pi.pinMode(OUTPUT_PIN,pi.OUTPUT)




