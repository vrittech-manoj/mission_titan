
import time #Import time

class Earth:
    def Device_Check(self):
        print("Welcome to the Vehicle Condition Check!\n")

        # Check fuel
        fuel = input("Is the engine oil level adequate? (yes/no): ").lower()
        if fuel != 'yes':
            print("Warning: Low engine oil. Check or replace the oil !!!")
    
        # Check battery condition
        battery = input("Is the battery have full Charge? (yes/no): ").lower()
        if battery != 'yes':
            print("Warning: Battery may need to be Charge !!!")
        # Check power system
        PowerSystem=input("Is the Power System Working Automatically? (yes/no): ").lower()
        if PowerSystem!='yes':
            print("Power System Failure !!!")
        #check communication system
        Communication=input("Is the Communication System Working Properly? (yes/no): ").lower()
        if Communication!='yes':
            print("Check Communication System...")
        #check life support system
        LifeSupportSystem=input("Check Life Support System? (yes/no): ").lower()
        if LifeSupportSystem!='yes':
            print("Check Life Support System:..")
        #check scientific instruments
        ScientificInstruments=input("Is Scientific Instruments Working Properly? (yes/no): ").lower()
        if ScientificInstruments!='yes':
            print("Scientific System Not Working properly....")
        #check backup systems
        BackupSystems=input("Does your Backup System Working Properly? (yes/no): ").lower()
        if BackupSystems!='yes':
            print("Check Backup Systems...")
    
    
        print("\nVehicle Condition Summary: ")
    
        # Check overall condition based on the responses
        warnings = 0
        for condition in [fuel, battery,PowerSystem,Communication,LifeSupportSystem,ScientificInstruments,BackupSystems]:
            if condition != 'yes':
                warnings += 1
    
        if warnings == 0:
            print("Your vehicle is in excellent condition!")
            print("Titan is Ready to Launch")
            time.sleep(5)

        # Countdown from 10 to 1
            for i in range(10, 0, -1):
                print(i)
                time.sleep(1)  # Pause for 1 second between numbers

            print("Congratulations!! Titan Have Launched Successfully: ")
            # continue

        elif warnings <= 3:
            print("Your vehicle is in good condition, but some minor issues need attention.")
        else:
            print("Your vehicle has several issues and needs professional inspection.")
    
# class Speed:
#     def speed(self):


a=Earth()
a.Device_Check()
# a.Earth_launch()
