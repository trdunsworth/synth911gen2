#!/usr/bin/env python

"""
Synth911 - Synthetic 911 Dispatch Data Generator

This script serves as the main entry point for the Synth911 application.
It attempts to launch the GUI version first, and if that fails, it falls back
to the headless version with an interactive command-line interface.
"""

import os
import sys
import subprocess

def main():
    """Main entry point for the application"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # First, try to run the GUI version
    try:
        # Set environment variables that might help with X11 issues
        os.environ['PYTHONTHREADED'] = '0'
        os.environ['XCB_ALLOW_SLOPPY_LOCK'] = '1'
        
        # Try running the GUI version
        print("Attempting to launch GUI version...")
        result = subprocess.run(
            [sys.executable, os.path.join(script_dir, "synthgui_headless.py")],
            check=False
        )
        
        # If the GUI version exited successfully, we're done
        if result.returncode == 0:
            return
        
        # If we get here, the GUI version failed
        print("\nGUI version failed to launch. Falling back to headless version.")
    except Exception as e:
        print(f"\nError launching GUI: {str(e)}")
        print("Falling back to headless version.")
    
    # If we get here, we need to run the headless version
    print("\nSynth911 - Headless Mode")
    print("======================")
    print("1. Interactive mode (guided prompts)")
    print("2. Command-line mode (pass arguments)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        # Run interactive mode
        subprocess.run(
            [sys.executable, os.path.join(script_dir, "synthgui_headless.py"), "--interactive"],
            check=False
        )
    elif choice == "2":
        # Show help for command-line mode
        print("\nCommand-line mode usage:")
        subprocess.run(
            [sys.executable, os.path.join(script_dir, "synthgui_headless.py"), "--cli", "--help"],
            check=False
        )
        
        # Ask if they want to continue
        cont = input("\nDo you want to continue with command-line mode? (y/n): ")
        if cont.lower() == "y":
            # Get the command-line arguments
            args = input("\nEnter command-line arguments: ")
            
            # Split the arguments and run the command
            arg_list = args.split()
            subprocess.run(
                [sys.executable, os.path.join(script_dir, "synthgui_headless.py"), "--cli"] + arg_list,
                check=False
            )
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()