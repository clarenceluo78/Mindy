# Generated by Django 3.2.11 on 2022-03-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CooperationMind',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('coop_mind_name', models.CharField(max_length=64, verbose_name='脑图名称')),
                ('creator', models.BigIntegerField(verbose_name='创建人ID')),
                ('client_id', models.CharField(max_length=64, verbose_name='客户端ID')),
                ('snapshot_data', models.TextField(null=True, verbose_name='脑图数据')),
                ('log_id', models.BigIntegerField(null=True, verbose_name='data对应的操作日志(cooperation_mind_log)ID')),
                ('data_format', models.CharField(max_length=32, verbose_name='数据格式化类型')),
            ],
            options={
                'verbose_name': '脑图表',
                'db_table': 'cooperation_mind',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CooperationMindLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('coop_mind_id', models.BigIntegerField(verbose_name='脑图ID')),
                ('log_uuid', models.CharField(max_length=64, verbose_name='操作UUID')),
                ('log_content', models.CharField(max_length=1024, verbose_name='操作内容')),
                ('operator', models.BigIntegerField(null=True, verbose_name='操作人')),
                ('operator_ip', models.CharField(max_length=32, verbose_name='操作人IP')),
                ('client_id', models.CharField(max_length=64, verbose_name='客户端ID')),
            ],
            options={
                'verbose_name': '操作日志表',
                'db_table': 'cooperation_mind_log',
                'ordering': ['id'],
            },
        ),
        migrations.AddIndex(
            model_name='cooperationmindlog',
            index=models.Index(fields=['coop_mind_id'], name='cooperation_coop_mi_32e0df_idx'),
        ),
        migrations.AddIndex(
            model_name='cooperationmindlog',
            index=models.Index(fields=['operator'], name='cooperation_operato_ef7add_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='cooperationmindlog',
            unique_together={('coop_mind_id', 'log_uuid')},
        ),
        migrations.AddIndex(
            model_name='cooperationmind',
            index=models.Index(fields=['creator'], name='cooperation_creator_6c1015_idx'),
        ),
    ]
