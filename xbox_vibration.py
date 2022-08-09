import inputs

gamepd = inputs.devices.gamepads[0]

gamepd.set_vibration(0.6,0.8,100) #(vibration sensitivity 0-1) (0-1 left, 0-1 right, time_duration in ms)
