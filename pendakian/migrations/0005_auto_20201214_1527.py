# Generated by Django 3.0.2 on 2020-12-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendakian', '0004_auto_20201214_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='provinsi',
            field=models.CharField(choices=[('Nanggroe Aceh Darussalam', 'Nanggroe Aceh Darussalam'), ('Sumatera Utara', 'Sumatera Utara'), ('Sumatera Utara', 'Sumatera Utara'), ('Sumatera Barat', 'Sumatera Barat'), ('Sumatera Selatan', 'Sumatera Selatan'), ('Riau', 'Riau'), ('Kepulauan Riau', 'Kepulauan Riau'), ('Jambi', 'Jambi'), ('Bengkulu', 'Bengkulu'), ('Bogor', 'Bogor'), ('Bangka Belitung', 'Bangka Belitung'), ('Banten', 'Banten'), ('DKI Jakarta', 'DKI Jakarta'), ('Jawa Timur', 'Jawa Timur'), ('Jawa Barat', 'Jawa Barat'), ('Jawa Tengah', 'Jawa Tengah'), ('DIY', 'DIY'), ('Bali', 'Bali'), ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'), ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'), ('Kalimantan Barat', 'Kalimantan Barat'), ('Kalimantan Selatan', 'Kalimantan Selatan'), ('Kalimantan Timur', 'Kalimantan Timur'), ('Kalimantan Utara', 'Kalimantan Utara'), ('Kalimantan Tengah', 'Kalimantan Tengah'), ('Gorontalo', 'Gorontalo'), ('Maluku', 'Maluku'), ('Maluku Utara', 'Maluku Utara'), ('Papua Barat', 'Papua Barat'), ('Papua', 'Papua'), ('Sulawesi Barat', 'Sulawesi Barat'), ('Sulawesi Selatan', 'Sulawesi Selatan'), ('Sulawesi Utara', 'Sulawesi Utara'), ('Sulawesi Tengah', 'Sulawesi Tengah'), ('Sulawesi Tenggara', 'Sulawesi Tenggara')], default='Bali', max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='tujuan',
            field=models.CharField(choices=[('Semeru', 'Semeru'), ('Arjuno', 'Arjuno'), ('Argopuro', 'Argopuro'), ('Raung', 'Raung'), ('Kawi', 'Kawi'), ('Lawu', 'Lawu'), ('Sumbing', 'Sumbing'), ('Sindoro', 'Sindoro'), ('Merbabu', 'Merbabu'), ('Merapi', 'Merapi'), ('Prau', 'Prau'), ('Ciremai', 'Ciremai'), ('Papandayan', 'Papandayan'), ('Gede', 'Gede'), ('Cikuray', 'Cikuray'), ('Guntur', 'Guntur'), ('Tangkuban Perahu', 'Tangkuban Perahu'), ('Salak', 'Salak'), ('Dempo', 'Dempo'), ('Latimojong', 'Latimojong'), ('Agung', 'Agung'), ('Kerinci', 'Kerinci'), ('Jaya Wijaya', 'Jaya Wijaya'), ('Rinjani', 'Rinjani'), ('Binaiya', 'Binaiya'), ('Bukit Raya', 'Bukit Raya')], default='Semeru', max_length=100),
        ),
    ]