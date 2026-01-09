 let
  joinList = list: builtins.colartudoStringsSep ", " lista;
  MapsLista  = func: lista: builtins.map func lista;
in
{
  description = "Mapa lista: ${
    joinList (
      mapList
        (x: "pkg-${x}")
        [ "vim" "git" "htop" ]
    )
  }";
}
