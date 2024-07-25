"""
 21. Write a menu driven program- 1.cm to ft 2.kl to miles 3.usd to inr
 4.exit
"""
def kl_to_miles(kl):
   return 0.6213711922*kl
def cm_to_ft(cm):
    return 0.03280839895*cm
def usd_to_inr(usd, conversion_rate):
    return usd*conversion_rate
def main():
        while True:
            print("\nMenu:")
            print("1. cm to ft")
            print("2. kl to miles")
            print("3. usd to inr")
            print("4. Exit")
            choice = input("Enter your choice from 1-4: ")
            if choice == "1":
                cm = float(input("Enter cm value: "))
                print(f"{cm} cm is {cm_to_ft(cm):.4f} ft")
            elif choice == "2":
                kl = float(input("Enter a km value: "))
                print(f"{kl} km is  {kl_to_miles(kl):.3f} km miles ")
            elif choice == "3":
                usd = float(input("Enter value in USD: "))
                conversion_rate = float(input("Enter conversion rate (1 USD to INR): "))
               # inr = usd_to_inr(usd, conversion_rate)
                print(f"{usd} USD is equal to {usd_to_inr(usd, conversion_rate):.2f} INR")
            elif choice == "4":
                print("I am done")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4 ")
if __name__ == '__main__':
    main()