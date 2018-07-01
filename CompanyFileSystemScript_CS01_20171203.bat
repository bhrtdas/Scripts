REM Set the local password policy.

NET ACCOUNTS /FORCELOGOFF:15 /MINPWLEN:8 /MAXPWAGE:90 /MINPWAGE:1 /UNIQUEPW:5

REM Create the groups for the filing system.

net localgroup owners /add /comment:"These people pay you."
net localgroup developers /add /comment:"They make the tools upon which you depend."
net localgroup employees /add /comment:"AKA the worker bees."
net localgroup contractors /add /comment:"Dirty human beings with dark souls, practically gingers." 
net localgroup managers /add /comment:"They tell you what to do, but they don't pay you. 
net localgroup sysadmins /add /comment:"Call them when your computer won't work, so they can ask you if it's plugged in." 
net localgroup marketing /add /comment:"Masters of subliminal messages." 
net localgroup sales /add /comment:"Will Just. Not. Shut. Up!" 
net localgroup accounting /add /comment:"They like to count beans." 
net localgroup it /add /comment:"Odd creatures. Tend to be found in closets and basements."
 
REM Create the user accounts and set the password REM so user is requested to change it upon first login. 

SET xeno="Scr00wed!"

net user devleague %xeno% /logonpasswordchg:yes /add
net user bart %xeno% /logonpasswordchg:yes /add
net user ross %xeno% /logonpasswordchg:yes /add
net user nick %xeno% /logonpasswordchg:yes /add
net user kaleo %xeno% /logonpasswordchg:yes /add
net user jason %xeno% /logonpasswordchg:yes /add
net user russel %xeno% /logonpasswordchg:yes /add
net user mary %xeno% /logonpasswordchg:yes /add
net user tyler %xeno% /logonpasswordchg:yes /add
net user tina %xeno% /logonpasswordchg:yes /add
net user alyssa %xeno% /logonpasswordchg:yes /add

REM Assign users to appropriate groups

net localgroup Administrators devleague /add
net localgroup developers bart kaleo mary alyssa /add
net localgroup contractors bart mary tyler /add
net localgroup accounting ross tyler /add  
net localgroup managers ross nick kaleo alyssa /add
net localgroup owners russel jason /add 
net localgroup sysadmins kaleo alyssa /add
net localgroup marketing jason tina /add
net localgroup sales nick jason /add
net localgroup employees ross nick kaleo jason russel tina alyssa /add


REM Create the parent directory. 

cd c:\
mkdir CompanyFileSystem

REM Set permissions on parent directory and disable inheritance. Users have read (R) access which, importantly, means they can neither create or delete any immediate subfolders. 

icacls CompanyFileSystem /inheritance:r

icacls CompanyFileSystem /grant:r Administrators:(F) Users:(R) sysadmins:(M)


REM Create the Departments directory and set the permissions.

mkdir C:\CompanyFileSystem\Departments
SET filepath=C:\CompanyFileSystem\Departments
mkdir %filepath%\Sales
mkdir %filepath%\Accounting
mkdir %filepath%\Marketing
mkdir %filepath%\IT

REM Disable inheritance and deny ability to delete or create objects to users by granting read only access. 

icacls %filepath% /inheritance:r

icacls %filepath% /grant:r owners:(R) employees:(R) managers:(R) Administrators:(F) sysadmins:(M) 

icacls %filepath% /deny contractors:(F)  

REM Set the permissions for the sub-directories. Allow employees in the department to read, write, execute, add and delete child folders. Keep inheritance enabled, so it persists into user created files. 

icacls %filepath%/Sales /grant:r owners:(R) employees:(R) managers:(R) Administrators:(F) sysadmins:(M) sales:(RX,W,DC)

icacls %filepath%/Accounting /grant:r owners:(R) employees:(R) managers:(R) Administrators:(F) sysadmins:(M) accounting:(RX,W,DC)

icacls %filepath%/Marketing /grant:r owners:(R) employees:(R) managers:(R) Administrators:(F) sysadmins:(M) marketing:(RX,W,DC)

icacls %filepath%/IT /grant:r owners:(R) employees:(R) managers:(R) Administrators:(F) sysadmins:(M) it:(RX,W,DC)

REM Create the Managers directory and subdirectories. Disable inheritance and deny ability to delete or create objects to managers, etc. by granting read only access. Deny access to contractors and employees. 

mkdir C:\CompanyFileSystem\Managers
SET filepath=C:\CompanyFileSystem\Managers
mkdir %filepath%\SalesManager
mkdir %filepath%\AccountingManager
mkdir %filepath%\MarketingManager
mkdir %filepath%\ITManager

icacls %filepath% /inheritance:r

icacls %filepath% /grant:r owners:(R) managers:(R) Administrators:(F) sysadmins:(M) 

icacls %filepath% /deny contractors:(F) employees:(F)

REM Set the permissions for each department manager's sub-directories. Allow managers in the department to read, write, execute, add and delete child folders. Keep inheritance enabled, so it persists into user created files. 

icacls %filepath%/SalesManager /grant:r owners:(R) Administrators:(F) sysadmins:(M) sales:(RX,W,DC)

icacls %filepath%/AccountingManager /grant:r owners:(R) Administrators:(F) sysadmins:(M) accounting:(RX,W,DC)

icacls %filepath%/MarketingManager /grant:r owners:(R) Administrators:(F) sysadmins:(M) marketing:(RX,W,DC)

icacls %filepath%/ITManager /grant:r owners:(R) Administrators:(F) sysadmins:(M) it:(RX,W,DC)

REM Create the owners' directory. Enable inheritance and set the permissions to allow owners in the department to read, write, execute, add and delete child folders. Deny access to contractors, managers and employees.

mkdir C:\CompanyFileSystem\Owners
SET filepath=C:\CompanyFileSystem\Owners 

icacls %filepath% /inheritance:e

icacls %filepath% /grant:r owners:(RX,W,DC) Administrators:(F) sysadmins:(M) 

icacls %filepath% /deny contractors:(F) employees:(F) managers:(F) 

REM Create the company's shared drive. Enable inheritance and set the permissions to allow Users group to read, write, execute, add and delete child folders.  

mkdir C:\CompanyFileSystem\SharedDrive
SET filepath=C:\CompanyFileSystem\SharedDrive

icacls %filepath% /inheritance:e

icacls %filepath% /grant:r Users:(RX,W,DC) Administrators:(F) sysadmins:(M)