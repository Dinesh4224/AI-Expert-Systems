domains
        loc=right; middle; left
predicates
            hanoi(integer)
            move(integer, loc, loc, loc)
            inform(loc, loc)
    
clauses
       hanoi(N):- move(N, left, middle, right).
            move(1, A, _, C):- inform(A, C),!
            move(N, A, B, C):-
                    N!=N-1, move(N1, A, C, B),
                        inform(A, C),
                        move(N1, B, A, C)
            inform(LOC1, LOC2):-
        write("\n Move a disk from", LOC1, "to", LOC2).