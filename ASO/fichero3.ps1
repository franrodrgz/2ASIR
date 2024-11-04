cls
do {
    Write-Host "1. Muestra las propiedades básicas del adaptador de red."
    Write-Host "2. Muestra configuración de la dirección IP, tanto IPv4 como IPv6 y las interfaces de red respectivas."
    Write-Host "3. Ejecuta comando Get-NetIPConfiguration, indicando que realiza."
    Write-Host "4. Ejecuta comando Get-NetConnectionProfile."
    Write-Host "5. Muestra la ruta que usan los paquetes en el proceso de envío y recepción."
    Write-Host "6. Muestra la información detallada de cada adaptador indicando su estado, velocidad e identificador VLAN si posee alguno."
    Write-Host "7. Ejecuta tracert."
    Write-Host "8. Comprueba el estado de los puertos abiertos del equipo."
    Write-Host "9. Ejecutar NSLOKKUP. ¿Qué realiza este comando?"
    Write-Host "10. Comprueba el estado actual de la red."
    Write-Host "11. La ruta que usan los paquetes de nuestra red en el proceso de envío y recepción."
    Write-Host "12. Obtener información detallada de cada adaptador indicando su estado, velocidad, etc."
    Write-Host "13. Realizar un test de los puertos de nuestro sistema."
    Write-Host "14. Obtener la dirección MAC de nuestra interfaz de red. Investiga la posibilidad de cambiar la misma."
    Write-Host "15. Salir."
    $x=Read-Host "Selecciona una opción"

if ($x -eq 1) 
{
    cls
    Get-NetAdapter
}
if ($x -eq 2) 
{
    cls
    Get-NetIPAddress
}
if ($x -eq 3) 
{
    cls
    Get-NetIPConfiguration
    Write-Host "El comando Get-NetIPConfiguration obtiene la configuración de red, incluidas las interfaces utilizables, las direcciones IP y los servidores DNS"

}
if ($x -eq 4) 
{
    cls
    Get-NetConnectionProfile
}
if ($x -eq 5) 
{
    cls
    Test-NetConnection
}
if ($x -eq 6) 
{
    cls
    Get-NetAdapterAdvancedProperty
}
if ($x -eq 7) 
{
    cls
    tracert 8.8.8.8
}
if ($x -eq 8) 
{
    cls
    netstat
}
if ($x -eq 9) 
{
    cls
    Start-Process nslookup
    Write-Host "El comando nslookup (Name Server Lookup) se utiliza para consultar servidores DNS y obtener información sobre nombres de dominio o direcciones IP."
}
if ($x -eq 10) 
{
    cls
    Get-NetTCPConnection | Where-Object { $_.State -eq 'Listen' }
}
if ($x -eq 11) 
{
    cls
    Get-NetRoute
}
if ($x -eq 12) 
{
    cls
    Get-NetAdapter | Select-Object Name, InterfaceDescription, Status, LinkSpeed, MacAddress
}
if ($x -eq 13) 
{
    cls
    Get-NetTCPConnection
}
if ($x -eq 14) 
{
    cls
    Get-NetAdapter | Select-Object Name, MacAddress, Status
}
if ($x -ne 15)
{
    Read-Host "Pulsa para continuar"
}
} while ($x -ne 15)
