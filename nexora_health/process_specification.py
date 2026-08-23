dataset_specs = {
    "organizations": {
        "file_name": "organizations.csv",

        "column_mapping": {
            "Id": "ORGANIZATION_ID",
            "NAME": "ORGANIZATION_NAME",
            "ADDRESS": "ADDRESS",
            "CITY": "CITY",
            "STATE": "STATE",
            "ZIP": "ZIP_CODE"
        },

        "validation_rules": {}
    },

    "providers": {
        "file_name": "providers.csv",

        "column_mapping": {
            "Id": "PROVIDER_ID",
            "ORGANIZATION": "ORGANIZATION_ID",
            "NAME": "PROVIDER_NAME",
            "GENDER": "GENDER",
            "SPECIALITY": "SPECIALTY",
            "ADDRESS": "ADDRESS",
            "CITY": "CITY",
            "STATE": "STATE",
            "ZIP": "ZIP_CODE"
        },

        "validation_rules": {}
    },

    "payers": {
        "file_name": "payers.csv",

        "column_mapping": {
            "Id": "PAYER_ID",
            "NAME": "PAYER_NAME",
            "OWNERSHIP": "OWNERSHIP",
            "STATE_HEADQUARTERED": "STATE_HEADQUARTERED"
        },

        "validation_rules": {}
    },

    "patients": {
            "file_name": "patients.csv",
    
            "column_mapping": {
                "Id": "PATIENT_ID",
                "BIRTHDATE": "BIRTH_DATE",
                "DEATHDATE": "DEATH_DATE",
                "GENDER": "GENDER",
                "RACE": "RACE",
                "ETHNICITY": "ETHNICITY",
                "GENDER": "GENDER",
                "CITY": "CITY",
                "STATE": "STATE",
                "COUNTY": "COUNTY",
                "ZIP": "ZIP",
                "LAT": "LATITUDE",
                "LON": "LONGITUDE",
                "HEALTHCARE_EXPENSES": "HEALTHCARE_EXPENSES",
                "HEALTHCARE_COVERAGE": "HEALTHCARE_COVERAGE",
                "INCOME": "INCOME"
            },

            "validation_rules": {}
    },

    "encounters": {
        "file_name": "encounters.csv",

        "column_mapping": {
            "Id": "ENCOUNTER_ID",
            "START": "START_TIMESTAMP",
            "STOP": "STOP_TIMESTAMP",
            "PATIENT": "PATIENT_ID",
            "ORGANIZATION": "ORGANIZATION_ID",
            "PROVIDER": "PROVIDER_ID",
            "PAYER": "PAYER_ID",
            "ENCOUNTERCLASS": "ENCOUNTER_CLASS",
            "CODE": "ENCOUNTER_CODE",
            "DESCRIPTION": "ENCOUNTER_DESCRIPTION",
            "TOTAL_CLAIM_COST": "TOTAL_CLAIM_COST",
            "PAYER_COVERAGE": "PAYER_COVERAGE",
        },

        "validation_rules": {}
    },

     "conditions": {
            "file_name": "conditions.csv",
    
            "column_mapping": {
                "START": "START_DATE",
                "STOP": "STOP_DATE",
                "PATIENT": "PATIENT_ID",
                "ENCOUNTER": "ENCOUNTER_ID",
                "CODE": "CONDITION_CODE",
                "DESCRIPTION": "CONDITION_DESCRIPTION"
            },
    
            "validation_rules": {}
        },    
}

