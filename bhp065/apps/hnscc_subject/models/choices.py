HIV_STATUS = (
    ('INFECTED', 'HIV infected'),
    ('UNINFECTED', 'HIV uninfected'),
    ('UNK', 'Unknown'), )

SMOKING_STATUS = (
    ('smoker', 'smoker'),
    ('non-smoker', 'non-smoker'),
    ('UNK', 'Unknown'), )

VISIT_REASON = (
    ('UNSCHEDULED', 'Unscheduled visit'),
    ('off study', 'Off study'), )

OFF_STUDY_REASON = (
    ('Completion of protocol', 'Completion of protocol'),
    ('Other, specify: ', 'Other, specify: '), )

HOSPITAL = (
    ('PMH', 'Princess Marina Hospital'),
    ('BLH', 'BAMALETE'),
    ('MAHALAPYE', 'Mahalapye'),
    ('RAMOTSWA', 'Ramotswa'),
    ('DENTAL', 'DENTAL'),
    ('OPD', 'OPD'),
    ('JWANENG', 'Jwaneng'),
    ('ENT', 'ENT'),
    ('KANYE', 'Kanye'), )

DATA_COLLECTION_TYPE = (
    ('contemporary', 'Contemporary'),
    ('historical', 'Historical'), )

REASON_NOT_DRAWN = (
    ('not enough tissue', 'There was not enough tissue'),
    ('technical failure', 'Technical failure'),
    ('no_supplies', 'No supplies'), )
