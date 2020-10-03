KPI's with SQL

select date(created_at), round(sum(price), 2)
from purchases
group by 1
order by 1;

## is null
select date(created_at), round(sum(price), 2) as daily_rev
from purchases
where refunded_at is null
group by 1
order by 1;

## daily active users
select date(created_at), count(distinct(user_id)) as dau
from gameplays
group by 1
order by 1;

#3rd object
select
  date(created_at),
  platform,
  count(distinct user_id) as dau
from gameplays
group by 1, 2
order by 1, 2;

## Daily Average Revenue Per Purchasing users
select date(created_at), round(sum(price)/count(distinct(user_id)), 2) as arppu
from purchases
where refunded_at is null
group by 1
order by 1;

## CTE = comomn table expressions - usually with cluase
with daily_revenue as (
  select date(created_at) as dt, round(sum(price),2) as rev
  from purchases
  where refunded_at is null
  group by 1
)
select *
from daily_revenue
order by dt;

## CTE - 2nd half of ARPU
with daily_revenue as (
  select date(created_at) as dt, round(sum(price),2) as rev
  from purchases
  where refunded_at is null
  group by 1
),
daily_players as (
  select date(created_at) as dt,
  count(distinct(user_id)) as players
  from gameplays
  group by 1
)
select *
from daily_players
order by dt;

## using is new, join on two created tables ** can also use join blahblah on
## blahblah.dt = blahblah.dt;
with daily_revenue as (
  select
    date(created_at) as dt,
    round(sum(price), 2) as rev
  from purchases
  where refunded_at is null
  group by 1
),
daily_players as (
  select
    date(created_at) as dt,
    count(distinct user_id) as players
  from gameplays
  group by 1
)
select
  daily_revenue.dt,
  daily_revenue.rev / daily_players.players
from daily_revenue
  join daily_players using (dt);

## 1 day retention - self joins
select date(g1.created_at) as dt, g1.user_id
from gameplays as g1
join gameplays as g2 on g1.user_id = g2.user_id
order by 1
limit 100;

## ****review left join
select
  date(g1.created_at) as dt,
  round(100 * count(distinct g2.user_id) /
    count(distinct g1.user_id)) as retention
from gameplays as g1
  left join gameplays as g2 on
    g1.user_id = g2.user_id
    and date(g1.created_at) = date(datetime(g2.created_at, '-1 day'))
group by 1
order by 1
limit 100;
