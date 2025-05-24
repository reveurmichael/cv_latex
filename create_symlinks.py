#!/usr/bin/env python3
"""
Create symbolic links from old file names to new ones for backward compatibility
"""
import os
import platform
import sys

def create_symlinks():
    """Create symbolic links from old file names to new ones"""
    
    # Map of old file name to new file name
    file_mapping = {
        "setup.py": "cli_setup.py",
        "cv_setup.py": "interactive_setup.py",
        "setup_vscode.py": "vscode_config.py",
        "setup_devcontainer.py": "devcontainer_config.py",
        "docker-build.sh": "docker_build.sh"
    }
    
    windows = platform.system() == "Windows"
    
    print("Creating symbolic links for backward compatibility...")
    
    for old_file, new_file in file_mapping.items():
        # Skip if the old file already exists as a regular file
        if os.path.isfile(old_file) and not os.path.islink(old_file):
            print(f"Skipping {old_file} -> {new_file}: original file exists")
            continue
            
        # Skip if the new file doesn't exist
        if not os.path.isfile(new_file):
            print(f"Skipping {old_file} -> {new_file}: target file doesn't exist")
            continue
            
        # Create symbolic link
        try:
            # Remove existing symlink if it exists
            if os.path.islink(old_file):
                os.unlink(old_file)
                
            if windows:
                # On Windows, we need administrator privileges for symlinks
                # Instead, create a simple Python script that imports and runs the new file
                with open(old_file, 'w') as f:
                    f.write(f'#!/usr/bin/env python3\n')
                    f.write(f'import {os.path.splitext(new_file)[0]}\n')
                    f.write(f'# This is a compatibility script that redirects to {new_file}\n')
                    
                    # If the file has a main function or is meant to be executed, add execution code
                    if new_file.endswith(".py"):
                        f.write(f'# Execute the same code as the target file\n')
                        f.write(f'if __name__ == "__main__":\n')
                        f.write(f'    # Import all attributes from the module\n')
                        f.write(f'    from {os.path.splitext(new_file)[0]} import *\n')
                        f.write(f'    # If the module has a main function, call it\n')
                        f.write(f'    if "main" in globals():\n')
                        f.write(f'        main()\n')
                
                print(f"Created Python redirection script: {old_file} -> {new_file}")
            else:
                # On Unix, create a proper symlink
                os.symlink(new_file, old_file)
                print(f"Created symbolic link: {old_file} -> {new_file}")
                
        except Exception as e:
            print(f"Error creating link {old_file} -> {new_file}: {e}")
    
    print("Done creating symbolic links.")

if __name__ == "__main__":
    create_symlinks() 