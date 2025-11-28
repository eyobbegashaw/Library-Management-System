#!/usr/bin/env python3
"""
Setup script for DBU Tech Library Management System
This script verifies all dependencies are available
"""

import sys
import sqlite3
import tkinter as tk

def check_dependencies():
    """Check if all required dependencies are available"""
    print("Checking dependencies...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    else:
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    # Check Tkinter
    try:
        test = tk.Tk()
        test.destroy()
        print("✅ Tkinter is available")
    except:
        print("❌ Tkinter is not available")
        return False
    
    # Check SQLite3
    try:
        conn = sqlite3.connect(':memory:')
        conn.close()
        print("✅ SQLite3 is available")
    except:
        print("❌ SQLite3 is not available")
        return False
    
    print("\n🎉 All dependencies are satisfied!")
    print("You can run the application with: python src/login.py")
    return True

if __name__ == "__main__":
    check_dependencies()