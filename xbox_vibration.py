import inputs

def main():
    gamepd = inputs.devices.gamepads[0]

    gamepd.set_vibration(1,0,10000)

if __name__ == "__main__":
    main()
