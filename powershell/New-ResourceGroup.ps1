Import-Module Az.Resources

<# Create a new Azure Resource Group#>
function New-ResourceGroup {
    [cmdletbinding()]

    param (
        [parameter(Mandatory)]
        [string]$rgName,

        [parameter(Mandatory)]
        [string]$location
    )

    $params = @{
        'Name' = $rgName
        'Location' = $location
    }

    New-AzResourceGroup @params
}

<# Add new tag to an Azure resource#>
function New-Tag {
    [cmdletbinding()]

    param (
        [parameter(Mandatory)]
        [string]$resourceID,

        [parameter(Mandatory)]
        [string]$tagName,

        [parameter(Mandatory)]
        [string]$tagValue
    )

    $params = @{
        'ResourceId' = $resourceID
        'Name' = $tagName
        'Value' = $tagValue
    }

    New-AzTag @params
}