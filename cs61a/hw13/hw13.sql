create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select a.name as name, b.size as size from dogs as a, sizes as b where a.height > b.min and a.height <= b.max;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select b.child from dogs as a, parents as b where a.name = b.parent order by -a.height; 

-- Sentences about siblings that are the same size
create table sentences as
    with 
    siblings(s1, s2) as (
        select p1.child , p2.child from parents as p1, parents as p2 where p1.parent = p2.parent and p1.child <> p2.child
    ),
    sizes(s1, s2, size1) as (
        select sib.s1, sib.s2, size1.size from siblings as sib, size_of_dogs as size1, size_of_dogs as size2 where size1.name = sib.s1 and size2.name = sib.s2 and size1.size = size2.size and sib.s1 < sib.s2  
    )
    select sizes.s1 || " and " || sizes.s2 || " are " || sizes.size1 || " siblings" from sizes; 
    --select sib.s1 || " and " || sib.s2 || " are " || sizes.size || " siblings"  from siblings as sib, sizes where ;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with
    ordered(name, height) as (
        select dog.name, dog.height from dogs as dog order by -dog.height
    ),
    pair(names, total, i, n) as (
        select dog.name, dog.height, dog.height, 1 from dogs as dog union
        select dog.name || ", " || dog1.names, dog1.total + dog.height, dog.height, n+1 from pair as dog1, dogs as dog where dog1.i > dog.height and n < 4
    )
    select names, total from pair where total >= 170 order by total;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as 
    with 
        grand_pair(grand, decent, n) as (
            select p.parent, c.child, 1 from parents as p, parents as c where p.child = c.parent union
            select p.child, c.parent, 1 from parents as p, parents as c where p.parent = c.child union
            select p.grand, c.child , n+1 from grand_pair as p, parents as c where p.decent = c.parent and n < 5 union
            select p.decent, c.parent, n +1 from grand_pair as p, parents as c where p.grand = c.child and n < 10
            
        )
        select grand, decent from grand_pair;
        

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
   select n from i;

create table divisors as
    select int.n as int, count(div.n) as divisible from ints as int, ints as div where div.n <= int.n and int.n % div.n = 0 group by int.n;


create table primes as
    select int from divisors where divisible = 2;
