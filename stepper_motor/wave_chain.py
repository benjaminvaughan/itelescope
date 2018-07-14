import pigpio
pi = pigpio.pi()

DIR = 20
STEP = 21

pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

def generate_ramp(ramp):
    pi.wave_clear()
    length = len(ramp)
    wid = [-1]*length

    for i in range(length):
        frequency = ramp[i][0]
        micros = int(500000/frequency)
        wf = []
        wf.append(pigpio.pulse(1 << STEP, 0 ,micros))
        wf.append(pigpio.pulse(0,1<<STEP, micros))
        pi.wave_add_generic(wf)
        wid[i] = pi.wave_create()

        chain = []
        for i in range(length):
            steps = ramp[i][1]
            x = steps & 255
            y = steps >> 8
            chain += [255,0,wid[i],255,1,x,y]

        pi.wave_chain(chain)

generate_ramp([[320,200]])

