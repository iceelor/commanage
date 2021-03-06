drop view if exists all_score_sum_VIEW;
CREATE VIEW all_score_sum_VIEW AS
SELECT max(member.id) id,
        max(member.name) name,
        max(member.sex) sex,
        max(member.branch) branch,
        max(member.post) post,
        max(member.mem_id) mem_id,
        max(member.phoneNum)  phoneNum,
        max(member.join_date) join_date,
        max(member.notice) notice,
        count(actrecord.score) join_time,
        sum(case when actinfo.category='changgui' then actrecord.score else 0 end ) changgui_score,
        sum(case when actinfo.category='jiafen' then actrecord.score else 0 end ) jiafen_score,
        sum(case when actinfo.category='jianfen' then actrecord.score else 0 end ) jianfen_score,
        sum(case when actinfo.category='yipiaofoujue' then actrecord.score else 0 end ) yipiaofoujue_score,
        sum(actrecord.score) score

FROM  activityRecord_memberinfo member,
  activityRecord_actinfo actinfo,
  activityRecord_actrecord actrecord
where actinfo.id=actrecord.act_id and actrecord.member_id=member.id
group by member.id;