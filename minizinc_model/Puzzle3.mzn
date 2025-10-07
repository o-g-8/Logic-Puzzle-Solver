int: P = 3;
int: O = 3;
int: Pl = 3;

set of int: Person = 0..P-1;
set of int: Object = 0..O-1;
set of int: Place = 0..Pl-1;


array[Person, Object] of var bool:P1;
array[Person, Place] of var bool:P2;


constraint forall(p in Person) (
  sum(k in Object)(P1[p,k]) == 1 /\
  sum(k in Place)(P2[p,k]) == 1
);

constraint forall(o in Object) (
  sum(k in Person)(P1[k,o]) == 1
);

constraint forall(pl in Place) (
  sum(k in Person)(P2[k,pl]) == 1
);

 % Solve
solve satisfy; % T