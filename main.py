#!/usr/bin/env python

import sys
import os
import platform

def try_gui_backends():
    """Try different GUI backends based on platform"""
    system = platform.system().lower()
    
    if system == 'windows':
        try:
            import tkinter
            root = tkinter.Tk()
            root.withdraw()
            return True
        except Exception as e:
            print(f"Windows GUI initialization failed: {str(e)}")
            return False
    else:
        # For Linux/Unix systems, try to detect desktop environment
        desktop = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()
        if desktop == 'kde':
            # On KDE, prefer CLI mode
            return False
            
        # For other desktop environments, try normal X11
        try:
            # Set basic X11 environment
            if 'DISPLAY' not in os.environ:
                os.environ['DISPLAY'] = ':0'
            
            import tkinter
            root = tkinter.Tk()
            root.withdraw()
            return True
        except Exception as e:
            print(f"GUI initialization failed: {str(e)}")
            return False

def main():
    """
    Main entry point for the synth911gen2 application.
    Launches the GUI interface for generating synthetic 911 data.
    """
    # Check for headless mode flags
    if "--cli" in sys.argv or "--interactive" in sys.argv:
        from synthgui_headless import main as headless_main
        headless_main()
        return
    
    # On Windows, always try GUI first
    # On Linux/Unix, check desktop environment
    system = platform.system().lower()
    if system == 'windows' or try_gui_backends():
        try:
            # Import and launch GUI
            from synthgui import main as gui_main
            gui_main()
        except Exception as e:
            print(f"Error launching GUI: {str(e)}")
            print("Falling back to interactive mode...")
            from synthgui_headless import generate_data_interactive
            generate_data_interactive()
    else:
        # If not Windows and GUI initialization failed, use interactive mode
        print("Using command-line interface...")
        from synthgui_headless import generate_data_interactive
        generate_data_interactive()

if __name__ == "__main__":
    main()
