Get-Service | Format-List DisplayName, Status
Get-Service | Format-Table

Get-Service | Sort-Object -Property Status -Descending | Format-Table DisplayName, Status | Out-File C:\services.txt
Install-WindowsFeature -Name