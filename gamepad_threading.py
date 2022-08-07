import inputs
import time
import threading
#set vibration for error/ state/ stop
print("GamePad Control Started..")

pad = inputs.devices.gamepads
try:
    print('CONTROLLER : ' + str(pad[0]))
except:
    IndexError

try:
    print('CONTROLLER : ' + str(pad[1]))
except:
    pass

def con1():
    if len(pad):
        while True:
            events = inputs.get_gamepad()
            for event in events:
                # print(event.ev_type,event.state,event.code)
                if event.ev_type == 'Key' and event.code == 'BTN_START':
                    print("START",event.state)#back
                if event.ev_type == 'Key' and event.code == 'BTN_SELECT':
                    print("SELECT",event.state)#start
                if event.ev_type == 'Key' and event.code == 'BTN_THUMBL':
                    print("THUMBL",event.state)#left joystick btn
                if event.ev_type == 'Key' and event.code == 'BTN_THUMBR':
                    print("THUMBR",event.state)#right joystick btn
                if event.ev_type == 'Key' and event.code == 'BTN_EAST':
                    print("B",event.state)#B
                if event.ev_type == 'Key' and event.code == 'BTN_NORTH':
                    print("Y",event.state)#Y
                if event.ev_type == 'Key' and event.code == 'BTN_WEST':
                    print("X",event.state)#X
                if event.ev_type == 'Key' and event.code == 'BTN_SOUTH':
                    print("A",event.state)#A

    else:
        print("NO gamepad or Controller found")

def con2():
    if len(pad):
        while 1:
                events = inputs.get_gamepad()
                for event in events:
                    if event.ev_type == 'Key' and event.code == 'BTN_TL':
                        print("LB",event.state)#LB
                    if event.ev_type == 'Key' and event.code == 'BTN_TR':
                        print("RB",event.state)#RB
                    if event.ev_type == 'Absolute' and event.code == 'ABS_Z':
                        print("LT",event.state)#LT
                    if event.ev_type == 'Absolute' and event.code == 'ABS_RZ':
                        print("RT",event.state)#RT
                    if event.ev_type == 'Absolute' and event.code == 'ABS_Y':
                        print("L_JOY_Y",event.state)#left joystick y
                    if event.ev_type == 'Absolute' and event.code == 'ABS_X':
                        print("L_JOY_X",event.state)#left joystick x
                    if event.ev_type == 'Absolute' and event.code == 'ABS_RX':
                        print("R_JOY_X",event.state)#right joystick x
                    if event.ev_type == 'Absolute' and event.code == 'ABS_RY':
                        print("R_JOY_Y",event.state)#right joystick y
                    if event.ev_type == 'Absolute' and event.code == 'ABS_HAT0X':
                        print("X_1",event.state)#Dpad X
                    if event.ev_type == 'Absolute' and event.code == 'ABS_HAT0Y':
                        print("Y_1",event.state)#Dpad Y

    else:
        print("NO gamepad or Controller found")

if __name__ == "__main__":
    x = threading.Thread(target=con1)
    y = threading.Thread(target=con2)

    x.start()
    time.sleep(0.1)
    y.start()
