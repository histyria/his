from django.db import models
from django.contrib.auth.models import User




class ArEn(models.Model):
    arb_char = models.CharField(db_column='ARB_CHAR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    eng_char = models.CharField(db_column='ENG_CHAR', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
       
        db_table = 'ar_en'


class ConsultantDr(models.Model):
    department_code = models.CharField(db_column='DEPARTMENT_CODE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    clnc_code = models.CharField(db_column='CLNC_CODE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    clnc_date = models.CharField(db_column='CLNC_DATE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    clnc_tme = models.CharField(db_column='CLNC_TME', max_length=19, blank=True, null=True)  # Field name made lowercase.
    patiant_no = models.CharField(db_column='PATIANT_NO', max_length=7, blank=True, null=True)  # Field name made lowercase.
    consul_dr = models.CharField(db_column='CONSUL_DR', max_length=8, blank=True, null=True)  # Field name made lowercase.
    consul_text = models.CharField(db_column='CONSUL_TEXT', max_length=455, blank=True, null=True)  # Field name made lowercase.
    consul_date = models.CharField(db_column='CONSUL_DATE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    consultant_dr = models.CharField(db_column='CONSULTANT_DR', max_length=8, blank=True, null=True)  # Field name made lowercase.
    consultant_date = models.CharField(db_column='CONSULTANT_DATE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    findings = models.CharField(db_column='FINDINGS', max_length=596, blank=True, null=True)  # Field name made lowercase.
    recomm = models.CharField(db_column='RECOMM', max_length=421, blank=True, null=True)  # Field name made lowercase.
    consul_no = models.CharField(db_column='CONSUL_NO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    consul_type = models.CharField(db_column='CONSUL_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pr_dia = models.CharField(db_column='PR_DIA', max_length=409, blank=True, null=True)  # Field name made lowercase.
    clnc_code_dest = models.CharField(db_column='CLNC_CODE_DEST', max_length=4, blank=True, null=True)  # Field name made lowercase.
    refrl_clinc = models.CharField(db_column='REFRL_CLINC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    refrl_doc = models.CharField(db_column='REFRL_DOC', max_length=8, blank=True, null=True)  # Field name made lowercase.
    seq = models.CharField(db_column='SEQ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    bleepno = models.CharField(db_column='BLEEPNO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    speciality_code = models.CharField(db_column='SPECIALITY_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    close_discharge = models.CharField(db_column='CLOSE_DISCHARGE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    sec_code = models.CharField(db_column='SEC_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rec_type = models.CharField(db_column='REC_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    refrl_to_clinc = models.CharField(db_column='REFRL_TO_CLINC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    record_no = models.CharField(db_column='RECORD_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
       
        db_table = 'consultant_dr'
    def __str__(self):
        return  str(self.patiant_no)



class Nationality(models.Model):
    country_code = models.CharField(db_column='COUNTRY_CODE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    country_desc = models.CharField(db_column='COUNTRY_DESC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    area_code = models.CharField(db_column='AREA_CODE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    male_nationality_desc = models.CharField(db_column='MALE_NATIONALITY_DESC', max_length=16, blank=True, null=True)  # Field name made lowercase.
    female_nationality_desc = models.CharField(db_column='FEMALE_NATIONALITY_DESC', max_length=16, blank=True, null=True)  # Field name made lowercase.
    country_e_desc = models.CharField(db_column='COUNTRY_E_DESC', max_length=23, blank=True, null=True)  # Field name made lowercase.
    nationality_e_desc = models.CharField(db_column='NATIONALITY_E_DESC', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
       
        db_table = 'Nationality'


class patient_file(models.Model):
    department_code = models.CharField(db_column='DEPARTMENT_CODE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    registration_date = models.CharField(db_column='REGISTRATION_DATE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    patiant_no = models.CharField(db_column='PATIANT_NO', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ar_patiant_name = models.CharField(db_column='AR_PATIANT_NAME', max_length=42, blank=True, null=True)  # Field name made lowercase.
    en_patiant_name = models.CharField(db_column='EN_PATIANT_NAME', max_length=69, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.CharField(db_column='BIRTH_DATE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='nationality', max_length=3, blank=True, null=True)  # Field name made lowercase.
    place_of_birth = models.CharField(db_column='PLACE_OF_BIRTH', max_length=21, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=1, blank=True, null=True)  # Field name made lowercase.
    religion_code = models.CharField(db_column='RELIGION_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    social_number = models.CharField(db_column='SOCIAL_NUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mobile_no = models.CharField(db_column='MOBILE_NO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mother_name = models.CharField(db_column='MOTHER_NAME', max_length=31, blank=True, null=True)  # Field name made lowercase.
    clinec_code = models.CharField(db_column='CLINEC_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    birth_g_date = models.CharField(db_column='BIRTH_G_DATE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    file_status = models.CharField(db_column='FILE_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    file_flag = models.CharField(db_column='FILE_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    file_type = models.CharField(db_column='FILE_TYPE', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
       
        db_table = 'patient_file'
    def __str__(self):
        return  str(self.ar_patiant_name)


class Sheet1(models.Model):
    region_code = models.CharField(db_column='REGION_CODE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    department_code = models.CharField(db_column='DEPARTMENT_CODE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    clnc_code = models.CharField(db_column='CLNC_CODE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    clnc_date = models.CharField(db_column='CLNC_DATE', max_length=21, blank=True, null=True)  # Field name made lowercase.
    clnc_time = models.CharField(db_column='CLNC_TIME', max_length=19, blank=True, null=True)  # Field name made lowercase.
    patiant_no = models.CharField(db_column='PATIANT_NO', max_length=7, blank=True, null=True)  # Field name made lowercase.
    main_code = models.CharField(db_column='MAIN_CODE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sub1_code = models.CharField(db_column='SUB1_CODE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    event_value = models.CharField(db_column='EVENT_VALUE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    event_time = models.CharField(db_column='EVENT_TIME', max_length=19, blank=True, null=True)  # Field name made lowercase.
    dscrptn = models.CharField(db_column='DSCRPTN', max_length=4, blank=True, null=True)  # Field name made lowercase.
    clnc_ordr_no = models.CharField(db_column='CLNC_ORDR_NO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    evnt_flag = models.CharField(db_column='EVNT_FLAG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    evnt_date = models.CharField(db_column='EVNT_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    user_region_code = models.CharField(db_column='USER_REGION_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    user_code = models.CharField(db_column='USER_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trans_date = models.CharField(db_column='TRANS_DATE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ins_user_code = models.CharField(db_column='INS_USER_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ins_user_date = models.CharField(db_column='INS_USER_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    upd_user_code = models.CharField(db_column='UPD_USER_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    upd_user_date = models.CharField(db_column='UPD_USER_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ins_date = models.CharField(db_column='INS_DATE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rec_type = models.CharField(db_column='REC_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    record_no = models.CharField(db_column='RECORD_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
       
        db_table = 'sheet_1'
