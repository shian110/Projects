% 決定変数  N:枠の番号 T:割り当て時間(11:30-11:40、など) B:バンド(休憩も含む)
%各バンドは一回出演する
{assign(T,B) : time(N, T)} =1 :- band(B).

assign_mem(N, H):-assign(T,B), member(B,H), time(N, T).


% 各人は、出演の間隔を2枠以上取る必要がある
:- assign_mem(N,H),assign_mem(N+1,H), member(B,H), time(N, T).
:- assign_mem(N,H),assign_mem(N+2,H), member(B,H), time(N, T). 
% 各枠は一つのバンドまたは休憩のみが割り当てられる(at-most-one),
:- not {assign(T,B): band(B)} 1, time(N, T).
:- assign(T,B), band(B), assign(T,"休憩").

%10分枠のバンドは10分の枠に入る
:- not {assign(T,B) : ten_time(N), time(N,T), ten_band(B)}=5.

:- not assign("16:50-17:00","証明写真19秒").
:- not assign("13:20-13:25","魔法のコトバ企画").
:- assign(T,"HomeFlee"), time(N,T), N<25.
#show member/2.
#show assign/2.
