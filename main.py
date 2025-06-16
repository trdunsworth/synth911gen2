#!/usr/bin/env python

import sys
import os

def main():
    """
    Main entry point for the synth911gen2 application.
    Launches the GUI interface for generating synthetic 911 data.
    """
    try:
        # Import the GUI module
        from synthgui import main as gui_main
        
        # Launch the GUI
        gui_main()
    except ImportError as e:
        print(f"Error importing GUI module: {e}")
        print("Make sure tkinter is installed on your system.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
