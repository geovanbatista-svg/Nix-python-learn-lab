def make_package(package_name, version, attrs):
    package_info = {
        "name": f"{package_name}-{version}",
        "src": attrs.get("src"),
        "buildInputs": attrs.get("buildInputs", []),
    }
    
    # Simulando a fase de instalação
    print(f"Creating package: {package_info['name']}")
    print(f"Source directory: {package_info['src']}")
    print(f"Build inputs: {package_info['buildInputs']}")
    print("Running install phase...")
    print(f"Creating output directory: $out/bin")
    print(f"Copying files from {attrs['src']} to $out/bin/")
    # Aqui você poderia adicionar lógica para realmente copiar os arquivos se necessário
    
# Chamada da função
make_package("meu-script", "1.0.0", {
    "src": "./src",
})