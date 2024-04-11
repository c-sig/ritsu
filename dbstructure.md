Table user {
  id string [pk]
  joined_at int
  status enum("full", "probationary", "trial", "collaborator")
  activity enum("active", "inactive", "retired", "hiatus")
}

Table qualification {
  id string [pk]
  qualification_code string
}

Table role {
  id int [pk]
  qualification string [ref: > qualification.id]
}

Table group {
  id int [pk]
  mangaupdates_id int
  merged_at int
}

Table series {
  id int [pk]
  mangaupdates_id int
  group_id int [ref: > group.id]
  status enum("ongoing", "completed", "dropped")
}

Table chapter {
  id int [pk]
  series_id int [ref: > series.id]
  status enum("backlog", "in-progress", "finished")
}

Table page {
  id int [pk]
  number int
  chapter_id int [ref: > chapter.id]
}

Table job {
  id int [pk]
  role_id int [ref: > role.id]
  order int
  status enum("backlog", "in-progress", "finished")
  claimed_by string [ref: > user.id]
  claimed_on int
  page_id int [ref: > page.id]
}
