
print(lab 3
% Graph edges 
edge(a, b). 
edge(a, c). 
edge(b, d). 
edge(b, e). 
edge(c, f). 
edge(e, f). 
% Main DFS predicate 
dfs(Start, Goal, Path) :- 
dfs_helper(Start, Goal, [Start], Path). 
% Base case: Goal reached 
dfs_helper(Goal, Goal, Visited, Path) :- 
reverse(Visited, Path). 
% Recursive case: explore next edge 
dfs_helper(Current, Goal, Visited, Path) :- 
edge(Current, Next), 
\+ member(Next, Visited), 
dfs_helper(Next, Goal, [Next|Visited], Path).)
