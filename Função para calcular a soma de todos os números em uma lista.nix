let
  addNumbers = a: b: a + b;
  sumList = list: builtins.foldl' addNumbers 0 list;
in
  sumList [ 1 2 3 4 5 ]  # Evaluates to 15