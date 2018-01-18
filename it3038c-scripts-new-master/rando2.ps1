$RAND0=0
$LogFile = "C:\logs\rando.log"

for($i=0; $i -lt 5; $i++){
    $RAND0=Get-Random -Maximum 1000 -Minimum 1
    Write-Host($RAND0)
    Add-Content $LogFile "INFO: Random Number is ${RAND0}"
    }