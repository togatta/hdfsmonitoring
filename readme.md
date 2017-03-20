## HDFS Monitoring
Script ini dibikin karena gw males buat ngecek lewat panel adminnya, sebenernya tinggal masuk aja sih ke panel admin manajemen hadoopnya tapi bikin alert aja sih lewat email biar aware gitu



## Line Yang Perlu di Ubah
di line 25 sender = '(isi alamat sendernya)' menjadi misal sender = '(test@test.com)' <br />
di line 26 recipients = ['isi alamat si penerimanya'] menjadi misal recipients = ['test1@test.co','test2@test.com']



## Cara Penggunaan 

Jika linenya udah diubah, cara pemakaiannya adalah sebagai berikut : <br />

Tinggal di execute aja sih 

hdfsmonitoring.py

terus dibikin crontabnya per 15 menit atau per 30 menit

