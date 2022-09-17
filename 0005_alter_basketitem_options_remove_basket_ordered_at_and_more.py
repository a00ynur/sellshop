# # Generated by Django 4.0.4 on 2022-09-09 12:59

# from django.db import migrations, models
# import django.db.models.deletion


# class Migration(migrations.Migration):

#     dependencies = [
#         ('product', '0002_color_discount_productreview_productversion_size_tag_and_more'),
#         ('basket', '0004_remove_basket_sub_total_basketitem'),
#     ]

#     operations = [
#         migrations.AlterModelOptions(
#             name='basketitem',
#             options={'verbose_name': 'BasketItem', 'verbose_name_plural': 'BasketItems'},
#         ),
#         migrations.RemoveField(
#             model_name='basket',
#             name='ordered_at',
#         ),
#         migrations.RemoveField(
#             model_name='basket',
#             name='product',
#         ),
#         migrations.RemoveField(
#             model_name='basketitem',
#             name='sub_total',
#         ),
#         migrations.AddField(
#             model_name='basket',
#             name='created_at',
#             field=models.DateTimeField(auto_now_add=True, default=False),
#             preserve_default=False,
#         ),
#         migrations.AddField(
#             model_name='basket',
#             name='update_at',
#             field=models.DateTimeField(auto_now_add=True, default=False),
#             preserve_default=False,
#         ),
#         migrations.AlterField(
#             model_name='basketitem',
#             name='basket',
#             field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.basket'),
#         ),
#         migrations.AlterField(
#             model_name='basketitem',
#             name='count',
#             field=models.IntegerField(blank=True, default=True, null=True),
#         ),
#         migrations.AlterField(
#             model_name='basketitem',
#             name='price',
#             field=models.ImageField(blank=True, null=True, upload_to=''),
#         ),
#         migrations.AlterField(
#             model_name='basketitem',
#             name='productVersion',
#             field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productversion'),
#         ),
#         migrations.AlterField(
#             model_name='billingaddress',
#             name='address',
#             field=models.CharField(max_length=255),
#         ),
#         migrations.CreateModel(
#             name='Order',
#             fields=[
#                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('total_price', models.IntegerField(blank=True, null=True)),
#                 ('created_at', models.DateTimeField(auto_now_add=True)),
#                 ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.basket')),
#             ],
#         ),
#     ]
