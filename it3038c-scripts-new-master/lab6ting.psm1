Function Create-Users{
    param($fileName, $emailDomain, $userPass, $numAccounts=10)  
    if($fileName -eq $null ){
        [array]$users  = $null
        for($i=0; $i -lt $numAccounts; $i++){
            $users += [PSCustomObject]@{
            FirstName = 'Random'
            LastName = 'User' + $i
            }
        }
    } else {
        $users = Import-Csv -Path $fileName
    }

    ForEach($user in $users)
    {
        $password = ''
        if($userPass)
        {
            $password = $userPass 
        } else {
            $password = Get-RandomPass
        }
        Create-User -firstName $user.FirstName `
        -lastName $user.LastName -emailDomain $emailDomain `
        -password $password
    } 
}

Function Create-User
{
    param($firstName, $lastName, $emailDomain, $password)
    $accountName = '{0}.{1}' -f $firstName, $lastName
    $emailAddr = '{0}@{1}' -f $accountName, $emailDomain
    $securePass = ConvertTo-SecureString $password -AsPlainText -Force

    New-ADUser -Name $accountName -AccountPassword $securePass `
    -ChangePasswordAtLogon $true -EmailAddress $emailAddr `
    -Displayname "$FirstName $Lastname"  -GivenName $Firstname `
    -Surname $LastName -Enabled $true

    Write-Host "$LastName,$FirstName,$AccountName,$emailAddr,$password"
}

function Get-RandomPass{
    $newPass = '' 
    1..10 | ForEach-Object { 
        $newPass += [char](Get-Random -Minimum 48 -Maximum 122)
    }
    return $newPass
}