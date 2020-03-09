@echo off
echo    *****************
echo    * CIS 120 FINAL *
echo    * WILKINSON, CJ *
echo    *  THE  TRIALS  *
echo    * OF DAGGERVALE *
echo    *****************
ECHO First, we must check to make sure your system can run the game...
pause
cls
@ECHO OFF 
:: This batch file reveals OS, hardware, and networking configuration. 
:: source @ https://www.windowscentral.com/how-create-and-run-batch-file-windows-10
TITLE Trials of Daggervale
ECHO Please wait... Checking system requirements.
:: Section 1: OS information.
ECHO ============================
ECHO OS INFO
ECHO ============================
systeminfo | findstr /c:"OS Name"
systeminfo | findstr /c:"OS Version"
systeminfo | findstr /c:"System Type"
:: Section 2: Hardware information.
ECHO ============================
ECHO HARDWARE INFO
ECHO ============================
systeminfo | findstr /c:"Total Physical Memory"
wmic cpu get name
:: Section 3: Networking information.
ECHO ============================
ECHO NETWORK INFO
ECHO ============================
ipconfig | findstr IPv4
ipconfig | findstr IPv6
ECHO SUCCESS! You may now run the game!
PAUSE
cls
C:\Users\cw0557613\OneDrive_-_Ozarks_Technical_Community_College\Desktop\Final Bkp\final_ToD.py