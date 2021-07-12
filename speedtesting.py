import speedtest
import datetime

now = datetime.datetime.now()
test = speedtest.Speedtest()

# Get download speed, upload speed, and ping.
print('loading server list ...')
test.get_servers()
best = test.get_best_server()
print(f"Found: {best['host']} located in {best['country']}")
print('performing download test...')
download_result = test.download()
print('performing upload test...')
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download speed : {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload speed : {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping : {ping_result:.2f} ms")

# save results to a txt file
f=open("SpeedLog.txt", "a+")
f.write(now.strftime("%y-%m-%d %H:%M:%S"))
f.write(f"\nDownload speed : {download_result / 1024 / 1024:.2f} Mbit/s\n")
f.write(f"Upload speed : {upload_result / 1024 / 1024:.2f} Mbit/s\n")
f.write(f"Ping : {ping_result:.2f} ms\n")
f.write('  \n')
f.close()
print('done')