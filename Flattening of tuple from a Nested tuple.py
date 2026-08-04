 nested_tuple=((1,2),(3,4),(5,6))
 flattened_tuple=tuple(item for subtuple in nested_tuple for item in subtuple)
  print("Nested tuple:",nested_tuple)
  print("Flattened tuple:",flattened_tuple)
