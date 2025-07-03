import subprocess
import sys

def run_general_bot():
    print("\n🔁 Launching General Baby Assistant...\n")
    subprocess.run([sys.executable, "text_to_text.py"])

def run_vaccine_bot():
    print("\n🔁 Launching Vaccine Assistant...\n")
    subprocess.run([sys.executable, "vaccine.py"])

if __name__ == "__main__":
    print("👶 Welcome to the Baby Care Assistant!")
    print("Please choose an option:")
    print("1️⃣  General Baby Questions")
    print("2️⃣  Vaccine Schedule / FAQ")

    choice = input("\nEnter 1 or 2: ").strip()

    if choice == "1":
        run_general_bot()
    elif choice == "2":
        run_vaccine_bot()
    else:
        print("❌ Invalid choice. Please run the program again.")
