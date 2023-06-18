$packages = @(
    "numpy",
    "pandas",
    "matplotlib"
    # Dodaj inne potrzebne pakiety tutaj
)

foreach ($package in $packages) {
    Write-Host "Installing package: $package"
    pip install $package
}