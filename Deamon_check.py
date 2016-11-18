#check some number of hosts for a daemon and send email about the hosts that did not have the daemon running.

import os,sys,paramiko,threading,re
cmd = "sudo initctl | grep dmesg"
outlock = threading.Lock()

def log_in(h):
    # SSH each host and get the output
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(h, 'username', 'password')
    # the output of command is present in the stdout
    stdin,stdout,stderr = ssh.exec_command(cmd)
    stdin.write('username \n')
    stdin.flush()
    # using lock for each thread to access the stdout buffer
#    outlock.aquire()
    output = stdout.readlines()
#    outlock.release()
    check_stat(output,h)

def check_stat(output,h)
    # Implemented RegEx to match the pattern 'Stop' or 'start' for each output
    str = " ".join(output)
    pattern = r'\w+\s+(\w+)'
    matched = re.match(pattern, str.lower())
    # matched.group(1) conatins stop or start (\w+)
    matched = matched.group(1)
#   matched = matched.split()
    #check the condition and send mail
    if 'stop' in matched:
        outlock.aquire()
        not_working.append(h)
        outlock.release()
#        send_mail(msg,h,stat = True)
    elif 'start' in matched:
        outlock.aquire()
        working.append(h)
        outlock.release()
    else:
        outlock.aquire()
        nothing.append(h)
        outlock.release()
#        send_mail(msg,h,stat=False)

def send_mail(msg,stat):
    # sending mail based the status in earlier condition.
    server = smtplib.SMTP("mail.google.com", '576')
    server.login("username", "password")

    if (stat):
        msg = ("the service is stopped for the following hosts: %s", %("".join(not_working)))
    elif:
        msg = ("the service is running fine for host %s", %("".join(working)))
    else:
        msg = (" no service running on host %s", %("".join(nothing)))

    server.sendmail("yourEmail", "TargetEmail", msg)
    server.exit()

def main_func():
    working = []
    not_working[]
    nothing=[]
    thread=[]
    # opens the host file and list of host is created
    with open("host.txt", 'r') as fout:
        host = fout.readlines()
        
        # for each host create a thread which runs SSH through log_in()
        for ip in host:
            new_thread = threading.Thread(target= log_in, arg = (ip, ))
            # check log_in()
            new_thread.start()
            thread.append(t)
            # join the thread after finished
            for x in thread:
                x.join()
#        send_mail(msg, Flag1 = True, Flag2 = False)
        send_mail(str(not_working),True)
        send_mail(str(working),False)


if __name__=='__main__':
    main_func()
