#!/usr/bin/env python3
"""
COMPASS Setup Script
Automatically sets up the COMPASS design survey automation tool.
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is 3.7 or higher."""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required.")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_dependencies():
    """Install required Python packages."""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def create_directories():
    """Create necessary directories."""
    print("\n📁 Creating directories...")
    directories = [
        "my_pages",
        "design_survey_results/1_personas",
        "design_survey_results/2_page_inventories", 
        "design_survey_results/3_scenarios",
        "design_survey_results/4_feedback_results",
        "design_survey_results/5_final_reports"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created: {directory}")

def create_env_file():
    """Create .env file template."""
    print("\n🔑 Creating environment file template...")
    env_content = """# COMPASS Configuration
# Add your Gemini API key here
GEMINI_API_KEY=your_api_key_here

# Optional: Configure other settings
# API_ENDPOINT=https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent
# MAX_RETRIES=3
# TIMEOUT=30
"""
    
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write(env_content)
        print("✅ Created .env file template")
        print("⚠️  Please add your Gemini API key to the .env file")
    else:
        print("✅ .env file already exists")

def create_sample_pages():
    """Create sample page structure."""
    print("\n📄 Creating sample page structure...")
    
    sample_pages = [
        ("assistant", "AI Assistant Interface"),
        ("dashboard", "Main Dashboard"),
        ("settings", "Settings Page")
    ]
    
    for page_name, description in sample_pages:
        txt_file = f"my_pages/{page_name}.txt"
        if not os.path.exists(txt_file):
            with open(txt_file, "w") as f:
                f.write(f"# {description}\n\n")
                f.write("This is a sample page description.\n")
                f.write("Replace this with your actual page description.\n")
                f.write("Include details about:\n")
                f.write("- Main features and functionality\n")
                f.write("- User interactions available\n")
                f.write("- Key UI elements and their purposes\n")
            print(f"✅ Created sample: {txt_file}")

def main():
    """Main setup function."""
    print("🧭 COMPASS Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Create directories
    create_directories()
    
    # Create environment file
    create_env_file()
    
    # Create sample pages
    create_sample_pages()
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Add your Gemini API key to the .env file")
    print("2. Add your page screenshots to my_pages/ (PNG format)")
    print("3. Update the page descriptions in my_pages/*.txt")
    print("4. Run: python main_controller.py")
    print("\n📚 For more information, see README.md")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
