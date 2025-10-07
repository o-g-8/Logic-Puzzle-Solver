int: A;
int: F;
int: D;
int: T;
set of int: Actor = 0..A-1;
set of int: Film = 0..F-1;
set of int: Day = 0..D-1;
set of int: Time = 0..T-1;

array[Actor, Film] of var bool:P1;
array[Actor, Day] of var bool:P2;
array[Actor, Time] of var bool:P3;


constraint forall(a in Actor) (
  sum(k in Film)(P1[a,k]) == 1 /\
  sum(k in Day)(P2[a,k]) == 1 /\
  sum(k in Time)(P3[a,k]) == 1
);

constraint forall(f in Film) (
  sum(k in Actor)(P1[k,f]) == 1
);

constraint forall(d in Day) (
  sum(k in Actor)(P2[k,d]) == 1
);

constraint forall(t in Time) (
  sum(k in Actor)(P3[k,t]) == 1
);


 % Solve
solve satisfy; % T