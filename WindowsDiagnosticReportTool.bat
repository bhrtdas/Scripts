echo @off
setlocal

SET filepath=%userprofile%\Documents\CS-01\WindowsDiagnosticReport_%username%_%DATE:~10,4%_%DATE:~4,2%_%DATE:~7,2%_%TIME:~0,2%_%TIME:~3,2%_%TIME:~6,2%.txt

CALL :get_system_info

CALL :get_environment

CALL :get_net_config

CALL :get_startup_progs

EXIT /b 0

:get_system_info
echo --- System OS and Processor --- >> %filepath%
echo. >> %filepath%
systeminfo | findstr C:/"Host Name" >> %filepath%
echo. >> %filepath%
systeminfo | findstr C:/"OS Version" >> %filepath%
echo. >> %filepath%
systeminfo | findstr C:/"System Manufacturer" >> %filepath%
echo. >> %filepath%
systeminfo | findstr C:/"System Model" >> %filepath%
echo. >> %filepath%
systeminfo | findstr C:/"System Type" >> %filepath%
echo. >> %filepath%
systeminfo | findstr C:/"Processor(s)" >> %filepath%
echo. >> %filepath%
echo. >> %filepath%
echo. >> %filepath%
EXIT /b 0

:get_environment
echo --- Environment Variables --- >> %filepath%
echo. >> %filepath%
set >> %filepath%
echo. >> %filepath%
echo. >> %filepath%
echo. >> %filepath%
EXIT /b 0

:get_net_config
echo --- Network Configuration --- >> %filepath%
echo. >> %filepath%
ipconfig >> %filepath%
echo. >> %filepath%
echo. >> %filepath%
echo. >> %filepath%
EXIT /b 0

:get_startup_progs
echo --- Start Up Programs --- >> %filepath%
echo Current User >> %filepath%
echo. >> %filepath%
dir C:\Users\globa\AppData\Roaming >> %filepath%
echo. >> %filepath%
echo. >> %filepath%
echo All Users >> %filepath%
dir C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup >> %filepath%
echo. >> %filepath%
echo. >> %filepath%
echo. >> %filepath%
EXIT /b 0

:raid_registry
echo --- RunOnce --- >> %filepath%
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Runonce /ve
echo. >> %filepath%
