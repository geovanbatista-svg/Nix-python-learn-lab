let
  joinList = list: builtins.concatStringsSep ", " list;
  filterList = condition: list: builtins.filter condition list;
in
{
  description = "Filtro lista: ${
    joinList (
      filterList
        (x: x != "b")
        [ "a" "b" "c" "d" ]
    )
  }";
}