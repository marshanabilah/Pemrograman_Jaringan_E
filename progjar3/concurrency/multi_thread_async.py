from broadcast import file_broadcast, config_broadcast
import time
import datetime
import concurrent.futures

def broadcast_all():
    texec = dict()
    configs = config_broadcast()
    status_task = dict()
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    catat_awal = datetime.datetime.now()
    for config in configs:
        print(f"broadcasting file to {config['ip_address']}")
        texec[config['ip_address']] = task.submit(file_broadcast, config['ip_address'],5005)
    for config in configs:
        status_task[config['ip_address']]=texec[config['ip_address']].result()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)

if __name__=='__main__':
    broadcast_all()