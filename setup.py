from cx_Freeze import setup, Executable

# pip install -r requirements.txt
# python setup.py build

setup(
    name="YourAppName",
    version="0.1",
    description="Your application description",
    executables=[Executable("hotkeys.py")]
)