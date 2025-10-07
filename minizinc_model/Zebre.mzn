int: S = 5; % Shirt
int: N = 5; % Name
int: H = 5; % Surname
int: P = 5; % Pasta
int: W = 5; % Wine
int: A = 5; % Age
int: Wo = 5; % Women

set of int: Shirt = 0..S-1;
set of int: Name = 0..N-1;
set of int: Surname = 0..H-1;
set of int: Pasta = 0..P-1;
set of int: Wine = 0..W-1;
set of int: Age = 0..A-1;
set of int: Women = 0..Wo-1;

array[Women, Shirt] of var bool: P1;
array[Women, Name] of var bool: P2;
array[Women, Surname] of var bool: P3;
array[Women, Pasta] of var bool: P4;
array[Women, Wine] of var bool: P5;
array[Women, Age] of var bool: P6;

constraint forall(w in Women) (
  sum(s in Shirt)(P1[w,s]) == 1 /\
  sum(n in Name)(P2[w, n]) == 1 /\
  sum(h in Surname)(P3[w, h]) == 1 /\
  sum(p in Pasta)(P4[w, p]) == 1 /\
  sum(wi in Wine)(P5[w, wi]) == 1 /\
  sum(a in Age)(P6[w, a]) == 1
);

constraint forall(s in Shirt) (
  sum(w in Women)(P1[w, s]) == 1
);

constraint forall(n in Name) (
  sum(w in Women)(P2[w, n]) == 1
);

constraint forall(h in Surname) (
  sum(w in Women)(P3[w, h]) == 1
);

constraint forall(p in Pasta) (
  sum(w in Women)(P4[w, p]) == 1
);

constraint forall(wi in Wine) (
  sum(w in Women)(P5[w, wi]) == 1
);

constraint forall(a in Age) (
  sum(w in Women)(P6[w, a]) == 1
);

% Solve
solve satisfy; % T
