{ pkgs ? import <nixpkgs> {} }:

let
  makePackage = packageName: version: attrs:
    pkgs.stdenv.mkDerivation {
      name = "${packageName}-${version}";
      src = attrs.src;
      buildInputs = attrs.buildInputs or [];
      installPhase = ''
        mkdir -p $out/bin
        cp -r ${attrs.src}/* $out/bin/
      '';
    };
in
makePackage "meu-script" "1.0.0" {
  src = ./src;
}
