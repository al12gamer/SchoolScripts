$IP = Get-NetIPAddress | Where-Object {$_.IPv4Address -like '10*'}
$Body = ("My IP address is {0} `n My hostname is {1}" -f $IP.IPv4Address, $env:COMPUTERNAME)
$EmailFrom ="seibenab@uc.edu"
$Subject = "Assignment 2"
$SMTPServer = "smtp.uc.edu"
Send-MailMessage -Body $Body -To "al12gamer@gmail.com" -From $EmailFrom -Subject $Subject -SmtpServer $SMTPServer