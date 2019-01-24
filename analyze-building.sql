
-- bâtiment avec un nom
with important_building as (
  select abs(osm_id) as osm_id
    , building
    , name
    -- , tags
    , way_area
    , way as geom
  from planet_osm_polygon
  where building is not null
    and building <> 'no'
    and name is not null -- y'en a 2900
  order by way_area desc
  )

select b.osm_id
  , building
  , name
  , way_area
  , elem
  , version
  , n_user
  , n_autocorr
  , n_corr
  , first_at
  , last_at
  , last_uid
  , last_ug
  , st_transform(b.geom, 4326) as geom
from important_building as b
  join osmq.element using(osm_id)
 ;

