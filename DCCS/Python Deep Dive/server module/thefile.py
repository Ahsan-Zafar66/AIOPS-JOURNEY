import paramiko

# machine ip address which you want to access remotely
machine_ip = "192.168.43.176"

# hostname
machine_host = "test user"

# hostname apssword
machine_host_pass = "test1234"

# establishing the connection using paramiko
client = paramiko.SSHClient()

# setting the host key
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# passing the machine ip, username and password
client.connect(hostname=machine_ip,username=machine_host,password=machine_host_pass)

# command to run in cliet
command = "dir"

std_inp,std_out,std_error = client.exec_command(command)

print(std_out.read().decode("utf-8"))

# client.close()
