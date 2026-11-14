
"""
Insulin Pump Control System
Educational simulation only.
This program does not control real medical equipment.
"""

from pump_controller import PumpController


def main():
    print("=" * 45)
    print("     INSULIN PUMP CONTROL SYSTEM")
    print("          EDUCATIONAL DEMO")
    print("=" * 45)

    controller = PumpController()

    while True:
        print("\n1. Start system")
        print("2. View system status")
        print("3. View event log")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            controller.run_cycle()

        elif choice == "2":
            controller.show_status()

        elif choice == "3":
            controller.show_logs()

        elif choice == "4":
            print("Exiting educational simulation. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
