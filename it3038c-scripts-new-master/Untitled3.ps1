Get-NetIPAddress | Where-Object {$_.IPv4Address -like '10*'}
Write-Output($IP)
Write-Output($IP.IPv4Address)
Write-Output("My IP Address is $IP")
Write-Output("My IP address is {0}" -f $IP.IPv4Address)