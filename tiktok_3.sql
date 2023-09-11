select U.email, count(distinct(*))
from users_tasks UT
join users U
join tasks T 
on UT.user_id = U.id and UT.task_id = T.id
where T.status = 'Open' or T.status = 'In Progress'
group by U.email
order by U.email asc;