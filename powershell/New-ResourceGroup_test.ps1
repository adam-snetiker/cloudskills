# To run the test:
# Invoke-Pester .\New-ResourceGroup_test.ps1

Describe "New-ResourceGroup" {
    $location = 'westus'
    $name = 'snetRG01'

    It "name should be snetRG01" {
        $name | Should Be 'snetRG01'
    }

    It "location should be westus" {
        $location | Should Be 'westus'
    }
}