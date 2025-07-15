Set WshShell = CreateObject("WScript.Shell")

' Set working directory to Python script location
WshShell.CurrentDirectory = "{code directory}"

' Run Python script using virtual environment
WshShell.Run "{Your python path} main.py", 1, True

' Show completion message
WScript.Echo "Python script completed"