#!/usr/bin/env python3
"""
CV Setup Tool - A user-friendly interface for LaTeX CV Builder setup
"""
import os
import sys
import platform
import subprocess

def clear_screen():
    """Clear the terminal screen in a platform-independent way"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_header():
    """Print the tool header"""
    clear_screen()
    print("="*60)
    print("             LaTeX CV Builder Setup Tool")
    print("="*60)
    print("\nThis tool helps you set up your LaTeX CV environment.\n")

def print_menu():
    """Print the main menu options"""
    print("\nPlease select an option:")
    print("1. Set up VSCode configuration")
    print("2. Set up DevContainer configuration")
    print("3. Build CV using Docker")
    print("4. Set up everything (all of the above)")
    print("5. Exit")
    print()

def run_setup_script(args):
    """Run the setup.py script with the given arguments"""
    cmd = [sys.executable, "setup.py"] + args
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\nError running setup script: {e}")
    
    input("\nPress Enter to continue...")

def main():
    """Main function for the CV setup tool"""
    while True:
        print_header()
        print_menu()
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            run_setup_script(["--vscode"])
        elif choice == "2":
            run_setup_script(["--devcontainer"])
        elif choice == "3":
            run_setup_script(["--docker"])
        elif choice == "4":
            run_setup_script(["--all"])
        elif choice == "5":
            print("\nExiting setup tool. Thank you for using LaTeX CV Builder!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main() 