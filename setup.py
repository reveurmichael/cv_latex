#!/usr/bin/env python3
import os
import sys
import argparse
import importlib.util

def check_python_version():
    """Check if Python version is at least 3.6"""
    if sys.version_info < (3, 6):
        print("Error: Python 3.6 or higher is required")
        sys.exit(1)

def import_script(script_name):
    """Import a Python script as a module"""
    spec = importlib.util.spec_from_file_location(script_name, f"{script_name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    """Main function that handles command line arguments and runs the appropriate scripts"""
    check_python_version()
    
    parser = argparse.ArgumentParser(description="LaTeX CV Builder Setup Tool")
    parser.add_argument("--all", action="store_true", help="Run all setup scripts")
    parser.add_argument("--vscode", action="store_true", help="Setup VSCode configuration")
    parser.add_argument("--devcontainer", action="store_true", help="Setup DevContainer configuration")
    parser.add_argument("--docker", action="store_true", help="Build using Docker")
    
    args = parser.parse_args()
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    
    try:
        if args.all or args.vscode:
            print("\n=== Setting up VSCode configuration ===")
            vscode_module = import_script("setup_vscode")
            vscode_module.create_vscode_settings()
        
        if args.all or args.devcontainer:
            print("\n=== Setting up DevContainer configuration ===")
            devcontainer_module = import_script("setup_devcontainer")
            devcontainer_module.create_devcontainer_config()
        
        if args.all or args.docker:
            print("\n=== Building with Docker ===")
            docker_module = import_script("docker_build")
            docker_module.check_docker()
            docker_module.build_cv()
        
        if args.all:
            print("\n=== All setup tasks completed successfully ===")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 