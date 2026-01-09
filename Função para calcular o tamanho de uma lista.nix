let
  lengthOfList = list: builtins.length list;
in
{
  description = "Tamanho da lista: ${toString (lengthOfList [ "a" "b" "c" ])}";
}
