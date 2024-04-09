from ..database import DqConnection


def get_users():
    engine = DqConnection('srcUsers').engine_dq
    return engine.execute("""select u.username
                             , max(u.email) as email
                             , max(u.last_name || ' ' || u.first_name || ' ' || coalesce(am.value, '')) as full_name
                             , max(ad.value) as department
                             from user_entity u
                             left join user_attribute am
                             on u.id = am.user_id
                             and am."name" = 'middleName'
                             left join user_attribute ad
                             on u.id = ad.user_id
                             and ad."name" = 'department'
                             where u.last_name is not null and u.first_name is not null
                             and length(u.username) < 20
                             group by u.username""").all()


def get_departments():
    engine = DqConnection('srcUsers').engine_dq
    return engine.execute("""select distinct value as department
                             from user_attribute
                             where "name" = 'department'""").all()
