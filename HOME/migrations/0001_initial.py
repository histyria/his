# Generated by Django 4.0.4 on 2022-04-20 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArEn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arb_char', models.CharField(blank=True, db_column='ARB_CHAR', max_length=1, null=True)),
                ('eng_char', models.CharField(blank=True, db_column='ENG_CHAR', max_length=2, null=True)),
            ],
            options={
                'db_table': 'ar_en',
            },
        ),
        migrations.CreateModel(
            name='ConsultantDr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(blank=True, db_column='DEPARTMENT_CODE', max_length=5, null=True)),
                ('clnc_code', models.CharField(blank=True, db_column='CLNC_CODE', max_length=2, null=True)),
                ('clnc_date', models.CharField(blank=True, db_column='CLNC_DATE', max_length=19, null=True)),
                ('clnc_tme', models.CharField(blank=True, db_column='CLNC_TME', max_length=19, null=True)),
                ('patiant_no', models.CharField(blank=True, db_column='PATIANT_NO', max_length=7, null=True)),
                ('consul_dr', models.CharField(blank=True, db_column='CONSUL_DR', max_length=8, null=True)),
                ('consul_text', models.CharField(blank=True, db_column='CONSUL_TEXT', max_length=455, null=True)),
                ('consul_date', models.CharField(blank=True, db_column='CONSUL_DATE', max_length=19, null=True)),
                ('consultant_dr', models.CharField(blank=True, db_column='CONSULTANT_DR', max_length=8, null=True)),
                ('consultant_date', models.CharField(blank=True, db_column='CONSULTANT_DATE', max_length=19, null=True)),
                ('findings', models.CharField(blank=True, db_column='FINDINGS', max_length=596, null=True)),
                ('recomm', models.CharField(blank=True, db_column='RECOMM', max_length=421, null=True)),
                ('consul_no', models.CharField(blank=True, db_column='CONSUL_NO', max_length=2, null=True)),
                ('consul_type', models.CharField(blank=True, db_column='CONSUL_TYPE', max_length=1, null=True)),
                ('pr_dia', models.CharField(blank=True, db_column='PR_DIA', max_length=409, null=True)),
                ('clnc_code_dest', models.CharField(blank=True, db_column='CLNC_CODE_DEST', max_length=4, null=True)),
                ('refrl_clinc', models.CharField(blank=True, db_column='REFRL_CLINC', max_length=4, null=True)),
                ('refrl_doc', models.CharField(blank=True, db_column='REFRL_DOC', max_length=8, null=True)),
                ('seq', models.CharField(blank=True, db_column='SEQ', max_length=2, null=True)),
                ('bleepno', models.CharField(blank=True, db_column='BLEEPNO', max_length=4, null=True)),
                ('speciality_code', models.CharField(blank=True, db_column='SPECIALITY_CODE', max_length=4, null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=1, null=True)),
                ('close_discharge', models.CharField(blank=True, db_column='CLOSE_DISCHARGE', max_length=19, null=True)),
                ('sec_code', models.CharField(blank=True, db_column='SEC_CODE', max_length=4, null=True)),
                ('rec_type', models.CharField(blank=True, db_column='REC_TYPE', max_length=1, null=True)),
                ('refrl_to_clinc', models.CharField(blank=True, db_column='REFRL_TO_CLINC', max_length=4, null=True)),
                ('record_no', models.CharField(blank=True, db_column='RECORD_NO', max_length=6, null=True)),
            ],
            options={
                'db_table': 'consultant_dr',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(blank=True, db_column='COUNTRY_CODE', max_length=3, null=True)),
                ('country_desc', models.CharField(blank=True, db_column='COUNTRY_DESC', max_length=25, null=True)),
                ('area_code', models.CharField(blank=True, db_column='AREA_CODE', max_length=2, null=True)),
                ('male_nationality_desc', models.CharField(blank=True, db_column='MALE_NATIONALITY_DESC', max_length=16, null=True)),
                ('female_nationality_desc', models.CharField(blank=True, db_column='FEMALE_NATIONALITY_DESC', max_length=16, null=True)),
                ('country_e_desc', models.CharField(blank=True, db_column='COUNTRY_E_DESC', max_length=23, null=True)),
                ('nationality_e_desc', models.CharField(blank=True, db_column='NATIONALITY_E_DESC', max_length=15, null=True)),
            ],
            options={
                'db_table': 'Nationality',
            },
        ),
        migrations.CreateModel(
            name='Sheet1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_code', models.CharField(blank=True, db_column='REGION_CODE', max_length=3, null=True)),
                ('department_code', models.CharField(blank=True, db_column='DEPARTMENT_CODE', max_length=5, null=True)),
                ('clnc_code', models.CharField(blank=True, db_column='CLNC_CODE', max_length=2, null=True)),
                ('clnc_date', models.CharField(blank=True, db_column='CLNC_DATE', max_length=21, null=True)),
                ('clnc_time', models.CharField(blank=True, db_column='CLNC_TIME', max_length=19, null=True)),
                ('patiant_no', models.CharField(blank=True, db_column='PATIANT_NO', max_length=7, null=True)),
                ('main_code', models.CharField(blank=True, db_column='MAIN_CODE', max_length=2, null=True)),
                ('sub1_code', models.CharField(blank=True, db_column='SUB1_CODE', max_length=2, null=True)),
                ('event_value', models.CharField(blank=True, db_column='EVENT_VALUE', max_length=8, null=True)),
                ('event_time', models.CharField(blank=True, db_column='EVENT_TIME', max_length=19, null=True)),
                ('dscrptn', models.CharField(blank=True, db_column='DSCRPTN', max_length=4, null=True)),
                ('clnc_ordr_no', models.CharField(blank=True, db_column='CLNC_ORDR_NO', max_length=4, null=True)),
                ('evnt_flag', models.CharField(blank=True, db_column='EVNT_FLAG', max_length=4, null=True)),
                ('evnt_date', models.CharField(blank=True, db_column='EVNT_DATE', max_length=10, null=True)),
                ('user_region_code', models.CharField(blank=True, db_column='USER_REGION_CODE', max_length=4, null=True)),
                ('user_code', models.CharField(blank=True, db_column='USER_CODE', max_length=4, null=True)),
                ('trans_date', models.CharField(blank=True, db_column='TRANS_DATE', max_length=4, null=True)),
                ('ins_user_code', models.CharField(blank=True, db_column='INS_USER_CODE', max_length=7, null=True)),
                ('ins_user_date', models.CharField(blank=True, db_column='INS_USER_DATE', max_length=10, null=True)),
                ('upd_user_code', models.CharField(blank=True, db_column='UPD_USER_CODE', max_length=7, null=True)),
                ('upd_user_date', models.CharField(blank=True, db_column='UPD_USER_DATE', max_length=10, null=True)),
                ('ins_date', models.CharField(blank=True, db_column='INS_DATE', max_length=4, null=True)),
                ('rec_type', models.CharField(blank=True, db_column='REC_TYPE', max_length=1, null=True)),
                ('record_no', models.CharField(blank=True, db_column='RECORD_NO', max_length=6, null=True)),
            ],
            options={
                'db_table': 'sheet_1',
            },
        ),
        migrations.CreateModel(
            name='patient_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(blank=True, db_column='DEPARTMENT_CODE', max_length=5, null=True)),
                ('registration_date', models.CharField(blank=True, db_column='REGISTRATION_DATE', max_length=19, null=True)),
                ('patiant_no', models.CharField(blank=True, db_column='PATIANT_NO', max_length=7, null=True)),
                ('ar_patiant_name', models.CharField(blank=True, db_column='AR_PATIANT_NAME', max_length=42, null=True)),
                ('en_patiant_name', models.CharField(blank=True, db_column='EN_PATIANT_NAME', max_length=69, null=True)),
                ('birth_date', models.CharField(blank=True, db_column='BIRTH_DATE', max_length=19, null=True)),
                ('place_of_birth', models.CharField(blank=True, db_column='PLACE_OF_BIRTH', max_length=21, null=True)),
                ('sex', models.CharField(blank=True, db_column='SEX', max_length=1, null=True)),
                ('religion_code', models.CharField(blank=True, db_column='RELIGION_CODE', max_length=4, null=True)),
                ('social_number', models.CharField(blank=True, db_column='SOCIAL_NUMBER', max_length=10, null=True)),
                ('mobile_no', models.CharField(blank=True, db_column='MOBILE_NO', max_length=12, null=True)),
                ('mother_name', models.CharField(blank=True, db_column='MOTHER_NAME', max_length=31, null=True)),
                ('clinec_code', models.CharField(blank=True, db_column='CLINEC_CODE', max_length=4, null=True)),
                ('birth_g_date', models.CharField(blank=True, db_column='BIRTH_G_DATE', max_length=19, null=True)),
                ('file_status', models.CharField(blank=True, db_column='FILE_STATUS', max_length=1, null=True)),
                ('file_flag', models.CharField(blank=True, db_column='FILE_FLAG', max_length=1, null=True)),
                ('file_type', models.CharField(blank=True, db_column='FILE_TYPE', max_length=3, null=True)),
                ('Nationality', models.ForeignKey(blank=True, db_column='Nationality', max_length=3, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HOME.nationality')),
            ],
            options={
                'db_table': 'patient_file',
            },
        ),
    ]
