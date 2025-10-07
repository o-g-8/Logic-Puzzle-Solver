int: M;
int: P;
int: H;
int: PRI;
set of int: Monitor = 0..M-1;
set of int: Processor = 0..P-1;
set of int: Harddisk = 0..H-1;
set of int: Price = 0..PRI-1;

array[Monitor, Processor] of var bool:P1;
array[Monitor, Harddisk] of var bool:P2;
array[Monitor, Price] of var bool:P3;


constraint forall(m in Monitor) (
  sum(k in Processor)(P1[m,k]) == 1 /\
  sum(k in Harddisk)(P2[m,k]) == 1 /\
  sum(k in Price)(P3[m,k]) == 1
);

constraint forall(p in Processor) (
  sum(k in Monitor)(P1[k,p]) == 1
);

constraint forall(h in Harddisk) (
  sum(k in Monitor)(P2[k,h]) == 1
);

constraint forall(p in Price) (
  sum(k in Monitor)(P3[k,p]) == 1
);


 % Solve
solve satisfy; % T
