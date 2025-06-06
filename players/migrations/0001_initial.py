# Generated by Django 5.1.7 on 2025-03-31 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="姓名")),
                (
                    "english_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="英文名"
                    ),
                ),
                ("number", models.CharField(max_length=10, verbose_name="球衣号码")),
                ("team", models.CharField(max_length=100, verbose_name="所属球队")),
                ("position", models.CharField(max_length=20, verbose_name="位置")),
                (
                    "height",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="身高(米)"
                    ),
                ),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="体重(公斤)"
                    ),
                ),
                ("birth_date", models.DateField(verbose_name="出生日期")),
                ("nationality", models.CharField(max_length=50, verbose_name="国籍")),
                ("experience", models.IntegerField(default=0, verbose_name="球龄")),
                (
                    "draft_year",
                    models.IntegerField(blank=True, null=True, verbose_name="选秀年份"),
                ),
                (
                    "draft_position",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="选秀顺位"
                    ),
                ),
                (
                    "college",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="毕业院校"
                    ),
                ),
                (
                    "games_played",
                    models.IntegerField(default=0, verbose_name="出场次数"),
                ),
                (
                    "games_started",
                    models.IntegerField(default=0, verbose_name="首发次数"),
                ),
                (
                    "minutes_per_game",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=4,
                        verbose_name="场均出场时间",
                    ),
                ),
                (
                    "points_per_game",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=4,
                        verbose_name="场均得分",
                    ),
                ),
                (
                    "field_goal_percentage",
                    models.DecimalField(
                        decimal_places=3,
                        default=0,
                        max_digits=4,
                        verbose_name="投篮命中率",
                    ),
                ),
                (
                    "three_point_percentage",
                    models.DecimalField(
                        decimal_places=3,
                        default=0,
                        max_digits=4,
                        verbose_name="三分命中率",
                    ),
                ),
                (
                    "free_throw_percentage",
                    models.DecimalField(
                        decimal_places=3,
                        default=0,
                        max_digits=4,
                        verbose_name="罚球命中率",
                    ),
                ),
                (
                    "rebounds_per_game",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=4,
                        verbose_name="场均篮板",
                    ),
                ),
                (
                    "assists_per_game",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=4,
                        verbose_name="场均助攻",
                    ),
                ),
                (
                    "steals_per_game",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=4,
                        verbose_name="场均抢断",
                    ),
                ),
                (
                    "blocks_per_game",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=4,
                        verbose_name="场均盖帽",
                    ),
                ),
                (
                    "turnovers_per_game",
                    models.DecimalField(
                        decimal_places=1,
                        default=0,
                        max_digits=4,
                        verbose_name="场均失误",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="是否现役"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="player_images/",
                        verbose_name="球员照片",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
            ],
            options={
                "verbose_name": "球员",
                "verbose_name_plural": "球员",
            },
        ),
    ]
