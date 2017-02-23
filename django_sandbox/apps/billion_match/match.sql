CREATE TABLE haystack (date_field text, key_field text, num_field text);
.separator "|"
.import haystack.tmp haystack
CREATE INDEX haystack_key_index ON haystack (key_field);


CREATE TABLE needle (key_field text);
.import needles.tmp needle
CREATE INDEX needle_key_index ON needle (key_field);

-- VACUUM;

SELECT COUNT(*) FROM haystack h INNER JOIN needle n on h.key_field = n.key_field;

